#o que faz?
#Programa que cria uma lista com o nome dos personagens
#sorteia 3 nomes e mostra para o usuario

#porque?
#A ideia é jogar com grupos com composições diferentes sem se prender alguma estragia especifica
#Assim o usuário pode jogar com todos os persoangens se ele quiser sem usar mods

#ideias para o futuro
#colocar uma interface grafica com o botão de sortear, adcionar o remover personagens
#mostrar a imagens dos personagens no lugar do nome
#quem sabe isso vire um mod que faz isso dentro do jogo

import random

nomes = ["Lae'Zel","Umbralma", "Astarion","Gale","Wyll", "Karlach", "Halsin","minthara", "jaheira", "minsc"]
historico = []

def Sort_party():
    party = random.sample(nomes, 3)
    print(f"O grupo escolhido foi: {', '.join(party)}")

Sort_party()