# 🤖 Robô Coletor de Lixo - Inteligência Artificial

Projeto desenvolvido para a disciplina de **Inteligência Artificial** da **Universidade Federal do Maranhão (UFMA)**, ministrada pelo professor **Me. Nerval de Jesus Santos Júnior**.

O projeto consiste na implementação de um **agente inteligente coletor de lixo** em um ambiente simulado de uma matriz **20×20**, utilizando diferentes arquiteturas de agentes para realizar a coleta e transporte dos resíduos até uma lixeira.

O objetivo é analisar e comparar o desempenho de diferentes estratégias de Inteligência Artificial considerando critérios como **pontuação obtida, quantidade de passos executados e tempo de execução**.

---

## 📌 Objetivo do Projeto

Desenvolver um robô capaz de:

- Explorar um ambiente representado por uma matriz 20×20;
- Coletar resíduos orgânicos e recicláveis;
- Transportar os resíduos até a posição da lixeira;
- Utilizar diferentes arquiteturas de agentes inteligentes;
- Comparar o desempenho das estratégias implementadas.

---

## 🌎 Características do Ambiente

O ambiente simulado possui:

- Matriz: **20×20 posições**
- Posição inicial do robô: **(1,1)**
- Localização da lixeira: **(20,20)**

Tipos de resíduos:

| Tipo de lixo | Quantidade | Pontuação |
|---|---|---|
| Orgânico | 10 unidades | +1 ponto |
| Reciclável | 5 unidades | +5 pontos |

O robô pode carregar apenas um lixo por vez e deve buscar maximizar sua pontuação reduzindo o número de movimentos.

---

# 🧠 Arquiteturas de Agentes Implementadas

## 1. Agente Reativo Simples

Baseado em regras de condição e ação.

O agente toma decisões utilizando apenas a percepção atual do ambiente, sem possuir memória do estado anterior.

Exemplo:
- Encontrou lixo → coleta;
- Está carregando lixo → leva até a lixeira.

---

## 2. Agente Baseado em Modelos

Possui um estado interno para armazenar informações do ambiente.

Utiliza memória para evitar decisões repetidas e melhorar a exploração da matriz.

---

## 3. Agente Baseado em Objetivos (BDI)

Utiliza o modelo:

- **Beliefs (Crenças):** informações conhecidas sobre o ambiente;
- **Desires (Desejos):** objetivos que deseja alcançar;
- **Intentions (Intenções):** planos escolhidos para atingir os objetivos.

O agente busca priorizar resíduos recicláveis e reduzir custos de deslocamento.

---

## 4. Agente Baseado em Utilidade

Realiza escolhas considerando o custo-benefício das ações.

A decisão leva em conta:

- Valor do lixo;
- Distância até o lixo;
- Distância até a lixeira.

O objetivo é encontrar a ação com maior utilidade.

---

# 📂 Estrutura do Projeto
ProjetoIA
│
├── agentes.py # Implementação das arquiteturas dos agentes
├── ambiente.py # Criação e gerenciamento do ambiente 20×20
├── main.py # Execução da simulação e comparação
├── resultados.txt # Resultados obtidos nos testes
└── README.md # Documentação do projeto

---

# 💻 Tecnologias Utilizadas

- Python 3
- Visual Studio Code
- Git/GitHub

---

# ▶️ Como Executar

Clone o repositório:

```bash
git clone https://github.com/lucasmatosdasilva/robo-coletor-lixo.git

Entre na pasta:

cd robo-coletor-lixo

Execute o programa:

python main.py
