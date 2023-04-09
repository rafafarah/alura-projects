from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, cnpj):
        if self.isvalid(cnpj):
            self._cnpj = cnpj
        else:
            raise ValueError("Invalid CNPJ")

    def __str__(self):
        return self.format()

    def isvalid(self, cnpj):
        return CNPJ().validate(cnpj)

    def format(self):
        return CNPJ().mask(self._cnpj)
