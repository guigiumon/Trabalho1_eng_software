import Produto
from tipo_desconto import TipoDesconto

maca = Produto(nome = "Maçã", preco =0.5, tipo_desconto = TipoDesconto.SEM_DESCONTO, valor_desconto=0)

camisa = Produto(nome = "Maçã", preco =30.0, tipo_desconto = TipoDesconto.CUPOM, valor_desconto=0)

celular = Produto(nome = "Maçã", preco =1199.9, tipo_desconto = TipoDesconto.PERCENTUAL, valor_desconto=0)

