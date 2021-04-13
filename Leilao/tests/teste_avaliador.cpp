#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "Avaliador.hpp"
#include <iostream>

Leilao emOrdemCrescente()
{
    Lance primeiroLance(Usuario("Jorge"), 1000);
    Lance segundoLance(Usuario("Jorgita"), 2000);
    Leilao leilao("Fiat 147 0Km");
    leilao.recebeLance(primeiroLance);
    leilao.recebeLance(segundoLance);

    return leilao;
}

Leilao emOrdemDecrescente()
{
    Lance primeiroLance(Usuario("Jorge"), 2000);
    Lance segundoLance(Usuario("Jorgita"), 1000);
    Leilao leilao("Fiat 147 0Km");
    leilao.recebeLance(primeiroLance);
    leilao.recebeLance(segundoLance);

    return leilao;
}

TEST_CASE("Avaliador") {
    // Arrange: preparando ambiente
    Avaliador avaliador;

    SECTION("Leilões ordenados") {
        Leilao leilao = GENERATE(emOrdemCrescente(), emOrdemDecrescente());

        SECTION("Recuperar maior lance de leilão") {
            // Act: executando o código a ser testado
            avaliador.avalia(leilao);

            // Assert: verificando a saída esperada
            REQUIRE(2000 == avaliador.recuperaMaiorValor());
        }

        SECTION("Recuperar menor lance de leilão") {
            // Act: executando o código a ser testado
            avaliador.avalia(leilao);

            // Assert: verificando a saída esperada
            REQUIRE(1000 == avaliador.recuperaMenorValor());
        }
    }

    SECTION("Recuperar 3 maiores lances") {
        // Arrange: preparando ambiente
        Lance primeiroLance(Usuario("Jorge"), 1000);
        Lance segundoLance(Usuario("Jorgita"), 2000);
        Lance terceiroLance(Usuario("Jefferson"), 1500);
        Lance quartoLance(Usuario("Jenifer"), 2500);

        Leilao leilao("Fiat 147 0Km");
        leilao.recebeLance(primeiroLance);
        leilao.recebeLance(segundoLance);
        leilao.recebeLance(terceiroLance);
        leilao.recebeLance(quartoLance);

        // Act: executando o código a ser testado
        leiloeiro.avalia(leilao);

        // Assert: verificando a saída esperada
        auto maiores3Lances = leiloeiro.recupera3MaioresLances();
        REQUIRE(3 == maiores3Lances.size());
        REQUIRE(2500 == maiores3Lances[0].recuperaValor());
        REQUIRE(2000 == maiores3Lances[1].recuperaValor());
        REQUIRE(1500 == maiores3Lances[2].recuperaValor());
    }
}

TEST_CASE("Leilão não deve receber lances consecutivos do mesmo usuário") {
    // Arrange
    Leilao leilao("Fiat 147 0Km");
    Usuario usuario("Jorge");

    Lance primeiroLance(usuario, 1000);
    Lance segundoLance(usuario, 1500);

    // Act
    leilao.recebeLance(primeiroLance);
    leilao.recebeLance(segundoLance);

    // Assert
    REQUIRE(1 == leilao.recuperaLances().size());
    REQUIRE(1000 == leilao.recuperaLances()[0].recuperaValor());
}

TEST_CASE("Usuário deve saber informar seu primeiro nome") {
    // Arrange
    Usuario usuario(GENERATE("Jorge", "Jorge Jefferson"));

    // Act
    std::string primeiroNome = usuario.recuperaPrimeiroNome();

    // Assert
    REQUIRE("Jorge" == primeiroNome);
}
