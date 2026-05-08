from enum import Enum

class TipoDesconto(Enum):
    SEM_DESCONTO = "sem_desconto"
    CUPOM = "cupom"
    PERCENTUAL = "percentual"