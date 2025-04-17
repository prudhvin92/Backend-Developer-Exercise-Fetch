## Example Test
```powershell
$testReceipt = @{...} | ConvertTo-Json
Invoke-WebRequest -Uri "http://localhost:5000/receipts/process" -Method POST -Body $testReceipt -ContentType "application/json"
