from objects import personaje
from objects import enemigo
from tuplas import listaArmas

pj = personaje(1, 10, 3, 3, 3)
araña = enemigo(5, 1, 2, 1, 6)
trasgo = enemigo(2, 1, 3, 2, 5)
salamandra = enemigo(5, 1, 3, 2, 5)
goblin = enemigo(2, 1, 2, 3, 5)

iniciarPartida = True

while iniciarPartida:
    print("Bienvenido a Land of RPG: ¿Quieres iniciar una nueva partida? (y/n)")
    iP = input(">")
    if iP == "y":
        print("¿Cómo te llamas?")
        name = input(">")
        name = name.title()
        pj = personaje(1, 10, 3, 3, 3)
        print("Bienvenido " + name + " estas son tus estadisticas: ")
        print("Nivel: " + str(pj.nivel) + ". Vida: " + str(pj.vida) + ". Fuerza: " + str(pj.fuerza) + ". Destreza: " + str(pj.destreza) + ". Agilidad: " + str(pj.agilidad) + ".")


    while not pj.armaEquipada:
        print("Elije un arma: Espada, Espada ropera, Gladio, Florete.")
        armavar = input(">")
        armavar = armavar.lower()

#Falta esto :p
        for i in listaArmas:
            if armavar == i.nombre:
                pj.equiparArma(i)

       
        # print("Has elegido: " + str(armavar) + ". " + "Tus estadisticas son: Fuerza: " + str(pj.fuerza) + ". Destreza: " + str(pj.destreza) + ". Agilidad: " + str(pj.agilidad) + ".")
        # print("¿Estas seguro? (y/n)")
        # eleccionarma = input(">")
        # eleccionarma = eleccionarma.lower()
        # if eleccionarma == "n":
        #     if armavar == "espada":
        #         pj.desequiparArma(espada)
        #     elif armavar == "espada ropera":
        #         pj.desequiparArma(espadaRopera)
        #     elif armavar == "gladio":
        #         pj.desequiparArma(gladio)
        #     elif armavar == "florete":
        #         pj.desequiparArma(florete)


    else:
        iniciarPartida = False