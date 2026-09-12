import time

from ambiente import Ambiente
from agentes import (
    ReativoSimples,
    Modelo,
    BDI,
    Utilidade
)


# Cria UM ÚNICO mapa inicial
ambiente_base = Ambiente()


agentes = [

    ("Reativo Simples", ReativoSimples),

    ("Baseado em Modelo", Modelo),

    ("BDI", BDI),

    ("Utilidade", Utilidade)

]


arquivo = open("resultados.txt","w")


for nome, classe in agentes:


    # Cada agente recebe uma cópia do MESMO ambiente
    ambiente = ambiente_base.copiar()


    robo = classe(ambiente)


    inicio = time.time()


    robo.executar()


    fim = time.time()



    resultado = f"""
=================================

Agente: {nome}

Lixos coletados: 15

Pontuação: {robo.pontos}

Passos executados: {robo.passos}

Tempo de execução: {(fim-inicio)*1000:.4f} ms

=================================

"""


    print(resultado)

    arquivo.write(resultado)



arquivo.close()