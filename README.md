# 🎮 Escrevendo as Classes de um Jogo

Este projeto consiste em uma aplicação Python que utiliza **Programação Orientada a Objetos (POO)** para simular os ataques de diferentes classes de heróis em um jogo de aventura.

## 📝 O Desafio

O objetivo era criar uma classe genérica para representar um herói com propriedades específicas (nome, idade, tipo) e um método de ataque que variasse conforme a classe escolhida.

### Tabela de Ataques:

| Tipo | Ataque |
| :--- | :--- |
| Mago | Magia |
| Guerreiro | Espada |
| Monge | Artes Marciais |
| Ninja/Arqueiro | Shuriken |

> **Saída esperada:** "O tipo **{tipo}** atacou usando **{ataque}**".

---

## 🚀 Tecnologias e Conceitos Utilizados

Nesta solução, foram aplicados conceitos avançados de estruturação de código:

* **Classes e Objetos:** Criação da classe `Jogo` para encapsular os dados do herói.
* **Métodos:** Implementação da função `tipo_ataque` dentro da classe para processar a lógica de combate.
* **Estrutura de Decisão Moderna (`match/case`):** Utilizada para selecionar o tipo de ataque de forma limpa e legível.
* **Encapsulamento Simples:** Uso do `self` para acessar as propriedades do objeto instanciado.
* **Interatividade:** Laço `while` para permitir múltiplos ataques com diferentes tipos de heróis na mesma sessão.

---

## 🛠️ Como Funciona o Código

1.  **Instanciação:** O programa recebe o nome e a idade do jogador.
2.  **Criação do Herói:** A cada rodada, um novo objeto da classe `Jogo` é criado com o tipo escolhido (mago, guerreiro, etc).
3.  **Lógica de Combate:** O método `tipo_ataque()` verifica o tipo do herói e retorna a arma ou habilidade correspondente.
4.  **Tratamento de Exceções:** Caso o usuário digite um tipo desconhecido, o código utiliza o wildcard (`_`) para retornar um "ataque misterioso".
5.  **Loop de Repetição:** O jogador pode testar novos tipos de heróis até que digite "não" para encerrar.

---

## 🏃 Como executar

1. Certifique-se de ter o **Python 3.10** ou superior instalado (necessário para o `match/case`).
2. Salve o código em um arquivo chamado `desafio3_r.py`.
3. No terminal, execute:
   ```bash
   python desafio3_r.py
