def limpar_tela():#Função que limpa a tela
    import time
    import os
        
    time.sleep(2)
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/Mac
        os.system('clear')