#include "Avaliador.hpp"
#include "Usuario.hpp"
#include "Lance.hpp"
#include "Leilao.hpp"
#include <iostream>

int main () {
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
    float valorEsperado = 2000;
    if (valorEsperado == leiloeiro.recuperaMaiorValor()) {
        std::cout << "TESTE OK" << std::endl;
    } else {
        std::cout << "TESTE FALHOU" << std::endl;
    }

    return 0;
}