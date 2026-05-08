import Produto
from tipo_desconto import TipoDesconto

maca = Produto.Produto(nome = "Maçã", preco =0.5, tipo_desconto = TipoDesconto.SEM_DESCONTO, valor_desconto=0)

camisa = Produto.Produto(nome = "Maçã", preco =30.0, tipo_desconto = TipoDesconto.CUPOM, valor_desconto=0.1)

celular = Produto.Produto(nome = "Maçã", preco =1199.9, tipo_desconto = TipoDesconto.PERCENTUAL, valor_desconto=0.15)

