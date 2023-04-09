def test_extend_list():
    user_data_science = [15, 23, 43, 56]
    user_machine_learning = [13, 23, 56, 42]

    watched = []
    watched = user_data_science.copy()
    watched.extend(user_machine_learning)
    # final list has duplicated elements
    print(watched)

def test_set():
    user_data_science = {15, 23, 43, 56}
    user_machine_learning = {13, 23, 56, 42}
    # a set has no duplicated element
    # set has no index access/no order
    watched_union = user_machine_learning | user_data_science
    watched_intesec = user_machine_learning & user_data_science
    watched_diff = user_machine_learning - user_data_science
    watched_exclusive = user_machine_learning ^ user_data_science
    print(watched_exclusive)
    for user in watched_exclusive:
        print(user)

def test_modifying_set():
    user = {1, 5, 76, 34, 52, 13, 17}
    print(len(user))
    user.add(765)
    print(len(user))

    # frozenset is a not mutable set
    frozen = frozenset(user)
    print(frozen)

def test_dictionary():
    # creating dictionary from constructor, not usual
    # dic = dict(jorge = 1, doge = 2, name = 2, come = 1,)
    dic = {
        "jorge" : 1,
        "doge" : 2,
        "name" : 2,
        "come" : 1,
    }

    # adding to dic
    dic["jefferson"] = 1
    print(dic)
    # removing from dic
    del dic["jefferson"]
    print(dic)

    print(dic["doge"])
    # set allows to define a default value if key isn't present
    print(dic.get("asfd", 0))

def test_iterate_dict():
    dic = {
        "jorge" : 1,
        "doge" : 2,
        "name" : 2,
        "come" : 1,
    }
    # print dict keys
    for elem in dic:
        print(elem)
    print()
    # print dict values
    for elem in dic.values():
        print(elem)
    print()
    # print dict couple
    for elem in dic.items():
        print(elem)
    print()
    # print dict couple anpacked
    for key, value in dic.items():
        print(key, ":", value)

def test_defaultdict():
    text = "Welcome my name is Jorge I like names vey much and I have a dog and I like dog very much"
    text = text.lower()

    # building a dictionary from text
    dic = {}
    for word in text.split():
        dic[word] = dic.get(word, 0) + 1
    print(dic)
    print()
    from collections import defaultdict
    # use defaultdict with int to return 0 as default value
    dic_default = defaultdict(int)
    for word in text.split():
        dic_default[word] += 1
    print(dic_default)

def test_counter_dict():
    from collections import Counter
    text = "Welcome my name is Jorge I like names vey much and I have a dog and I like dog very much"
    text = text.lower()

    # use Counter direct with iterable
    dic_default = Counter(text.split())
    print(dic_default)

def test_collections():
    from collections import Counter
    text_flutter = """
Antes de entrarmos no tópico sobre o Nuvigator propriamente dito, precisamos entender o que temos disponível hoje nativamente no Flutter e como é criado para posteriormente notarmos quais são as diferenças expressivas de um para o outro. Normalmente, tendemos a utilizar rotas como os sites utilizam, já que é um padrão difundido há vários anos na web, mas, diferente dos sites que os usuários têm acesso à URL, em Flutter utilizamos este artifício “por baixo dos panos”.
Independentemente do que utilizamos para navegar, é importante entender que os usuários esperam conseguir ir de uma tela para a outra e voltar. Algumas vezes, precisaremos passar informações de uma tela para a tela seguinte que será aberta (como os detalhes de um produto, por exemplo) ou mesmo passar dados de uma segunda tela para a anterior. Esse fluxo de “vai e vem” dos dados precisa ser tratado com bastante cuidado por nós programadores e programadoras.
A documentação do Flutter traz algumas formas de criar a navegação, sendo elas:
Cada uma dessas formas de navegação tem suas particularidades, diferenças, vantagens e desvantagens. Basicamente, o que precisamos entender agora é que cada uma dessas implementações é uma forma de empilhar, substituir e remover telas abertas ao longo da navegação realizada pelos usuários.
Push e Pop
O mecanismo de pilha, ou seja, o primeiro que é aberto é o último a ser fechado, é amplamente utilizado e difundido no universo Flutter. Além de ser a forma mais simples de navegar entre telas, segundo os próprios criadores do framework, os comandos push e pop são utilizados amplamente para realizar estas ações. Podemos criar um exemplo básico seguindo a documentação do Flutter. A seguir, veja um exemplo implementado com o mecanismo de rotas em push e pop:
Partindo do exemplo acima, conseguimos criar um botão para avançar uma página e retroceder uma página, de acordo com a necessidade do usuário. Repare que foi necessário o uso do widget MaterialPageRoute para definir como a transição entre as telas acontecerá.
Apesar de bastante simples, esse exemplo tem um problema escondido que logo aparecerá quando o código começar a crescer. E este problema é o acoplamento das duas telas: a tela dois precisa instanciar o widget da tela três. Para isso foi necessário importar o arquivo da tela 3 dentro da tela 2. Repare bem na seguinte linha logo no começo do exemplo:
Outro detalhe importante, que também está diretamente na tela, é que o tipo de rota a ser utilizada foi o MaterialPageRoute. Imagine um cenário em que as transições de tela mudarem para CoupertinoPageRoute? Ou ainda que decidamos mudar todas as rotas presentes no aplicativo de push e pop para rotas nomeadas? E agora, quem poderá nos defender? :fire:
Talvez você esteja pensando agora se é simples de resolver. É só criar um arquivo com várias funções e cada função retorna o widget da nova tela. Desta maneira conseguiríamos definir separadamente as rotas em um arquivo que pode ser importado pelos widgets que querem navegar entre telas. Por exemplo:
    """
    text_etics = """
Na filosofia, a Ética é a ciência que estuda sobre um conjunto de valores morais e normas comportamentais construída por um grupo de pessoas que definem o que é certo e errado. Existem diferentes códigos de ética e eles variam de acordo com cada sociedade, o que é considerado certo para um conjunto de pessoas, pode ser errado para outras.
Se você trabalha com TI, além dos conhecimentos técnicos, é importante agir com honestidade, respeito e dignidade diante seus colegas de trabalho, clientes e conduta ética da empresa, dentre outras condutas.
Você sabe quais são as principais consequências para quem age sem ética no trabalho?
O que podemos considerar um comportamento ético no contexto da tecnologia da informação? É ético utilizar ou cobrar por ferramentas piratas? Acessar dados pessoais que o cliente deixou aberto no computador é uma atitude ética?
Continue lendo este artigo para saber mais sobre o assunto :)
No mercado de trabalho existem os códigos de ética profissional que variam de acordo com cada profissão, eles são definidos através dos comportamentos que são considerados mais adequados e honestos para aquele trabalho.
As empresas também têm os seus códigos de ética e eles são demonstrados através da missão, visão, valores e a cultura cultivada na organização. Profissionais que se preocupam e respeitam a ética profissional da empresa têm maiores chances de obter sucesso no desenvolvimento de sua carreira e na construção de uma boa reputação na empresa.
Recomenda-se que profissionais da área de TI precisam usufruir de suas habilidades com muita responsabilidade, já que a internet é uma rede aberta, ou seja, tenha cuidado ao manusear a informações, conhecendo e respeitando as leis existentes e a privacidade dos usuários.
A ética, como vimos, define o que é certo e errado, porém cabe a cada profissional agir de acordo com a sua conduta ética na hora de trabalhar. Outros comportamentos éticos que um (a) profissional do segmento de TI deve ter em mente é da não utilização de ferramentas ou aplicativos piratas, manipulação de dados e informações e acessar recursos computacionais não autorizados.
    """

    def compute_freq(text):
        dic = Counter(text.lower())
        total = sum(dic.values())
        ratio = Counter(dict((letter, freq/total) for letter, freq in dic.items()))
        common = ratio.most_common(10)
        for letter, freq in common:
            print("{} => {:.2f}%".format(letter, freq*100))

    compute_freq(text_flutter)
    print()
    compute_freq(text_etics)


if __name__ == "__main__":
    test_collections()
