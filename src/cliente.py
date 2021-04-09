from pprint import pprint

class Client:
    def __init__(self, name, cpf, occupation):
        self.name = name
        self.cpf = cpf
        self.occupation = occupation

client = Client('jhon doe', '123.456.789-00', 'dev')

# print attribute as dictionary
# print(client.__dict__)
pprint(client.__dict__, width=40)
