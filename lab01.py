# Escolha do filme para assistir baseado no jogo Pedra-Papel-Tesoura-Lagarto-Spock!

sheila_move = input()
reginaldo_move = input()

if sheila_move == "tesoura" and reginaldo_move == "papel":
    print("Interestelar")
elif sheila_move == "papel" and reginaldo_move == "pedra":
    print("Interestelar")
elif sheila_move == "pedra" and reginaldo_move == "lagarto":
    print("Interestelar")
elif sheila_move == "lagarto" and reginaldo_move == "spock":
    print("Interestelar")
elif sheila_move == "spock" and reginaldo_move == "tesoura":
    print("Interestelar")
elif sheila_move == "tesoura" and reginaldo_move == "lagarto":
    print("Interestelar")
elif sheila_move == "lagarto" and reginaldo_move == "papel":
    print("Interestelar")
elif sheila_move == "papel" and reginaldo_move == "spock":
    print("Interestelar")
elif sheila_move == "spock" and reginaldo_move == "pedra":
    print("Interestelar")
elif sheila_move == "pedra" and reginaldo_move == "tesoura":
    print("Interestelar")
elif sheila_move == "papel" and reginaldo_move == "tesoura":
    print("Jornada nas Estrelas")
elif sheila_move == "pedra" and reginaldo_move == "papel":
    print("Jornada nas Estrelas")
elif sheila_move == "lagarto" and reginaldo_move == "pedra":
    print("Jornada nas Estrelas")
elif sheila_move == "spock" and reginaldo_move == "lagarto":
    print("Jornada nas Estrelas")
elif sheila_move == "tesoura" and reginaldo_move == "spock":
    print("Jornada nas Estrelas")
elif sheila_move == "lagarto" and reginaldo_move == "tesoura":
    print("Jornada nas Estrelas")
elif sheila_move == "papel" and reginaldo_move == "lagarto":
    print("Jornada nas Estrelas")
elif sheila_move == "spock" and reginaldo_move == "papel":
    print("Jornada nas Estrelas")
elif sheila_move == "pedra" and reginaldo_move == "spock":
    print("Jornada nas Estrelas")
elif sheila_move == "tesoura" and reginaldo_move == "pedra":
    print("Jornada nas Estrelas")
else:
    print("empate")