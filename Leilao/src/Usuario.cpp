#include "Usuario.hpp"

Usuario::Usuario(std::string nome): nome(nome)
{
}

std::string Usuario::recuperaNome() const
{
    return nome;
}

std::string Usuario::recuperaPrimeiroNome() const
{
    return nome.find(' ') != -1 ? nome.substr(0, nome.find(' ')) : nome;
}