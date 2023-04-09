#include <iostream>
#include <string>
#include <memory>
#include <cstring>
#include "Usuario.hpp"

// void* operator new(size_t bytes)
// {
//     std::cout << "Alocando " << bytes << " bytes" << std::endl;
//     return malloc(bytes);
// }

void exibeNome(std::string_view nome)
{
    std::cout << nome << std::endl;
}

void exibeNomeUsuario(std::shared_ptr<Usuario> usuario)
{
    std::cout << usuario->recuperaNome() << std::endl;
}

int main_test_string_manipulation_and_smart_pointer() {
    std::cout << "--------------------------" << std::endl;
    // Small String Optimization(SSO) - alloc memory on stack instead of heap
    std::string nomeCasal = "Jorge Jefferson Jefferson & Jorgita Jeniffer Jeniffer";
    // Operates a string without using any additional memory
    std::string_view nomeDele(nomeCasal.c_str(), nomeCasal.find('&') - 1);
    std::string_view nomeDela(nomeCasal.c_str() + nomeCasal.find('&') + 2);

    exibeNome(nomeDele);
    exibeNome(nomeDela);
    exibeNome("string literal alocada na stack");
    std::cout << "--------------------------" << std::endl;

    Usuario* usuario = new Usuario("Jorge Jefferson");
    std::cout << usuario->recuperaNome() << std::endl;
    delete usuario;
    std::cout << "--------------------------" << std::endl;

    std::unique_ptr<Usuario> usuaria = std::make_unique<Usuario>(Usuario("Jorgita Jeniffer"));
    std::cout << usuaria->recuperaNome() << std::endl;
    std::cout << "--------------------------" << std::endl;

    std::shared_ptr<Usuario> usuarita = std::make_shared<Usuario>("Jorgita Jeniffer");
    exibeNomeUsuario(usuarita);

    return 0;
}

class String
{
private:
    char* data;
    size_t size;
public:
    String(const char* string)
    {
        std::cout << "String criada" << std::endl;
        size =  strlen(string);
        data = new char[size];
        memcpy(data, string, size);
    }

    String(const String& string)
    {
        std::cout << "String copiada" << std::endl;
        size =  strlen(string.data);
        data = new char[size];
        data[size] = 0;
        memcpy(data, string.data, size);
    }

    String(String&& string)
    {
        // copy size and move data from temporary string
        std::cout << "String movida" << std::endl;
        size = string.size;
        data = string.data;

        // make temporary string invalid so it won't call delete
        string.size = 0;
        string.data = nullptr;
    }

    ~String()
    {
        delete data;
    }
};

class User
{
private:
    String nome;
public:
    User(const String& string) : nome(string)
    {
    }

    // move string to name
    // equivalent to cast it to rvalue: nome((String&&) string)
    User(String&& string) : nome(std::move(string))
    {
    }
};

int main_test_move_semantics() {
    User(String("Jorge Jefferson"));
    return 0;
}