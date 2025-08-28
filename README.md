# Procedural Breakout

## Descrição
Um jogo arcade/puzzle do tipo quebra-blocos, feito em Python com Pygame (desktop) e Kivy (Android). Cada partida possui um layout único de blocos gerado proceduralmente, tornando o desafio sempre novo. O objetivo é destruir todos os blocos sem deixar a bola cair.

### Plataformas Suportadas
- **Desktop**: Python + Pygame
- **Android**: Python + Kivy + Buildozer (APK/AAB)

## Índice
- [Procedural Breakout](#procedural-breakout)
  - [Descrição](#descrição)
  - [Índice](#índice)
  - [Instalação](#instalação)
  - [Uso](#uso)
  - [Contribuição](#contribuição)
  - [Agradecimentos](#agradecimentos)
  - [Notas Adicionais](#notas-adicionais)

## Instalação
1. Clone o repositório:
   ```sh
   git clone https://github.com/michelbr84/ProceduralBreakout.git
   cd ProceduralBreakout
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Uso

### Desktop (Pygame)
Execute o jogo com:
```sh
python main.py
```

### Android (Kivy)
Para compilar para Android:

1. **Configurar ambiente:**
   ```powershell
   .\setup_android_build.ps1
   ```

2. **Compilar APK:**
   ```powershell
   .\test_android_build.ps1
   ```

3. **Ou manualmente:**
   ```bash
   wsl -d Ubuntu
   cd /mnt/g/Jogos/ProceduralBreakout/android_build
   buildozer -v android debug
   ```

### Testar versão Kivy (Desktop)
```sh
python main_kivy.py
```

## Contribuição
Contribuições são bem-vindas! Abra issues ou pull requests.

## Agradecimentos
- Comunidade Pygame
- Inspiração: Breakout clássico

## Notas Adicionais
- Todo o visual é desenhado via código, sem imagens externas.
- Para detalhes do design, veja `docs/GDD.md`.
- Sons e fontes podem ser adicionados em `/assets`.
- **Controles Android**: Tap para lançar bola, swipe horizontal para mover paddle.
- **Compatibilidade**: Funciona em Android 5.0+ (API 21+).
- **Orientação**: Landscape recomendado para melhor experiência.
