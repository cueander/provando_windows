



def game():
    # Let's start to play
    make_choice = True

    while make_choice:
        # ask to choice between options
        Question =  input('Primer Turno: \r\n')
        Question2 =  input('Segundo Turno: \r\n')

        

        if Question == 'Piedra' and Question2 == 'Piedra':
            print('Empate, Intenta Nuevamente')
            print('Escribe "X" para salir del juego')
            game()
        elif Question == 'Piedra' and Question2 == 'Papel':
            print('El jugador Num 2 ha ganado')
            print('Escribe "X" para salir del juego')
            game()
        elif Question == 'Piedra' and Question2 == 'Tijeras':
            print('El jugador Num 1 ha ganado')
            print('Escribe "X" para salir del juego')
            game()
        elif Question == 'Papel' and Question2 == 'Piedra':
            print('El jugador Num 1 ha ganado')
            print('Escribe "X" para salir del juego')
            game()
        elif Question == 'Papel' and Question2 == 'Papel':
            print('Empate, Intenta Nuevamente')
            print('Escribe "X" para salir del juego')
            game()
        elif Question == 'Papel' and Question2 == 'Tijeras':
            print('El jugador Num 2 ha ganado')
            print('Escribe "X" para salir del juego')
            game()
        elif Question == 'Tijeras' and Question2 == 'Piedra':
            print('El jugador Num 2 ha ganado')
            print('Escribe "X" para salir del juego')
            game()
        elif Question == 'Tijeras' and Question2 == 'Papel':
            print('El jugador Num 1 ha ganado')
            print('Escribe "X" para salir del juego')
            game()
        elif Question == 'Tijeras' and Question2 == 'Tijeras':
            print('Empate, Intenta Nuevamente')
            print('Escribe "X" para salir del juego')
            game()
        elif Question == 'X':
            print('El juego terminó')
            make_choice = False

            
game()