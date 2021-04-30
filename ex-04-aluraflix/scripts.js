var listaFilmes = []


function adicionarFilme() {
  var campoFilme = document.querySelector('#filme')
  if (campoFilme.value.endsWith(".jpg")) {
    // buscar filme em listaFilme e add e printar caso não tiver sido adicionado antes
    listarFilmesNaTela(campoFilme.value)
  } else {
    // alert("Not a image")
  }

  campoFilme.value = ""
}

function listarFilmesNaTela(filme) {
  var listaFilmes = document.querySelector('#listaFilmes')
  var elementoFilme = "<img src=" + filme + ">"
  listaFilmes.innerHTML += elementoFilme
}

/* Challenge */
/*Paulo: Add movie name or link below image
Rafa: Ask the movies to display
Gui: Don't show move twice*/

/* Challenge */
/*Paulo: Add trailer embedded; understand document.querySelector
Rafa: Understand innerHTML
Gui: Move image validation to function*/