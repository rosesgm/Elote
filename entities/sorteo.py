import random
# sorteo de la suerte


class Sorteo:
    def __init__(self, numero1, numero2,  numero3):
        self.numero1=numero1
        self.numero2=numero2
        self.numero3=numero3
        
    def ganador(self)-> bool:
            
        valor1=int(self.numero1)
        valor2=int(self.numero2)
        valor3=int(self.numero3)
        ganador=random.randint(1,100)

        if valor1==ganador  or valor2==ganador or valor3==ganador:
            return True
        else:
            return False


    

    