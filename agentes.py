import math


class Agente:

    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.posicao = ambiente.robo
        self.carga = None
        self.pontos = 0
        self.passos = 0


    def mover(self, destino):

        x,y = self.posicao
        nx,ny = destino

        while x != nx:
            x += 1 if nx > x else -1
            self.passos += 1

        while y != ny:
            y += 1 if ny > y else -1
            self.passos += 1

        self.posicao = destino



# 1 - Reativo simples
class ReativoSimples(Agente):

    def executar(self):

        for lixo in list(self.ambiente.lixos):

            self.mover(lixo)

            tipo = self.ambiente.pegar_lixo(lixo)

            if tipo:
                self.carga = tipo

            self.mover(self.ambiente.lixeira)

            if self.carga:
                self.pontos += 1 if self.carga=="organico" else 5
                self.carga=None



# 2 - Baseado em modelo
class Modelo(Agente):

    def executar(self):

        visitados=[]

        for lixo in list(self.ambiente.lixos):

            if lixo not in visitados:

                visitados.append(lixo)

                self.mover(lixo)

                tipo=self.ambiente.pegar_lixo(lixo)

                self.mover(self.ambiente.lixeira)

                if tipo:
                    self.pontos += 1 if tipo=="organico" else 5




# 3 - BDI / Objetivos
class BDI(Agente):

    def executar(self):

        while self.ambiente.lixos:

            reciclaveis=[
                p for p,t in self.ambiente.lixos.items()
                if t=="reciclavel"
            ]

            alvo = reciclaveis[0] if reciclaveis else list(self.ambiente.lixos)[0]

            self.mover(alvo)

            tipo=self.ambiente.pegar_lixo(alvo)

            self.mover(self.ambiente.lixeira)

            self.pontos += 5 if tipo=="reciclavel" else 1



# 4 - Utilidade
class Utilidade(Agente):

    def executar(self):

        while self.ambiente.lixos:

            melhor=None
            maior=-999


            for pos,tipo in self.ambiente.lixos.items():

                valor=5 if tipo=="reciclavel" else 1

                distancia=abs(self.posicao[0]-pos[0])+abs(self.posicao[1]-pos[1])

                utilidade=valor-distancia*0.1


                if utilidade>maior:
                    maior=utilidade
                    melhor=pos


            self.mover(melhor)

            tipo=self.ambiente.pegar_lixo(melhor)

            self.mover(self.ambiente.lixeira)

            self.pontos += 5 if tipo=="reciclavel" else 1