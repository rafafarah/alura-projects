#include "Leilao.hpp"

Leilao::Leilao(std::string descricao): descricao(descricao)
{
    
}

const std::vector<Lance>& Leilao::recuperaLances() const
{
    return lances;
}

bool Leilao::usuarioAtualIgualUltimoUsuario(Lance lance) const
{
    if(lances.size() > 0 && lances.back().recuperaNomeUsuario() == lance.recuperaNomeUsuario()) {
        return true;
    }

    return false;
}

void Leilao::recebeLance(const Lance& lance)
{
    // ignore consecutive bets by the same user
    if(usuarioAtualIgualUltimoUsuario(lance)) {
        return;
    }

    lances.push_back(lance);
}
