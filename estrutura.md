ProceduralBreakout/

│

├── README.md

├── requirements.txt

├── main.py

│

├── /assets/

│   ├── /fonts/

│   └── /sounds/         # (opcional, não usar imagens externas)

│

├── /src/

│   ├── \_\_init\_\_.py

│   ├── game.py              # Gerencia o loop principal e estados do jogo

│   ├── settings.py          # Configurações globais, cores, tamanhos, etc.

│   ├── level\_generator.py   # Lógica procedural dos blocos

│   ├── paddle.py            # Classe da barra (paddle)

│   ├── ball.py              # Classe da bola

│   ├── block.py             # Classe do bloco individual

│   ├── ui.py                # Interface: score, mensagens, menus

│   └── utils.py             # Funções auxiliares genéricas

│

├── /tests/

│   └── test\_level\_generator.py

│

└── /docs/

&nbsp;   ├── GDD.md

&nbsp;   └── manual\_ptbr.md

```



---



\## \*\*Explicação dos Diretórios e Arquivos\*\*



\* \*\*main.py\*\*

&nbsp; Arquivo de entrada que inicializa e roda o jogo.



\* \*\*README.md\*\*

&nbsp; Descrição do projeto, instruções de uso e instalação.



\* \*\*requirements.txt\*\*

&nbsp; Dependências do projeto (principalmente `pygame`).



\* \*\*/assets/\*\*

&nbsp; Apenas para \*\*sons\*\* ou \*\*fontes\*\* (nunca imagens externas).



\* \*\*/src/\*\*

&nbsp; Contém todo o código-fonte do jogo, com arquivos separados por responsabilidade:



&nbsp; \* `game.py`: loop principal, gerenciamento de estados.

&nbsp; \* `settings.py`: constantes e configs.

&nbsp; \* `level\_generator.py`: lógica de geração procedural dos blocos.

&nbsp; \* `paddle.py`, `ball.py`, `block.py`: entidades do jogo.

&nbsp; \* `ui.py`: menus, score, mensagens.

&nbsp; \* `utils.py`: funções de apoio.



\* \*\*/tests/\*\*

&nbsp; Testes automatizados (opcional).



\* \*\*/docs/\*\*

&nbsp; Documentação, GDD, manuais, instruções em português, etc.

