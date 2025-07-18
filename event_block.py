        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continue
            if event.type == pygame.KEYDOWN:
                if menu_state == 'pause':
                    print('Menu de pausa aberto')
                    menu_state = 'pause'
                elif menu_state == 'options':
                    print('Menu de opções ativado')
                elif game_state == 'playing' and event.key == pygame.K_ESCAPE:
                    menu_state = 'pause'
                    print('Menu de pausa ativado')
                # ... resto dos eventos do jogo ...

