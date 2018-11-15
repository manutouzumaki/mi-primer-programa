
pokemon_elegido = input("contra que pokemon quieres combatir? (squirtel / charmander / bulbasaur)")

vida_pikachu = 100
vida_enemigo = 0
ataque_enemigo = 0
nombre_pokemon = pokemon_elegido
#se declaran los pokemon
if pokemon_elegido == "squirtel":
    vida_enemigo = 90
    nombre_pokemon = "squirtel"
    ataque_enemigo = 8

elif pokemon_elegido == "charmander":
    vida_enemigo = 80
    nombre_pokemon = "charmander"
    ataque_enemigo = 7

elif pokemon_elegido == "bulbasaur":
    vida_enemigo = 100
    nombre_pokemon = "bulbasaur"
    ataque_enemigo = 10
#elegimos e ataque
while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("que ataque usaras? chispazo / bola voltio")
    if ataque_elegido == "chispazo":
        vida_enemigo = vida_enemigo - 10
    elif ataque_elegido == "bola voltio":
        vida_enemigo = vida_enemigo - 12
#programamos el ataque del enemigo
    print("la vida de {} ahora es de {}".format(nombre_pokemon , vida_enemigo))

    print("{} te hace un ataque de {} de dano".format(nombre_pokemon , ataque_enemigo))
    vida_pikachu = vida_pikachu - ataque_enemigo

    print("tu vida ahora es de {}".format(vida_pikachu))
#se muestra quien gana
if vida_enemigo <= 0:
    print("has ganado")
if vida_pikachu <= 0:
    print("has perdido")

print("termina cobate")


