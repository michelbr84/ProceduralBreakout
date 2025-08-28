# Script para testar a compilação Android (debug)
Write-Host "Iniciando teste de compilação Android..."

# Navegar para o diretório de build dentro do WSL e executar buildozer
wsl -d Ubuntu -- bash -c "cd /mnt/g/Jogos/ProceduralBreakout/android_build && buildozer -v android debug"

Write-Host "Teste de compilação concluído. Verifique o APK em android_build/bin/"
