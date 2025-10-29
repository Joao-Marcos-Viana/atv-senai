def heranca():
    class Funcionarios:#Classe pai
        def __init__(self,nome,email):
            self.nome = nome
            self.email = email
        def detalhes(self):
            pass

    class Gerente(Funcionarios):#Classe Filho
        def __init__(self,nome, email, area):
            super().__init__(nome,email)
            self.area = area
        def detalhes(self):
            print('------Gerentes------')
            print(f'Nome: {self.nome}')
            print(f'E-mail: {self.email}')
            print(f'Gerencia na area de: {self.area}')

    class Professor(Funcionarios):
        def __init__(self,nome,email,materia):
            super().__init__(nome,email)
            self.materia = materia
        def detalhes(self):
            print('------Professores------')
            print(f'Nome: {self.nome}')
            print(f'E-mail: {self.email}')
            print(f'Disciplina: {self.materia}')

    professorGeo = Professor('Gersu','gersu@gmail.com','Geografia')
    professorGeo.detalhes()
    print('\n')
    gerenteProjetos = Gerente('Clodoal','clod@gmail.com','Projetos')
    gerenteProjetos.detalhes()

#----------------------------------------------------------------------------------------------------------------------------------------------
#Exemplo de Herança Multipla (OBS: Só existe em python)
def herancaMultipla():
    class Animal:
        def __init__(self,respirar):
            self.respirar = respirar
        def folego(self):
            print('Está Respirando...')
            
    class Mamifero:
        def __init__(self,amamentar):
            self.amamentar = amamentar
        def sendoAmamentado(self):
            print('Está Sendo Amamentado...')

    class Morcego(Animal, Mamifero):
        def __init__(self, respirar, amamentar, voar):
            Animal.__init__(self,respirar)
            Mamifero.__init__(self,amamentar)
            self.voar = voar
        def voando(self):
            print('Está Voando...')
        
    morcego = Morcego(True, True, True)
    print('--------Morcego--------')
    morcego.folego()
    morcego.sendoAmamentado()
    morcego.voando()    