import yaml
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class AgentConfig:
    model_name: str = "meta-llama/Meta-Llama-3.1-8B-Instruct"
    max_context_length: int = 4000
    temperature: float = 0.7
    top_p: float = 0.9
    torch_dtype: str = "float16"  # FP16 precision
    use_flash_attention: bool = True
    use_tf32: bool = True  # Enable TF32 for Ampere GPUs
    workspace_path: str = "./workspace"
    enable_git: bool = True
    backup_edits: bool = True
    batch_size: int = 4  # For batch inference
    max_memory_fraction: float = 0.9  # GPU memory allocation
    
    @classmethod
    def from_yaml(cls, config_path: str):
        with open(config_path, 'r') as f:
            config_data = yaml.safe_load(f)
        return cls(**config_data)
    
    def to_yaml(self, config_path: str):
        with open(config_path, 'w') as f:
            yaml.dump(self.__dict__, f, default_flow_style=False)

# Example config.yaml for FP16
config_yaml = """
model_name: "meta-llama/Meta-Llama-3.1-8B-Instruct"
max_context_length: 4000
temperature: 0.7
top_p: 0.9
torch_dtype: "float16"
use_flash_attention: true
use_tf32: true
workspace_path: "./workspace"
enable_git: true
backup_edits: true
batch_size: 4
max_memory_fraction: 0.9
"""
