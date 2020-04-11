import random

undseis = random.randrange (1, 7)

class arma():
    def __init__ (self, n, afue, ades, aagi, adañ):
        self.nombre = n
        self.fuerza = afue
        self.destreza = ades
        self.agilidad = aagi
        self.daño = adañ

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
