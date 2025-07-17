# Process multiple files efficiently
file_paths = ["file1.py", "file2.py", "file3.py"]
prompts = []

for file_path in file_paths:
    code = file_manager.read_file(file_path)
    prompt = f"Review this code for bugs and improvements:\n{code}"
    prompts.append(prompt)

# Batch inference for better throughput
results = optimizer.batch_inference(agent, prompts, batch_size=2)

for i, result in enumerate(results):
    print(f"Analysis for {file_paths[i]}:")
    print(result)
    print("-" * 50)
