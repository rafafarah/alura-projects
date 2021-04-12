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
