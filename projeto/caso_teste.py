# Importamos a classe Produto e as Estratégias em vez do antigo Enum
from Produto import Produto
from Produto import SemDesconto, DescontoCupom, DescontoPercentual

# 1. Produto SEM DESCONTO
# Podemos passar a estratégia SemDesconto() explicitamente ou simplesmente 
# omitir, já que definimos ela como padrão na classe Produto.
maca = Produto(nome="Maçã", preco=0.5, estrategia_desconto=SemDesconto())

# 2. Produto com CUPOM (Valor Fixo)
# Passamos a classe DescontoCupom já com o valor (0.1) embutido nela.
camisa = Produto(nome="Camisa", preco=30.0, estrategia_desconto=DescontoCupom(0.1))

# 3. Produto com PERCENTUAL
# Passamos a classe DescontoPercentual com o valor (0.15, que representa 15%) embutido nela.
celular = Produto(nome="Celular", preco=1199.9, estrategia_desconto=DescontoPercentual(0.15))

# --- Print dos resultados ---
print(maca.printaResultadoComDesconto())
print(camisa.printaResultadoComDesconto())
print(celular.printaResultadoComDesconto())