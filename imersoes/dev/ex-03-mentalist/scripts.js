var numeroSecreto = parseInt(Math.random() * 10)
var tentativas = 3

while (tentativas > 0) {
  tentativas--
  
  var chute = parseInt(prompt("Digite um número entre 0 e 10"))

  if (numeroSecreto == chute) {
    alert("Acertô miseravi!")
    break
  } else if (chute > numeroSecreto && tentativas) {
    alert("O número secreto é menor")
  } else if (chute < numeroSecreto && tentativas) {
    alert("O número secreto é maior")
  }
}

if (numeroSecreto != chute) {
  alert("Errrrrou. O número secreto era " + numeroSecreto)
}

/* Challenge */
/*Paulo: Add score and tries remainings on html
Rafa: Remove break and use and alternative
Gui: Generate other ranges for secret number*/