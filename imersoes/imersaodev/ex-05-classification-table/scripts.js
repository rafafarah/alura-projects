var paulo = {
  name: "Paulo",
  wins: 2,
  draws: 5,
  losses: 1,
  points: 0
}
var rafa = {
  name: "Rafa",
  wins: 3,
  draws: 5,
  losses: 2,
  points: 0
}
var players = [paulo, rafa]

for (var i = 0; i < players.length; i++) {
  players[i].points = calculaPontos(players[i])
}
exibirJogadoresNaTela(players)

function calculaPontos(player) {
  var points = (player.wins * 3) + player.draws
  return points
}

function exibirJogadoresNaTela(players) {
  var html = ""

  for(var i = 0; i < players.length; i++) {
    html += "<tr><td>" + players[i].name + "</td>"
    html += "<td>" + players[i].wins + "</td>"
    html += "<td>" + players[i].draws + "</td>"
    html += "<td>" + players[i].losses + "</td>"
    html += "<td>" + players[i].points + "</td>"
    html += "<td><button onClick='adicionarVitoria(" + i + ")'>Vitória</button></td>"
    html += "<td><button onClick='adicionarEmpate(" + i + ")'>Empate</button></td>"
    html += "<td><button onClick='adicionarDerrota(" + i + ")'>Derrota</button></td></tr>"
  }

  var playersTable = document.getElementById("tabelaJogadores")
  console.log(playersTable)
  playersTable.innerHTML = html
}

function adicionarVitoria(i) {
  var player = players[i]
  player.wins++
  player.points = calculaPontos(player)
  exibirJogadoresNaTela(players)
}

function adicionarEmpate(i) {
  var player = players[i]
  player.draws++
  player.points = calculaPontos(player)
  exibirJogadoresNaTela(players)
}

function adicionarDerrota(i) {
  var player = players[i]
  player.losses++
  exibirJogadoresNaTela(players)
}

/* Challenge */
/*Paulo: Refactor to keep data consistency
Rafa: Only one button for draws update both columns*/