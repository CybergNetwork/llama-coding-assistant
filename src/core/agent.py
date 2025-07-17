from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch

class LlamaCodeAgent:
    def __init__(self, model_name="meta-llama/Meta-Llama-3.1-8B-Instruct"):
        # FP16 configuration for optimal performance
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto",
            trust_remote_code=True,
            low_cpu_mem_usage=True,
            use_flash_attention_2=True  # Enable Flash Attention 2 for better performance
        )
        
        # Optimize for FP16 inference
        self.model.half()  # Ensure model is in FP16
        if torch.cuda.is_available():
            self.model = self.model.cuda()
            # Enable tensor cores optimization
            torch.backends.cuda.matmul.allow_tf32 = True
            torch.backends.cudnn.allow_tf32 = True
        
        # Set pad token
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
            
        # FP16 generation configuration
        self.generation_config = {
            'max_new_tokens': 512,
            'temperature': 0.7,
            'top_p': 0.9,
            'do_sample': True,
            'pad_token_id': self.tokenizer.eos_token_id,
            'use_cache': True,
            'torch_dtype': torch.float16
        }
    
    def generate_response(self, prompt, max_tokens=512):
        """Generate response with FP16 optimization"""
        inputs = self.tokenizer(
            prompt, 
            return_tensors="pt", 
            padding=True, 
            truncation=True, 
            max_length=4096
        )
        
        if torch.cuda.is_available():
            inputs = {k: v.cuda() for k, v in inputs.items()}
        
        with torch.cuda.amp.autocast(dtype=torch.float16):
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=max_tokens,
                    temperature=self.generation_config['temperature'],
                    top_p=self.generation_config['top_p'],
                    do_sample=self.generation_config['do_sample'],
                    pad_token_id=self.generation_config['pad_token_id'],
                    use_cache=self.generation_config['use_cache']
                )
        
        # Decode response
        response = self.tokenizer.decode(
            outputs[0][inputs['input_ids'].shape[1]:], 
            skip_special_tokens=True
        )
        return response.strip()
