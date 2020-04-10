import random
undseis = random.randrange (1, 7)

class arma():
    def __init__ (self, n, afue, ades, aagi, adañ):
        self.nombre = n
        self.fuerza = afue
        self.destreza = ades
        self.agilidad = aagi
        self.daño = adañ

espada = arma("espada", 0, 1, 0, 1)
espadaRopera = arma("espada ropera",-1, 2, 0, 1)
gladio = arma("gladio", 0, 2, -1, 1)
florete = arma("florete", -2, 3, 0, 1)
listaArmas = (espada, espadaRopera, gladio, florete)


class personaje():
    def __init__ (self, pniv, pvid, pfue, pdes, pagi):
        self.nivel = pniv
        self.vida = pvid
        self.fuerza = pfue
        self.destreza = pdes
        self.agilidad = pagi
        self.armaEquipada = False

    def recibirDaño (self, pfue, pdes, pagi, efue, edes, eagi, pvid, edañ):
        ataque = undseis
        defensa = undseis
        if ataque > defensa:
            self.vida = pvid - edañ        
        if (pfue < efue) or (pdes < edes) or (pagi < eagi):
            ataque = undseis + 1
            defensa = undseis
            if ataque > defensa:
                self.vida = pvid - edañ
        elif (pfue < efue) and (pdes < edes) or (pagi < eagi) and (pdes < edes) or (pfue < efue) and (pagi < eagi):
            ataque = undseis + 2
            defensa = undseis
            if ataque > defensa:
                self.vida = pvid - edañ
        elif (pfue < efue) and (pdes < edes) and (pagi < eagi):
            ataque = undseis + 3
            defensa = undseis
            if ataque > defensa:
                self.vida = pvid - edañ
 
    def equiparArma (self, arma):
        self.armaEquipada = True
        self.fuerza = self.fuerza + arma.fuerza
        self.destreza = self.destreza + arma.destreza
        self.agilidad = self.agilidad + arma.agilidad
    
    def desequiparArma (self, arma):
        self.armaEquipada = False
        self.fuerza = self.fuerza - arma.fuerza
        self.destreza = self.destreza - arma.destreza
        self.agilidad = self.agilidad - arma.agilidad

pj = personaje(1, 10, 3, 3, 3)

class enemigo():
    def __init__ (self, evid, edañ, efue, edes, eagi):
        self.vida = evid
        self.daño = edañ
        self.fuerza = efue
        self.destreza = edes
        self.agilidad = eagi

    def atacar (self, pfue, pdes, pagi, efue, edes, eagi, evid, adañ):
        ataque = undseis
        defensa = undseis
        if ataque > defensa:
            self.vida = evid - adañ        
        if (pfue > efue) or (pdes > edes) or (pagi > eagi):
            ataque = undseis + 1
            defensa = undseis
            if ataque > defensa:
                self.vida = evid - adañ
        elif (pfue > efue) and (pdes > edes) or (pagi > eagi) and (pdes > edes) or (pfue > efue) and (pagi > eagi):
            ataque = undseis + 2
            defensa = undseis
            if ataque > defensa:
                self.vida = evid - adañ
        elif (pfue > efue) and (pdes > edes) and (pagi > eagi):
            ataque = undseis + 3
            defensa = undseis
            if ataque > defensa:
                self.vida = evid - adañ

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