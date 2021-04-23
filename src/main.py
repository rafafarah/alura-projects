from cpf import Cpf
from cnpj import Cnpj

def test_cpf():
    cpf_doc = 52998224725
    cpf = Cpf(cpf_doc)
    print(cpf)

def test_cnpj():
    cnpj_doc = 35379838000112
    cnpj = Cnpj(cnpj_doc)
    print(cnpj)

if __name__ == "__main__":
    test_doc_factory()