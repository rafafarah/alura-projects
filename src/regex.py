import re

email1 = 'My number is 1234-1234'
email2 = 'You can find me on 1234-1234, this is my telephone number'
email3 = '1234-1234 is my cellphone number'
email4 = 'ewqhueyhaxdnbca 995431254 fhdsahf 98761234 ifdskafpohds 9876-1234'

padrao = '[0-9]{4,5}[-]*[0-9]{4}'

retorno = re.search(padrao, email1)
print(retorno.group())

retorno = re.search(padrao, email2)
print(retorno.group())

retorno = re.search(padrao, email3)
print(retorno.group())

retorno = re.findall(padrao, email4)
print(retorno)