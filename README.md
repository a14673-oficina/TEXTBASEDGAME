<h1>TextBasedGame<h1>
Portugueses (Português Portugal)

# Floresta Encantada - Capítulo 2 - Brevemente!

Bem-vindo à continuação da tua aventura na Floresta Encantada! 

## **Data de Lançamento:** [2025]

### **Novidades no Capítulo 2**
- **Inventário:** Coleciona itens e usa-os para progredir na aventura.
- **Finais Personalizados:** Finais únicos e engraçados baseados nas tuas escolhas.
- **Código Melhorado:** Estrutura mais modular para facilitar futuras expansões.

### **Como Jogar**
Podes continuar a partir do Capítulo 1 ou iniciar diretamente o Capítulo 2. Faz escolhas sábias para explorar os caminhos mais seguros ou descobre finais inesperados!
  
## **Visão geral do jogo**

A Floresta Encantada é um jogo, onde o jogador explora uma floresta com vários finais diferentes.
O objetivo é encontrar o final que conclui o primeiro capitulo tomando as decisões certas,como tal um dos caminhos o jogador enfrenta uma criatura estranha.
Este jogo oferece uma experiência leve.

**Onde surgiu a ideia para o jogo.**

A ideia para o jogo veio de um colega que sugeriu um enredo com escolhas e finais diferentes.

## **Descrição do Jogo**

**Principais funcionalidades e mecânicas do jogo.**

Escolhas e Caminhos: Decisões que afetam a aventura e levam a diferentes cenários.

Ações de Sobrevivência: Escolhas de lutar, fugir e usar itens ou trágicos.

Finais Variados: Deferentes desfechos com finais, normais ou de morte.

**Estrutura narrativa e a lógica das escolhas.**

O jogo permite que o jogador escolha entre dois caminhos principais: á direita (cabana sombria com uma entidade)
e à esquerda (porta de ferro a ser inspecionada). Cada escolha leva a diferentes ações e desfechos — felizes e trágicos com uma mensagem genérica no caso de perder “game over”. Essa estrutura cria uma aventura com múltiplos finais.

## **Técnicas de Implementação**

## **Estrutura do Código.**

A estrutura do código de Floresta Encantada pode ser organizada em funções para facilitar a leitura e manutenção:
iniciar_jogo(): Apresenta a introdução e pergunta se o jogador deseja começar.
caminho_direita() e caminho_esquerda(): Tratam dos cenários de cada caminho, organizando as escolhas e eventos -específicos.
Funções de Finais: Cada final (feliz, trágico, etc.) é gerido por uma função separada, permitindo uma fácil expansão.

**Controle de Fluxo.**

No jogo o controle de fluxo é gerido principalmente por condições if, elif e else, que permitem ao jogo responder às escolhas do jogador, como iniciar e decidir entre os caminhos.
Ciclos while não são utilizados atualmente, mas poderiam ser implementados no futuro do jogo.

**Gestão de Dados.**

A gestão de dados é feita principalmente com variáveis para armazenar informações essenciais, como o nome do jogador(NomeJ) e suas escolhas exemplo: (direção = ...).  As decisões e o estado do jogo são controlados por essas variáveis.

**Interatividade com o Utilizador.**

A interatividade com o jogador é feita por meio de inputs de texto. o jogo apresenta uma escolha e solicita uma resposta do jogador através da função (input()). por exemplo: para o jogador escolher a direção, o jogador insere uma letra específica (por exemplo, "D" ou "E"), no caso de erro o input é comparado com as opções válidas, exibir uma mensagem de erro.

## **Desafios e Soluções.**

**Desafios encontrados durante o desenvolvimento do código e como os superei.**

Durante o desenvolvimento do jogo, alguns desafios surgiram. Aqui estão dois principais e como foram resolvidos:
Gestão de Escolhas Inválidas: Um dos primeiros problemas foi garantir que o jogador fizesse escolhas válidas (como “D” ou “E” para a direção). inputs inválidos causavam falhas no fluxo do jogo. Para resolver isso, implementamos uma verificação com if e else para validar as entradas e exibir mensagens de erro caso o jogador digitasse algo errado.
Manutenção da Estrutura do Código: À medida que o jogo crescia, o código ficava difícil de ler e atualizar. A solução foi dividir o código em funções para cada segmento do jogo, como iniciar_jogo() e caminho_direita().

## **Conclusão**

No desenvolvimento de Floresta Encantada (Capítulo 1), aprendi a importância de uma estrutura de código clara e modular. No futuro, pretendo:
Aprofundar Narrativa e Decisões: Fazer com que escolhas anteriores impactem eventos futuros, tornando a história mais envolvente.
Caso o jogo siga para novos capítulos, levará tempo para manter e expandir a qualidade, mas o projeto tem potencial para crescer.

## **English**

# Enchanted Forest - Chapter 2 - Coming Soon!

Welcome to the continuation of your adventure in the Enchanted Forest! 

## **Release Date:** [2025]

### **What's New in Chapter 2**
- **Inventory:** Collect items and use them to progress in the adventure.
- **Custom Endings:** Unique and funny endings based on your choices.
- **Improved Code:** More modular structure to facilitate future expansions.

### **How to Play**
You can continue from Chapter 1 or start directly with Chapter 2. Make wise choices to explore safer paths or discover unexpected endings!
# Game Overview

**The Enchanted Forest** is a game where the player explores a forest with multiple endings. The objective is to find the ending that concludes the first chapter by making the right decisions. Along one of the paths, the player encounters a strange creature. This game offers a lighthearted experience.

## Origin of the Game Idea

The idea for the game came from a colleague who suggested a storyline with choices and different endings.

# Game Description

## Main Features and Mechanics of the Game

- **Choices and Paths:** Decisions that affect the adventure and lead to different scenarios.
- **Survival Actions:** Choices to fight, flee, or use items or face tragic outcomes.
- **Varied Endings:** Different outcomes including happy and tragic endings, with a generic message for "game over" situations.

## Narrative Structure and Choice Logic

The game allows the player to choose between two main paths: to the right (a dark cabin with an entity) and to the left (an iron door to be inspected). Each choice leads to different actions and outcomes—happy and tragic—with a generic "game over" message if the player loses. This structure creates an adventure with multiple endings.

# Implementation Techniques

## Code Structure

The code structure of **Enchanted Forest** can be organized into functions for easier readability and maintenance:
- `start_game()`: Presents the introduction and asks if the player wants to start.
- `path_right()` and `path_left()`: Handle the scenarios of each path, organizing specific choices and events.
- Final Functions: Each ending (happy, tragic, etc.) is managed by a separate function, allowing for easy expansion.

## Control Flow

In the game, control flow is primarily managed through `if`, `elif`, and `else` conditions, which allow the game to respond to the player's choices, such as starting the game and deciding between the paths. While loops are not currently used but could be implemented in the future.

## Data Management

Data management is primarily done with variables to store essential information, such as the player's name (`player_name`) and their choices (e.g., `direction = ...`). The decisions and game state are controlled by these variables.

## User Interaction

User interactivity is achieved through text inputs. The game presents a choice and prompts the player for a response using the `input()` function. For example, to choose a direction, the player enters a specific letter (e.g., "R" for right or "L" for left). If an invalid input is given, it is compared against valid options, displaying an error message.

# Challenges and Solutions

## Challenges Encountered During Code Development and How I Overcame Them

During the development of the game, several challenges arose. Here are two main challenges and their solutions:
- **Invalid Choice Management:** One of the first problems was ensuring that the player made valid choices (like “R” or “L” for direction). Invalid inputs caused flow issues in the game. To solve this, we implemented checks using `if` and `else` to validate entries and display error messages if the player typed something incorrect.
- **Maintaining Code Structure:** As the game grew, the code became difficult to read and update. The solution was to break the code into functions for each segment of the game, such as `start_game()` and `path_right()`.

# Conclusion

In developing **Enchanted Forest (Chapter 1)**, I learned the importance of a clear and modular code structure. In the future, I plan to:
- **Deepen Narrative and Decisions:** Make previous choices impact future events, making the story more engaging.
- If the game moves on to new chapters, it will take time to maintain and expand quality, but the project has the potential to grow.



