from cpf import Cpf
from cnpj import Cnpj
from doc import Doc
from tel import Tel
from date import Date
from cep import Address

def test_cpf():
    cpf_doc = 52998224725
    cpf = Cpf(cpf_doc)
    print(cpf)

def test_cnpj():
    cnpj_doc = 35379838000112
    cnpj = Cnpj(cnpj_doc)
    print(cnpj)

def test_doc_factory():
    cnpj_doc = 35379838000112
    cpf_doc = 52998224725
    doc = Doc.create(cnpj_doc)
    print(doc)

def test_email_pattern():
    import re
    # \d is equivalent to [0-9]
    pattern = "\d[a-z]{2}[0-9]"
    text = "123 1ac2 1cc aa1"
    print(re.search(pattern, text).group())

    # \w include alphanumeric and underscore charactere
    pattern_email = "\w{1,50}@\w{1,10}.\w{2,3}(.\w{2,3})?"
    email = "jorge@bol.com"
    print(re.search(pattern_email, email).group())

def test_telephone_pattern():
    import re

    pattern = "\d{2}\d{4,5}\d{4}"
    tel = "jorge@bol.com cel 01234567890"
    print(re.search(pattern, tel).group())

def test_tel():
    tel_number = 353798346854
    tel = Tel(tel_number)
    print(tel._tel)
    print(tel)

def test_date():
    import time
    date = Date()
    time.sleep(10)
    print(date.get_month())
    print(date.get_weekday())
    print(date)
    print(date.delta())

def test_cep():
    add = Address("01001001")
    bairro, cidade, estado = add.access_via_cep()
    print(add, bairro, cidade, estado)


if __name__ == "__main__":
    test_cep()