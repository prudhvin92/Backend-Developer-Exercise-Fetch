## Example Test
```powershell
$testReceipt = @{...} | ConvertTo-Json
Invoke-WebRequest -Uri "http://localhost:5000/receipts/process" -Method POST -Body $testReceipt -ContentType "application/json"

# Fetch Receipt Processor

## ✅ Features
- Implements all 7 scoring rules from Fetch's challenge
- REST API with two endpoints
- Comprehensive unit tests

## 🚀 Quick Start
```bash
# Setup
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# Run server
python app.py
