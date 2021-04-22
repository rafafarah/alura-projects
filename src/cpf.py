class Cpf:
    def __init__(self, cpf):
        cpf = str(cpf)
        if self.isvalid(cpf):
            self._cpf = cpf
        else:
            raise ValueError("Invalid CPF")

    def __str__(self):
        return self.format()

    def isvalid(self, doc):
        return 11 == len(doc)

    def format(self):
        return "{}.{}.{}-{}".format(
            self._cpf[:3],
            self._cpf[3:6],
            self._cpf[6:9],
            self._cpf[9:])
