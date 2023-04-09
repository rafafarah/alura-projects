from cpf import Cpf
from cnpj import Cnpj

class Doc:
    @staticmethod
    def create(doc):
        doc = str(doc)
        if 11 == len(doc):
            return Cpf(doc)
        elif 14 == len(doc):
            return Cnpj(doc)
        else:
            raise ValueError("Invalid document")
