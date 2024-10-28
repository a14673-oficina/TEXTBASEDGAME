<h1>TextBasedGame<h1>
print(f"{'Seja bem-vindo a Floresta Encantada!' :^65}")

NomeJ = input("Qual vai ser o nome do Jogador? > ")
print(f"{NomeJ}! Queres Iniciar o Jogo?")
IniciarJogo = str(input("Sim (S) ou Não (N)? > "))
IniciarJogo1 = IniciarJogo.lower()
if IniciarJogo1 == "s":
  print("A iniciar o jogo")
  direção1 = input(f"{NomeJ}, queres ir pela entrada da direita (D) ou esquerda (E) > ")
  direção1.lower()
  if direção1 == "d":
    print("Encontras-te uma cabana, vamos entrar.")
    print("Está muito escuro, usa a tua lanterna.")
    lanterna = input(f"{NomeJ}, Clicar na tecla (F) e (Enter) para ligar a lanterna > ")
    lanterna.lower()
    if lanterna == "f":
      print("Lanterna Ligada")
    else: 
      print("A letra persionada não é (F),.")
    print(f"{NomeJ}, ao Iluminar tu encontras-te uma Entidade, Visual: Cabeça Voadora.")
    Ataque = input("CORRER PELA SUA VIDA(C) ou Enfrentar a Entidade (E)? > ")
    Ataque.lower()
    if Ataque == "c":
      print("Tu corres-te para o carro, a Entidade tentou acabar com o carro mas felizmente conseguite escapar - Obrigado por jogar, tem outro fim")
      print(f"{'Final Feliz(YEAP)' :^65}") #4
      exit()
    elif Ataque == "e":
      print("Tu Atacaste a Entidade sem nada, achavas que ia derrotala, pela amor de deu!")
      print(f"{'Final Estupido (Game Over)' :^65}") #3
      exit()
    else: 
      print("A letra persionada não é a certa.")
  elif direção1 == "e":
    print("Depois de andares mais ou menos 1km, entontras-te uma porta de ferro.")
    caminho = input(f"{NomeJ}, Tu pertendes Ignorar (I) ou Especionar (E)? > ")
    caminho.lower()
    if caminho == "i":
      print("Pouca sorte caio uma arvore em sima de ti!")
      print(f"{'Final da Arvore podre (Game Over)' :^65}") #2
      exit()
    elif caminho == "e":
      print("Pare-se que para abrir a porta é necessario que a alavanca tenha energia.")
      print("Pare-se que encontras-te um gerador, tu ligaste.")
      print("Porta Aberta!")
      print("Tu acabaste de descer umas escadas, (PRIMEIRO CAPITULO COMCLUIDO) - Obrigado por jogar")
      print(f"{'Final Normal' :^65}") #1
      exit()
  else: 
    print("A letra persionada não é a certa.")
elif IniciarJogo1 == "n":
  print("O jogo foi cancelado")
else: 
  print("A letra persionada não é a certa.")
  exit()
