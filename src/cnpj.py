from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, cnpj):
        cnpj = str(cnpj)
        if self.isvalid(cnpj):
            self._cnpj = cnpj
        else:
            raise ValueError("Invalid CNPJ")

    def __str__(self):
        return self.format()

    def isvalid(self, cnpj):
        return 14 == len(cnpj) and CNPJ().validate(cnpj)

    def format(self):
        return CNPJ().mask(self._cnpj)
