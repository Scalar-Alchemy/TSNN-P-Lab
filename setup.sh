
```bash
#!/bin/bash
echo "Setting up TSNN-P environment..."
pip install --no-cache-dir -r requirements.txt
python -c "import cupy; print('CuPy version:', cupy.__version__)"
echo "Setup complete!"
```
