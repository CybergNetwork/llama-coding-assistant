# INSTALLATION

## Download project directory
```
git clone https://github.com/CybergNetwork/llama-coding-assistant.git
cd llama-coding-assistant
```
## Create virtual environment
```
python -m venv venv
```
## Activate virtual environment
```
source venv/bin/activate
```
## Upgrade pip
```
pip install --upgrade pip
```
## Install dependencies
```
pip install -r requirements.txt
```
## Environment setup from project root
```
chmod +x scripts/setup_environment.sh
./scripts/setup_environment.sh
```
## Install tree-sitter parsers
```
chmod +x scripts/install_tree_sitter.sh
./scripts/install_tree_sitter.sh
```
## Install and login to Hugging Face
```
pip install huggingface_hub
huggingface-cli login
```
## Download model (optional - will download on first use)
```
python scripts/download_model.py
```
# Commands to Run from Each Directory

## From Project Root (llama-coding-assistant/)

# Initial setup
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```
# Run the agent CLI
```
python run_agent.py
```
# Run the web server
```
python run_server.py
```
# Run tests
```
pytest tests/
```
# Install as package
```
pip install -e .
```
# From scripts/ directory
```
bashcd scripts
```
# Setup environment
```
chmod +x setup_environment.sh
./setup_environment.sh
```
# Install tree-sitter
```
chmod +x install_tree_sitter.sh
./install_tree_sitter.sh
```
# Download model
```
python download_model.py
```
# Run benchmarks
```
python benchmark.py
```
# From tree-sitter/ directory
```
bashcd tree-sitter
```
# Build parsers
```
python build.py
```
# Check if parsers are built
```
ls -la parsers/
```
# From tests/ directory
```
bashcd tests
```
# Run all tests
```
python -m pytest
```
# Run specific test file
```
python -m pytest test_agent.py
```
# Run with coverage
```
python -m pytest --cov=src
```
# Run integration tests
```
python -m pytest test_integration.py -v
```
# From web/ directory
```
bashcd web
```
# Serve static files (for development)
```
python -m http.server 8080
```
# Or use a simple server
```
python -c "import http.server; http.server.HTTPServer(('', 8080), http.server.SimpleHTTPRequestHandler).serve_forever()"
```
# From src/ directory
```
bashcd src
```
# Run individual modules for testing
```
python -m core.agent
```
```
python -m utils.performance
```
```
python -m features.refactoring
```
# Development Workflow

1. Daily Development

# Activate environment
```
source venv/bin/activate
```
# Pull latest changes
```
git pull origin main
```
# Run tests
```
pytest tests/
```
# Start development server
```
python run_server.py
```
2. Adding New Feature

# Create feature branch
```
git checkout -b feature/new-feature
```
# Add new module
```
touch src/features/new_feature.py
```
# Add tests
```
touch tests/test_new_feature.py
```
# Run tests
```
pytest tests/test_new_feature.py
```
3. Performance Testing

# Run benchmarks
```
python scripts/benchmark.py
```
# Monitor GPU usage
```
nvidia-smi
```
# Check memory usage
```
python -c "import torch; print(torch.cuda.memory_allocated() / 1024**3, 'GB')"
```
Docker Setup (Optional)

Create Dockerfile:
```
bashtouch Dockerfile
touch docker-compose.yml
touch .dockerignore
```
Run with Docker:

# Build image
```
docker build -t llama-coding-assistant .
```
# Run container
```
docker run -p 8000:8000 llama-coding-assistant
```
# Or with docker-compose
```
docker-compose up
```
Production Deployment

1. Server Deployment

# Install production dependencies
```
pip install gunicorn
```
# Run with gunicorn
```
gunicorn -w 4 -k uvicorn.workers.UvicornWorker src.api.server:app
```
# Or with uvicorn
```
uvicorn src.api.server:app --host 0.0.0.0 --port 8000 --workers 4
```
2. Environment Variables

# Set production environment
```
export ENVIRONMENT=production
export MODEL_PATH=/path/to/model
export WORKSPACE_PATH=/path/to/workspace
export GPU_MEMORY_FRACTION=0.9
```
4. Monitoring

# Check logs
```
tail -f logs/agent.log
```
# Monitor performance
```
python scripts/benchmark.py --production
```
Troubleshooting Commands

GPU Issues

# Check CUDA availability
```
python -c "import torch; print(torch.cuda.is_available())"
```
# Check GPU memory
```
nvidia-smi
```
# Clear GPU cache
```
python -c "import torch; torch.cuda.empty_cache()"
```
Model Issues

# Check model loading
```
python -c "from transformers import AutoTokenizer; print(AutoTokenizer.from_pretrained('meta-llama/Meta-Llama-3.1-8B-Instruct'))"
```
# Download model manually
```
python scripts/download_model.py --model-name meta-llama/Meta-Llama-3.1-8B-Instruct
```
Dependencies Issues

# Reinstall requirements
```
pip install -r requirements.txt --force-reinstall
```
# Check conflicting packages
```
pip check
```
# Update all packages
```
pip install -r requirements.txt --upgrade
```
