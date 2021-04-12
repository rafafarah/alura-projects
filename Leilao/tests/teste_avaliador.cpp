#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "Avaliador.hpp"
#include <iostream>

TEST_CASE("Recuperar maior lance de leilão em ordem crescente") {
    // Arrange: preparando ambiente
    Lance primeiroLance(Usuario("Jorge"), 1000);
    Lance segundoLance(Usuario("Jorgita"), 2000);
    Leilao leilao("Fiat 147 0Km");
    leilao.recebeLance(primeiroLance);
    leilao.recebeLance(segundoLance);
    Avaliador leiloeiro;

    // Act: executando o código a ser testado
    leiloeiro.avalia(leilao);

    // Assert: verificando a saída esperada
    REQUIRE(2000 == leiloeiro.recuperaMaiorValor());
}

TEST_CASE("Recuperar maior lance de leilão em ordem decrescente") {
    // Arrange: preparando ambiente
    Lance primeiroLance(Usuario("Jorge"), 2000);
    Lance segundoLance(Usuario("Jorgita"), 1000);
    Leilao leilao("Fiat 147 0Km");
    leilao.recebeLance(primeiroLance);
    leilao.recebeLance(segundoLance);
    Avaliador leiloeiro;

    // Act: executando o código a ser testado
    leiloeiro.avalia(leilao);

    // Assert: verificando a saída esperada
    REQUIRE(2000 == leiloeiro.recuperaMaiorValor());
}

TEST_CASE("Recuperar menor lance de leilão em ordem crescente") {
    // Arrange: preparando ambiente
    Lance primeiroLance(Usuario("Jorge"), 1000);
    Lance segundoLance(Usuario("Jorgita"), 2000);
    Leilao leilao("Fiat 147 0Km");
    leilao.recebeLance(primeiroLance);
    leilao.recebeLance(segundoLance);
    Avaliador leiloeiro;

    // Act: executando o código a ser testado
    leiloeiro.avalia(leilao);

    // Assert: verificando a saída esperada
    REQUIRE(1000 == leiloeiro.recuperaMenorValor());
}

TEST_CASE("Recuperar menor lance de leilão em ordem decrescente") {
    // Arrange: preparando ambiente
    Lance primeiroLance(Usuario("Jorge"), 2000);
    Lance segundoLance(Usuario("Jorgita"), 1000);
    Leilao leilao("Fiat 147 0Km");
    leilao.recebeLance(primeiroLance);
    leilao.recebeLance(segundoLance);
    Avaliador leiloeiro;

    // Act: executando o código a ser testado
    leiloeiro.avalia(leilao);

    // Assert: verificando a saída esperada
    REQUIRE(1000 == leiloeiro.recuperaMenorValor());
}

TEST_CASE("Recuperar 3 maiores lances") {
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
    Avaliador leiloeiro;

    // Act: executando o código a ser testado
    leiloeiro.avalia(leilao);

    // Assert: verificando a saída esperada
    auto maiores3Lances = leiloeiro.recupera3MaioresLances();
    REQUIRE(3 == maiores3Lances.size());
    REQUIRE(2500 == maiores3Lances[0].recuperaValor());
    REQUIRE(2000 == maiores3Lances[1].recuperaValor());
    REQUIRE(1500 == maiores3Lances[2].recuperaValor());
}
