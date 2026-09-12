import random
import copy


class Ambiente:

    def __init__(self, lixos=None):

        self.tamanho = 20

        # Robô começa em (1,1) -> índice Python (0,0)
        self.robo = (0,0)

        # Lixeira (20,20) -> índice Python (19,19)
        self.lixeira = (19,19)

        if lixos:
            self.lixos = copy.deepcopy(lixos)

        else:
            self.lixos = {}

            # 10 lixos orgânicos
            while len(self.lixos) < 10:
                pos = (
                    random.randint(0,19),
                    random.randint(0,19)
                )

                if pos not in self.lixos and pos not in [self.robo,self.lixeira]:
                    self.lixos[pos] = "organico"


            # 5 recicláveis
            while len(self.lixos) < 15:
                pos = (
                    random.randint(0,19),
                    random.randint(0,19)
                )

                if pos not in self.lixos and pos not in [self.robo,self.lixeira]:
                    self.lixos[pos] = "reciclavel"



    def pegar_lixo(self,posicao):

        if posicao in self.lixos:
            return self.lixos.pop(posicao)

        return None



    def copiar(self):

        return Ambiente(self.lixos)