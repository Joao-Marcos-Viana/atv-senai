import exemploHeranca
import clear

while True:    
    print('-'*30)
    print('1 - Exemplo de Herança')
    print('2 - Exemplo de Herança Multipla')
    print('-'*30)
    opcao = input()
    match opcao:
        case '1':
            clear.limpar_tela()
            exemploHeranca.heranca()
            print('\n')
            print('\n')
            input()
            clear.limpar_tela()
        case '2':
            clear.limpar_tela()
            exemploHeranca.herancaMultipla()
            print('\n')
            print('\n')
            input()
            clear.limpar_tela()
        case '3':
            break