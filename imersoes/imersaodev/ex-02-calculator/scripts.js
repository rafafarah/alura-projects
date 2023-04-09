var primeiroValor = parseInt(prompt("Digite o primeiro valor:"))
var segundoValor = parseInt(prompt("Digite o segundo valor:"))
var operacao = prompt("Qual operação?(+,-,*,/)")

var resultado = "err"

switch (operacao) {
  case '+':
    resultado = primeiroValor + segundoValor
    break
  case '-':
    resultado = primeiroValor - segundoValor
    break
  case '*':
    resultado = primeiroValor * segundoValor
    break
  case '/':
    resultado = primeiroValor / segundoValor
    break
}
console.log(resultado)
if (resultado != "err") {
  document.write("<h2>" + primeiroValor + " " + operacao + " " + segundoValor + " = " + resultado + "</h2>")
} else {
  document.write("<h2> Error </h2>")
}



/* Challenges */
/*Rafa: Who's that pokémon
Paulo: Pokémon evolution line from user inital entry
*/