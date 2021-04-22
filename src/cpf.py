from validate_docbr import CPF

class Cpf:
    def __init__(self, cpf):
        cpf = str(cpf)
        if self.isvalid(cpf):
            self._cpf = cpf
        else:
            raise ValueError("Invalid CPF")

    def __str__(self):
        return self.format()

    def isvalid(self, cpf):
        return 11 == len(cpf) and CPF().validate(cpf)

    def format(self):
        return CPF().mask(self._cpf)
