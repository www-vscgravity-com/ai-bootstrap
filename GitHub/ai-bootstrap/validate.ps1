Write-Host "🔍 Validating capsule integrity..."
 = 0

foreach ( in @("environment.yml", "bootstrap.ipynb", "capsule-meta.yml")) {
    if (Test-Path ) {
        Write-Host "✅ Found "
    } else {
        Write-Host "❌ Missing "
        ++
    }
}

Write-Host "🔁 Validation complete."
exit 
