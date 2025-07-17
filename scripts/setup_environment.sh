#!/bin/bash

pip install transformers torch accelerate
pip install flash-attn --no-build-isolation  # For Flash Attention 2
pip install langchain langchain-community
pip install tree-sitter tree-sitter-python tree-sitter-javascript
pip install gitpython pyparsing
pip install fastapi uvicorn websockets
pip install huggingface_hub
huggingface-cli login
