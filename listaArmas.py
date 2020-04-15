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