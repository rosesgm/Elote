#Hacer una conversion de moneda
class Currency:
    def __init__(self, pesos):
        self.pesos = pesos

    def to_dollars(self, exchange_rate=19):
        
            dollars = float(self.pesos) / exchange_rate
            return f"${dollars:.2f} USD"
        
   