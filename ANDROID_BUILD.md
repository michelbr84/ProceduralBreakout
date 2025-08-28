# Compilação Android - Procedural Breakout

## Pré-requisitos

### 1. WSL2 (Windows Subsystem for Linux)
```powershell
# Instalar WSL2
wsl --install

# Reiniciar o computador após instalação
```

### 2. Ubuntu no WSL2
```powershell
# Instalar Ubuntu
wsl --install -d Ubuntu

# Ou se já tiver WSL instalado:
wsl -d Ubuntu
```

### 3. Dependências no Ubuntu
```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependências básicas
sudo apt install -y python3-pip python3-venv git openjdk-17-jdk unzip libffi-dev libssl-dev

# Instalar Buildozer
pip3 install --user buildozer Cython==0.29.36

# Adicionar ao PATH
echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

## Estrutura do Projeto Android

```
ProceduralBreakout/
├── main_kivy.py          # Versão Kivy do jogo
├── buildozer.spec        # Configuração Buildozer
├── android_requirements.txt  # Dependências Android
├── build_android.ps1     # Script de build automatizado
├── test_kivy.py          # Script de teste
└── android_build/        # Diretório de build (criado automaticamente)
```

## Passos para Compilação

### 1. Testar Versão Kivy (Desktop)
```powershell
# Instalar dependências Python
pip install kivy numpy

# Testar se funciona
python test_kivy.py

# Testar jogo Kivy
python main_kivy.py
```

### 2. Compilação Automática
```powershell
# Executar script de build
.\build_android.ps1
```

### 3. Compilação Manual (WSL)
```bash
# Acessar WSL
wsl -d Ubuntu

# Navegar para o projeto
cd /mnt/g/Jogos/ProceduralBreakout/android_build

# Compilar debug
buildozer -v android debug

# Compilar release
buildozer -v android release
```

## Configurações do APK

### buildozer.spec
- **Nome**: Procedural Breakout
- **Pacote**: org.proceduralbreakout
- **Versão**: 1.0
- **API Android**: 33 (Android 13)
- **Arquiteturas**: arm64-v8a, armeabi-v7a
- **Orientação**: Landscape
- **Permissões**: INTERNET

### Dependências
- python3
- kivy
- numpy

## Controles Touch

### Controles Implementados
- **Tap na tela**: Lançar bola
- **Swipe horizontal**: Mover paddle
- **Tap no menu**: Iniciar jogo
- **Tap em game over**: Voltar ao menu

### Controles Planejados
- Botões virtuais para pause/menu
- Controles de volume
- Opções de configuração

## Resolução e Otimizações

### Resolução Mobile
- **Padrão**: 1080x1920 (portrait)
- **Suporte**: 720x1280, 1440x2560
- **Orientação**: Landscape (recomendado)

### Otimizações
- Renderização otimizada para mobile
- Controles touch responsivos
- Performance ajustada para dispositivos móveis

## Troubleshooting

### Problemas Comuns

#### 1. Erro de NDK/SDK
```bash
# Limpar cache
rm -rf .buildozer
rm -rf .gradle

# Reinstalar dependências
buildozer android clean
```

#### 2. Erro de permissões
```bash
# Dar permissões de execução
chmod +x buildozer.spec
```

#### 3. Erro de memória
```bash
# Aumentar memória Java
export GRADLE_OPTS="-Xmx2048m"
```

#### 4. Erro de dependências
```bash
# Atualizar buildozer
pip3 install --upgrade buildozer

# Limpar cache pip
pip3 cache purge
```

### Logs de Debug
```bash
# Ver logs detalhados
buildozer -v android debug 2>&1 | tee build.log

# Ver logs específicos
tail -f .buildozer/android/platform/build-*/gradle.log
```

## Distribuição

### APK Debug
- Localização: `android_build/bin/`
- Nome: `proceduralbreakout-1.0-debug.apk`
- Uso: Teste em dispositivos

### APK Release
- Localização: `android_build/bin/`
- Nome: `proceduralbreakout-1.0-release.apk`
- Uso: Distribuição

### AAB (Android App Bundle)
```bash
# Gerar AAB para Play Store
buildozer -v android release aab
```

## Teste em Dispositivo

### 1. Habilitar Depuração USB
- Configurações > Sobre o telefone > Toque 7x em "Número da versão"
- Configurações > Opções do desenvolvedor > Depuração USB

### 2. Instalar APK
```bash
# Via ADB
adb install bin/proceduralbreakout-1.0-debug.apk

# Ou transferir arquivo e instalar manualmente
```

### 3. Testar Funcionalidades
- [ ] Jogo inicia corretamente
- [ ] Controles touch funcionam
- [ ] Sons funcionam
- [ ] Menus funcionam
- [ ] Performance adequada

## Próximos Passos

### Melhorias Planejadas
- [ ] Adicionar ícone personalizado
- [ ] Implementar tela de splash
- [ ] Adicionar vibração
- [ ] Otimizar para diferentes tamanhos de tela
- [ ] Implementar save/load de progresso
- [ ] Adicionar achievements
- [ ] Implementar leaderboards

### Play Store
- [ ] Criar conta de desenvolvedor
- [ ] Preparar assets (ícones, screenshots)
- [ ] Escrever descrição do app
- [ ] Configurar preços e disponibilidade
- [ ] Submeter para revisão

## Suporte

Para problemas específicos:
1. Verificar logs de build
2. Testar em diferentes dispositivos
3. Consultar documentação do Kivy/Buildozer
4. Abrir issue no GitHub do projeto
