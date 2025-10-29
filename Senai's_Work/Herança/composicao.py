def composicao():

    class Motor:
        def ligar(self):
            print('Ligando Motor...')


    class Carro:
        def __init__(self):
            self.motor = Motor()
            
        def dirigir(self):
            self.motor.ligar()
            
    class Barco:
        def __init__(self):
            self.motor = Motor()
        
        def navegar(self):
            self.motor.ligar()