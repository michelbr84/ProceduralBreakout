# Script para compilação completa do APK/AAB Android
Write-Host "Iniciando compilação completa do Android..."

# Limpar e construir debug
wsl -d Ubuntu -- bash -c "cd /mnt/g/Jogos/ProceduralBreakout/android_build && buildozer android clean && buildozer -v android debug"

# Opcional: construir release AAB
# wsl -d Ubuntu -- bash -c "cd /mnt/g/Jogos/ProceduralBreakout/android_build && buildozer -v android release aab"

Write-Host "Compilação Android concluída. Verifique os arquivos em android_build/bin/"
