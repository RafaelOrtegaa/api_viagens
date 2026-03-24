from pydantic import BaseModel
from datetime import date

class UsuarioSchema(BaseModel):
    nome: str
    cpf: str
    data_nascimento: date
    idade: int
    senha: str
    email: str
    usuario: str

# Converte model em schema 
    class Config:
        from_attributes = True


# Define os esquemas usados para validação e entrada/saída de dados da API.
# Ex: como os dados devem chegar e sair nas requisições.