#include <iostream>
#include <string>
#include <memory>
#include "Usuario.hpp"

void* operator new(size_t bytes)
{
    std::cout << "Alocando " << bytes << " bytes" << std::endl;
    return malloc(bytes);
}

void exibeNome(std::string_view nome)
{
    std::cout << nome << std::endl;
}

void exibeNomeUsuario(std::shared_ptr<Usuario> usuario)
{
    std::cout << usuario->recuperaNome() << std::endl;
}

int main() {
    std::cout << "--------------------------" << std::endl;
    // Small String Optimization(SSO) - alloc memory on stack instead of heap
    std::string nomeCasal = "Jorge Jefferson Jefferson & Jorgita Jeniffer Jeniffer";
    // Operates a string without using any additional memory
    std::string_view nomeDele(nomeCasal.c_str(), nomeCasal.find('&') - 1);
    std::string_view nomeDela(nomeCasal.c_str() + nomeCasal.find('&') + 2);

    exibeNome(nomeDele);
    exibeNome(nomeDela);
    exibeNome("string literal alocada na stack");

    return 0;
}
