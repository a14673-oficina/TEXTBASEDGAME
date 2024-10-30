<h1>TextBasedGame<h1>

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

**Estrutura do Código.**

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

English
Game Overview
The Enchanted Forest is a game where the player explores a forest with various different endings. The goal is to find the ending that completes the first chapter by making the right decisions; in one of the paths, the player faces a strange creature. This game offers a light-hearted experience.

Where the Idea for the Game Came From.

The idea for the game came from a colleague who suggested a plot with choices and different endings.

Game Description
Main Features and Mechanics of the Game.

Choices and Paths: Decisions that affect the adventure and lead to different scenarios.

Survival Actions: Choices to fight, flee, or use items or tragic actions.

Varied Endings: Different outcomes with happy or death endings.

Narrative Structure and the Logic of Choices.

The game allows the player to choose between two main paths: to the right (dark cabin with an entity) and to the left (iron door to be inspected). Each choice leads to different actions and outcomes—happy and tragic—with a generic message in case of losing: “game over.” This structure creates an adventure with multiple endings.

Implementation Techniques
Code Structure.

The code structure for Enchanted Forest can be organized into functions for easier reading and maintenance:
start_game(): Presents the introduction and asks if the player wants to start.
right_path() and left_path(): Handle the scenarios for each path, organizing the choices and specific events.
Ending Functions: Each ending (happy, tragic, etc.) is managed by a separate function, allowing for easy expansion.

Control Flow.

In the game, the control flow is mainly managed by if, elif, and else conditions, which allow the game to respond to the player's choices, such as starting and deciding between paths. While loops are not currently used but could be implemented in the future of the game.

Data Management.

Data management is mainly done with variables to store essential information, such as the player's name (NameJ) and their choices (example: direction = ...). Decisions and the game state are controlled by these variables.

User Interaction.

User interaction is done through text inputs. The game presents a choice and requests a response from the player via the input() function. For example, to choose the direction, the player enters a specific letter (e.g., "D" or "E"), and in case of an error, the input is compared with valid options, displaying an error message.

Challenges and Solutions.
Challenges Faced During Code Development and How I Overcame Them.

During the development of the game, some challenges arose. Here are two main ones and how they were resolved:
Management of Invalid Choices: One of the first problems was ensuring that the player made valid choices (like “D” or “E” for the direction). Invalid inputs caused failures in the game's flow. To solve this, I implemented a check with if and else to validate the entries and display error messages if the player typed something wrong.
Maintaining Code Structure: As the game grew, the code became difficult to read and update. The solution was to split the code into functions for each segment of the game, such as start_game() and right_path().

Conclusion
In the development of Enchanted Forest (Chapter 1), I learned the importance of a clear and modular code structure. In the future, I plan to:
Deepen Narrative and Decisions: Ensure that previous choices impact future events, making the story more engaging.
If the game proceeds to new chapters, it will take time to maintain and expand the quality, but the project has potential for growth.

Français
Aperçu du jeu
La Forêt Enchantée est un jeu où le joueur explore une forêt avec plusieurs fins différentes. L'objectif est de trouver la fin qui conclut le premier chapitre en prenant les bonnes décisions ; dans l'un des chemins, le joueur est confronté à une créature étrange. Ce jeu offre une expérience légère.

D'où vient l'idée du jeu.

L'idée du jeu est venue d'un collègue qui a suggéré une intrigue avec des choix et des fins différentes.

Description du Jeu
Principales fonctionnalités et mécaniques du jeu.

Choix et Chemins : Décisions qui affectent l'aventure et mènent à différents scénarios.

Actions de Survie : Choix de se battre, fuir ou utiliser des objets ou des actions tragiques.

Fins Variées : Différentes issues avec des fins heureuses ou mortelles.

Structure narrative et la logique des choix.

Le jeu permet au joueur de choisir entre deux chemins principaux : à droite (cabane sombre avec une entité) et à gauche (porte en fer à inspecter). Chaque choix mène à différentes actions et résultats — heureux et tragiques — avec un message générique en cas de perte : « game over ». Cette structure crée une aventure avec plusieurs fins.

Techniques d'Implémentation
Structure du Code.

La structure du code de La Forêt Enchantée peut être organisée en fonctions pour faciliter la lecture et la maintenance :
demarrer_jeu(): Présente l'introduction et demande si le joueur souhaite commencer.
chemin_droite() et chemin_gauche(): Gèrent les scénarios de chaque chemin, organisant les choix et événements spécifiques.
Fonctions de Fins : Chaque fin (heureuse, tragique, etc.) est gérée par une fonction séparée, permettant une expansion facile.

Contrôle de Flux.

Dans le jeu, le contrôle de flux est principalement géré par des conditions if, elif et else, qui permettent au jeu de répondre aux choix du joueur, comme commencer et décider entre les chemins. Les boucles while ne sont pas actuellement utilisées mais pourraient être mises en œuvre dans le futur du jeu.

Gestion des Données.

La gestion des données est principalement effectuée avec des variables pour stocker des informations essentielles, comme le nom du joueur (NomJ) et ses choix (exemple : direction = ...). Les décisions et l'état du jeu sont contrôlés par ces variables.

Interaction avec l'Utilisateur.

L'interaction avec le joueur se fait par le biais d'entrées de texte. Le jeu présente un choix et demande une réponse du joueur via la fonction input(). Par exemple, pour choisir la direction, le joueur saisit une lettre spécifique (par exemple, "D" ou "G"), et en cas d'erreur, l'entrée est comparée aux options valides, affichant un message d'erreur.

Défis et Solutions.
Défis rencontrés lors du développement du code et comment je les ai surmontés.

Au cours du développement du jeu, certains défis sont apparus. Voici deux principaux et comment ils ont été résolus :
Gestion des Choix Invalides : L'un des premiers problèmes a été de garantir que le joueur faisait des choix valides (comme “D” ou “G” pour la direction). Les entrées invalides provoquaient des échecs dans le flux du jeu. Pour résoudre cela, j'ai mis en place une vérification avec if et else pour valider les entrées et afficher des messages d'erreur si le joueur saisissait quelque chose de faux.
Maintien de la Structure du Code : À mesure que le jeu grandissait, le code devenait difficile à lire et à mettre à jour. La solution a été de diviser le code en fonctions pour chaque segment du jeu, comme demarrer_jeu() et chemin_droite().

Conclusion
Dans le développement de La Forêt Enchantée (Chapitre 1), j'ai appris l'importance d'une structure de code claire et modulaire. À l'avenir, je prévois de :
Approfondir la Narration et les Décisions : Faire en sorte que les choix précédents impactent les événements futurs, rendant l'histoire plus engageante.
Si le jeu progresse vers de nouveaux chapitres, cela prendra du temps pour maintenir et élargir la qualité, mais le projet a le potentiel de croître.

Español
Descripción del Juego
El Bosque Encantado es un juego donde el jugador explora un bosque con varios finales diferentes. El objetivo es encontrar el final que completa el primer capítulo tomando las decisiones correctas; en uno de los caminos, el jugador se enfrenta a una criatura extraña. Este juego ofrece una experiencia ligera.

De dónde surgió la idea para el juego.

La idea del juego vino de un colega que sugirió una trama con elecciones y diferentes finales.

Descripción del Juego
Principales funcionalidades y mecánicas del juego.

Elecciones y Caminos: Decisiones que afectan la aventura y conducen a diferentes escenarios.

Acciones de Supervivencia: Elecciones de luchar, huir y usar objetos o acciones trágicas.

Finales Variados: Diferentes desenlaces con finales felices o de muerte.

Estructura narrativa y la lógica de las elecciones.

El juego permite que el jugador elija entre dos caminos principales: a la derecha (cabaña oscura con una entidad) y a la izquierda (puerta de hierro para inspeccionar). Cada elección lleva a diferentes acciones y desenlaces — felices y trágicos — con un mensaje genérico en caso de perder: “game over.” Esta estructura crea una aventura con múltiples finales.

Técnicas de Implementación
Estructura del Código.

La estructura del código de El Bosque Encantado
