# Gerador de Arquivos de Texto
# Programa que recebe texto do usuário e salva em arquivo

def criar_arquivo_txt():
    print("=== GERADOR DE ARQUIVOS TXT ===")
    print("Digite 'sair' para encerrar o programa\n")
    
    while True:
        # Recebe o texto do usuário
        texto = input("Digite o texto que deseja salvar: ")
        
        # Verifica se o usuário quer sair
        if texto.lower() == 'sair':
            print("Programa encerrado!")
            break
        
        # Solicita o nome do arquivo
        nome_arquivo = input("Digite o nome do arquivo (sem extensão): ")
        
        # Adiciona a extensão .txt se não tiver
        if not nome_arquivo.endswith('.txt'):
            nome_arquivo += '.txt'
        
        try:
            # Cria e escreve no arquivo
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write(texto)
            
            print(f"✅ Arquivo '{nome_arquivo}' criado com sucesso!")
            print(f"📁 Localização: {nome_arquivo}")
            
        except Exception as e:
            print(f"❌ Erro ao criar arquivo: {e}")
        
        print("-" * 40)

# Versão mais avançada com opções extras
def criar_arquivo_avancado():
    print("=== GERADOR AVANÇADO DE ARQUIVOS ===")
    
    while True:
        print("\nOpções:")
        print("1 - Criar novo arquivo")
        print("2 - Adicionar ao arquivo existente")
        print("3 - Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '3':
            print("Programa encerrado!")
            break
        
        if opcao in ['1', '2']:
            texto = input("Digite o texto: ")
            nome_arquivo = input("Nome do arquivo: ")
            
            if not nome_arquivo.endswith('.txt'):
                nome_arquivo += '.txt'
            
            try:
                # Modo 'w' = escrever (substitui), 'a' = adicionar
                modo = 'w' if opcao == '1' else 'a'
                
                with open(nome_arquivo, modo, encoding='utf-8') as arquivo:
                    if opcao == '2':  # Se está adicionando, pula linha
                        arquivo.write('\n' + texto)
                    else:
                        arquivo.write(texto)
                
                acao = "criado" if opcao == '1' else "atualizado"
                print(f"✅ Arquivo '{nome_arquivo}' {acao} com sucesso!")
                
            except Exception as e:
                print(f"❌ Erro: {e}")
        else:
            print("❌ Opção inválida!")

# Exemplo com formatação de data
def criar_arquivo_com_data():
    from datetime import datetime
    
    print("=== GERADOR COM DATA/HORA ===")
    
    texto = input("Digite seu texto: ")
    nome_arquivo = input("Nome do arquivo: ")
    
    if not nome_arquivo.endswith('.txt'):
        nome_arquivo += '.txt'
    
    # Adiciona data e hora ao texto
    agora = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
    conteudo = f"Criado em: {agora}\n\n{texto}"
    
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
        
        print(f"✅ Arquivo '{nome_arquivo}' criado com timestamp!")
        
    except Exception as e:
        print(f"❌ Erro: {e}")

# Executa o programa principal
if __name__ == "__main__":
    print("Escolha qual versão executar:")
    print("1 - Versão simples")
    print("2 - Versão avançada") 
    print("3 - Versão com data/hora")
    
    escolha = input("Digite sua escolha: ")
    
    if escolha == '1':
        criar_arquivo_txt()
    elif escolha == '2':
        criar_arquivo_avancado()
    elif escolha == '3':
        criar_arquivo_com_data()
    else:
        print("Opção inválida! Executando versão simples...")
        criar_arquivo_txt()