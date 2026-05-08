from tipo_desconto import TipoDesconto

class Produto:
    
    def __init__(self, nome: str, preco: float, tipo_desconto: TipoDesconto = TipoDesconto.SEM_DESCONTO, valor_desconto: float = 0.0):
        self.nome = nome
        self.preco = preco
        self.tipo_desconto = tipo_desconto
        self.valor_desconto = valor_desconto
        
    def calculaValorFinal(self):
        preco_final = self.preco - (self.preco* self.valor_desconto)
        return preco_final
    
    def printaResultadoComDesconto(self) -> str:
        return f"{self.nome} | Preço: R${self.preco:.2f} -> Preço Final: R${self.calculaValorFinal():.2f}"