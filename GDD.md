\# \*\*Game Design Document (GDD) – Procedural Breakout\*\*



---



\## \*\*1. Game Overview\*\*



\* \*\*Título:\*\* Procedural Breakout

\* \*\*Gênero:\*\* Arcade / Puzzle (Quebra-blocos)

\* \*\*Plataforma:\*\* Desktop (Python + Pygame)

\* \*\*Visual:\*\* Apenas blocos, retângulos e círculos (Pygame shapes)

\* \*\*Resumo:\*\*

&nbsp; O jogador controla uma barra na base da tela para rebater uma bola e quebrar todos os blocos do topo. Cada partida possui um layout único de blocos gerado aleatoriamente, tornando o desafio sempre novo. O objetivo é destruir todos os blocos sem deixar a bola cair.



---



\## \*\*2. Mecânicas Principais\*\*



\* \*\*Barra do jogador:\*\*



&nbsp; \* Controlada pelo teclado (←, →).

&nbsp; \* Sempre horizontal, posicionada na parte inferior da tela.

&nbsp; \* Dimensão, cor e velocidade fixas.

\* \*\*Bola:\*\*



&nbsp; \* Movimento constante e diagonal; rebate nas paredes, barra e blocos.

&nbsp; \* Perde o jogo se cair além da barra.

&nbsp; \* Cor, velocidade e tamanho fixos.

\* \*\*Blocos:\*\*



&nbsp; \* Gerados proceduralmente: posição, cor e quantidade variam a cada partida.

&nbsp; \* Sempre em linhas e colunas, mas podem ter espaçamentos ou lacunas aleatórias.

&nbsp; \* Bloco destruído ao ser atingido pela bola.

\* \*\*Score:\*\*



&nbsp; \* Pontuação por bloco destruído.

&nbsp; \* Score exibido no topo.



---



\## \*\*3. Geração Procedural do Layout\*\*



\* \*\*Quantidade de linhas e colunas de blocos:\*\*



&nbsp; \* Definidas aleatoriamente dentro de limites (ex: 4–8 linhas, 6–12 colunas).

\* \*\*Blocos podem faltar em posições aleatórias\*\* ("buracos" no layout).

\* \*\*Cores dos blocos:\*\*



&nbsp; \* Definidas aleatoriamente, mas em paleta harmônica (evitar excesso de brilho).

\* \*\*Cada bloco ocupa espaço fixo; blocos e espaços alinhados em grid.\*\*



---



\## \*\*4. Fluxo do Jogo\*\*



1\. \*\*Menu inicial:\*\*



&nbsp;  \* Título, botão “Start”, instruções rápidas.

2\. \*\*Geração do nível:\*\*



&nbsp;  \* Gera grid procedural dos blocos antes da partida iniciar.

3\. \*\*Gameplay:\*\*



&nbsp;  \* Jogador controla barra, bola é lançada automaticamente.

&nbsp;  \* Bola rebate, quebra blocos, score sobe.

&nbsp;  \* Se a bola cair, jogador perde.

&nbsp;  \* Se todos os blocos sumirem, jogador vence.

4\. \*\*Game Over/Vitória:\*\*



&nbsp;  \* Mostra mensagem e score.

&nbsp;  \* Opção de jogar novamente (novo layout aleatório).



---



\## \*\*5. Controles\*\*



\* \*\*Seta Esquerda/Direita:\*\* mover a barra.

\* \*\*Espaço:\*\* iniciar a bola (primeiro lançamento).

\* \*\*R:\*\* reiniciar partida.

\* \*\*ESC:\*\* sair do jogo.



---



\## \*\*6. Interface \& Visual\*\*



\* \*\*Sem imagens externas.\*\*

\* \*\*Barra:\*\* retângulo preenchido (cor única).

\* \*\*Bola:\*\* círculo pequeno (cor contrastante).

\* \*\*Blocos:\*\* retângulos coloridos, em grid procedural.

\* \*\*Fundo:\*\* cor sólida ou gradiente simples via Pygame.

\* \*\*Score:\*\* texto no topo.

\* \*\*Mensagens de vitória/derrota:\*\* texto grande no centro.



---



\## \*\*7. Regras \& Condições de Fim de Jogo\*\*



\* \*\*Perde:\*\* quando a bola ultrapassa a barra e toca a base da tela.

\* \*\*Ganha:\*\* quando todos os blocos são destruídos.

\* \*\*Restart:\*\* sempre começa um novo layout procedural.



---



\## \*\*8. Possíveis Melhorias Futuras\*\*



\* Vidas extras.

\* Power-ups nos blocos.

\* Níveis em sequência (com dificuldades/procedimentos diferentes).

\* Efeitos visuais com partículas Pygame.



---



\## \*\*9. Estrutura de Pastas\*\*



```

ProceduralBreakout/

│

├── main.py

├── README.md

├── requirements.txt

├── /assets/         # apenas fontes ou arquivos de som (opcional, nunca imagens)

└── /src/

&nbsp;    ├── game.py

&nbsp;    ├── level\_generator.py

&nbsp;    ├── paddle.py

&nbsp;    ├── ball.py

&nbsp;    ├── block.py

&nbsp;    └── ui.py

```



> \*\*Obs.:\*\* Tudo desenhado com código! Nada de imagens externas.



---



\## \*\*10. Exemplo de Algoritmo Procedural dos Blocos\*\*



```python

import random



def generate\_blocks(rows\_range=(4,8), cols\_range=(6,12)):

&nbsp;   rows = random.randint(\*rows\_range)

&nbsp;   cols = random.randint(\*cols\_range)

&nbsp;   grid = \[]

&nbsp;   for y in range(rows):

&nbsp;       row = \[]

&nbsp;       for x in range(cols):

&nbsp;           # 80% de chance de existir bloco nesta posição

&nbsp;           if random.random() < 0.8:

&nbsp;               color = random.choice(\[

&nbsp;                 (255,0,0), (0,255,0), (0,0,255),

&nbsp;                 (255,255,0), (0,255,255), (255,0,255)

&nbsp;               ])

&nbsp;               row.append({'exists': True, 'color': color})

&nbsp;           else:

&nbsp;               row.append({'exists': False})

&nbsp;       grid.append(row)

&nbsp;   return grid

