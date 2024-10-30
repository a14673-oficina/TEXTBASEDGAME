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
