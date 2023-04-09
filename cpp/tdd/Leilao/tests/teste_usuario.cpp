#include "catch.hpp"
#include "Usuario.hpp"

TEST_CASE("Usuário deve saber informar seu primeiro nome") {
    // Arrange
    Usuario usuario(GENERATE("Jorge", "Jorge Jefferson"));

    // Act
    std::string primeiroNome = usuario.recuperaPrimeiroNome();

    // Assert
    REQUIRE("Jorge" == primeiroNome);
}
