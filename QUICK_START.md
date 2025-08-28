# Guia Rápido - Android APK

## Pré-requisitos
- Windows 10/11
- WSL2 (será instalado automaticamente)
- Dispositivo Android para teste

## Passos Rápidos

### 1. Configurar Ambiente (Primeira vez)
```powershell
.\setup_android_build.ps1
```

### 2. Compilar APK
```powershell
.\test_android_build.ps1
```

### 3. Instalar no Dispositivo
- Conecte o dispositivo via USB
- Habilite "Depuração USB" nas opções do desenvolvedor
- O APK será gerado em `android_build/bin/`

## Controles Android
- **Tap na tela**: Lançar bola
- **Swipe horizontal**: Mover paddle
- **Tap no menu**: Iniciar jogo
- **Tap em game over**: Voltar ao menu

## Troubleshooting

### WSL não encontrado
```powershell
# Instalar WSL manualmente
wsl --install
# Reiniciar computador
```

### Buildozer não encontrado
```bash
# No WSL Ubuntu
pip3 install --user buildozer Cython==0.29.36
```

### Erro de memória
```bash
# Aumentar memória Java
export GRADLE_OPTS="-Xmx2048m"
```

## Arquivos Importantes
- `main_kivy.py` - Versão Kivy do jogo
- `buildozer.spec` - Configuração Android
- `android_build/` - Diretório de compilação
- `ANDROID_BUILD.md` - Documentação completa

## Suporte
Para problemas específicos, consulte `ANDROID_BUILD.md` ou abra uma issue no GitHub.
