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
    if lanterna == "F":
      print("Lanterna Ligada")
    else: 
      print("A letra persionada não é (F).")
    print(f"{NomeJ}, ao Iluminar tu encontras-te uma Entidade, Visual: Cabeça Voadora.")
    Ataque = input("CORRER PELA SUA VIDA(C) ou Enfrentar a Entidade (E)? > ")
  elif direção1 == "e":
    print()
elif IniciarJogo1 == "n":
  print("O jogo foi cancelado")
