from pydantic import BaseModel

class MetodoPagamentoSchema(BaseModel):
    
    descricao: str
    nome_financeira: str

    class Config:
        from_attributes = True