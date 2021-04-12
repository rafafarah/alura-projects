#ifndef Avaliador_hpp
#define Avaliador_hpp
#include "Leilao.hpp"

class Avaliador
{
private:
    float maiorValor = INT32_MIN;
    float menorValor = INT32_MAX;
public:
    void avalia(Leilao);
    float recuperaMaiorValor() const;
    float recuperaMenorValor() const;
};

#endif /* Avaliador_hpp */