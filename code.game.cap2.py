def mostrar_mensagem_centralizada(mensagem, largura=65):
  print(f"{mensagem:^{largura}}")

def criar_inventario():
  return []

def adicionar_ao_inventario(inventario, item):
  inventario.append(item)

def exibir_inventario(inventario):
  if inventario:
      print("Itens no teu inventário:")
      for item in inventario:
          print(f"- {item}")
  else:
      print("O teu inventário está vazio.")

def mostrar_menu():
  print("\nMenu Principal:")
  print("1. Continuar Aventura")
  print("2. Ver Inventário")
  print("3. Sair do Jogo")
  escolha = input("Escolhe uma opção: > ").strip()
  return escolha

def perguntar_reiniciar():
  escolha = input("Queres reiniciar o jogo (R) ou retomar da página anterior (P)? > ").strip().lower()
  return escolha

def iniciar_jogo():
  NomeJ = input("Qual vai ser o nome do Jogador? > ")
  mostrar_mensagem_centralizada(f"Bem-vindo ao Capítulo 2, {NomeJ}!")

  inventario = criar_inventario()
  while True:
      escolha = mostrar_menu()
      if escolha == "1":
          capitulo_2(NomeJ, inventario)
      elif escolha == "2":
          exibir_inventario(inventario)
      elif escolha == "3":
          print("O jogo foi encerrado. Obrigado por jogar!")
          exit()
      else:
          print("Opção inválida. Tenta novamente!")

def capitulo_2(NomeJ, inventario):
  print("Depois de descer as escadas, encontras-te num corredor sombrio e frio.")
  print("Há duas direções à tua frente: uma porta à esquerda e uma passagem à direita.")

  escolha = input(f"{NomeJ}, Seguir pela porta (P) ou pela passagem (R)? > ").strip().lower()
  if escolha == "p":
      explorar_porta(NomeJ, inventario)
  elif escolha == "r":
      explorar_passagem(NomeJ, inventario)
  else:
      print("Escolha inválida. Tenta novamente!")
      capitulo_2(NomeJ, inventario)

def explorar_porta(NomeJ, inventario):
  print("A porta range ao ser aberta e revela uma sala cheia de livros antigos e estranhos.")
  print("No centro da sala, há um pedestal com um livro iluminado.")

  acao = input(f"{NomeJ}, Lê o livro (L) ou sai da sala (S)? > ").strip().lower()
  if acao == "l":
      print("Ao abrir o livro, uma luz ofuscante envolve-te. A tua mente é preenchida com conhecimento proibido!")
      mostrar_mensagem_centralizada("Final Misterioso (Game Over)")
      print("Hmmm... talvez mexer no desconhecido não tenha sido a melhor ideia. Reinicia e tenta algo diferente!")
      reiniciar_ou_retomar(NomeJ, inventario)
  elif acao == "s":
      print("Deixas a sala rapidamente, sentindo um arrepio na espinha.")
      capitulo_2(NomeJ, inventario)  # Volta ao corredor
  else:
      print("Escolha inválida. Tenta novamente!")
      explorar_porta(NomeJ, inventario)

def explorar_passagem(NomeJ, inventario):
  print("A passagem é estreita e cheia de teias de aranha. Ao fundo, vês uma luz fraca.")
  print("Aproximas-te e percebes que é uma lanterna caída ao lado de uma mochila.")

  acao = input(f"{NomeJ}, Pegar na mochila (M) ou ignorar (I)? > ").strip().lower()
  if acao == "m":
      print("Dentro da mochila, encontras um mapa e uma chave enferrujada.")
      adicionar_ao_inventario(inventario, "Mapa")
      adicionar_ao_inventario(inventario, "Chave Enferrujada")
      exibir_inventario(inventario)
      print("O mapa indica um caminho secreto para a saída da floresta.")
      mostrar_mensagem_centralizada("Final Inteligente - Sobreviveste!")
      print("Bua! És incrível! Obrigado por jogar. Aguarda pelo Capítulo 3, onde mais mistérios te aguardam!")
      exit()
  elif acao == "i":
      print("Ignoras a mochila e segues em frente. Uma armadilha é ativada e és capturado!")
      mostrar_mensagem_centralizada("Final Trágico (Game Over)")
      print("Meu Deus, o que achavas que ia acontecer? Tenta novamente e presta mais atenção!")
      reiniciar_ou_retomar(NomeJ, inventario)
  else:
      print("Escolha inválida. Tenta novamente!")
      explorar_passagem(NomeJ, inventario)

def reiniciar_ou_retomar(NomeJ, inventario):
  escolha = perguntar_reiniciar()
  if escolha == "r":
      iniciar_jogo()
  elif escolha == "p":
      capitulo_2(NomeJ, inventario)
  else:
      print("Escolha inválida. Tenta novamente!")
      reiniciar_ou_retomar(NomeJ, inventario)

# Início do jogo
mostrar_mensagem_centralizada("Seja bem-vindo à Floresta Encantada - Capítulo 2!")
iniciar_jogo()