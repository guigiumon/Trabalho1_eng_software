from tipo_desconto import TipoDesconto
from abc import ABC, abstractmethod

# Interface da Estratégia
class EstrategiaDesconto(ABC):
    @abstractmethod
    def calcular(self, preco: float) -> float:
        pass

# Estratégia 1: Sem desconto
class SemDesconto(EstrategiaDesconto):
    def calcular(self, preco: float) -> float:
        return preco

# Estratégia 2: Desconto Percentual (ex: 10% = 0.10)
class DescontoPercentual(EstrategiaDesconto):
    def __init__(self, percentual: float):
        self.percentual = percentual
        
    def calcular(self, preco: float) -> float:
        # Usando a mesma fórmula do seu código original
        return preco - (preco * self.percentual)

# Estratégia 3: Desconto por Cupom (Valor fixo abatido do preço)
class DescontoCupom(EstrategiaDesconto):
    def __init__(self, valor_cupom: float):
        self.valor_cupom = valor_cupom
        
    def calcular(self, preco: float) -> float:
        # max() evita que o preço fique negativo
        return max(0.0, preco - self.valor_cupom)
    
class Produto:
    # A classe agora recebe a estratégia em vez do enum e do valor
    def __init__(self, nome: str, preco: float, estrategia_desconto: EstrategiaDesconto = None):
        self.nome = nome
        self.preco = preco
        # Se nenhuma estratégia for passada, o padrão é SemDesconto()
        self.estrategia_desconto = estrategia_desconto or SemDesconto()
        
    def calculaValorFinal(self) -> float:
        # A mágica do Strategy: o Produto apenas pede para a estratégia calcular
        return self.estrategia_desconto.calcular(self.preco)
    
    def printaResultadoComDesconto(self) -> str:
        return f"{self.nome} | Preço: R${self.preco:.2f} -> Preço Final: R${self.calculaValorFinal():.2f}"