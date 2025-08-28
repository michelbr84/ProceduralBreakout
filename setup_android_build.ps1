# Script para configurar o ambiente de build Android (WSL2 + Buildozer)
Write-Host "Verificando e instalando WSL2..."
wsl --install
Write-Host "Reinicie o computador se solicitado e execute este script novamente."

Write-Host "Instalando Ubuntu no WSL2..."
wsl --install -d Ubuntu

Write-Host "Configurando Buildozer no Ubuntu..."
wsl -d Ubuntu -u root -- bash -c "apt update && apt upgrade -y && apt install -y python3-pip python3-venv git openjdk-17-jdk unzip libffi-dev libssl-dev"
wsl -d Ubuntu -- bash -c "pip3 install --user buildozer Cython==0.29.36"
wsl -d Ubuntu -- bash -c "echo 'export PATH=\$HOME/.local/bin:\$PATH' >> ~/.bashrc && source ~/.bashrc"
Write-Host "Ambiente Buildozer configurado no WSL Ubuntu."
