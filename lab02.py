# 0 = Não
# 1 = Sim
# 2 = Sim, realizo testes e invasão de sistemas
# Outro número não é reconhecido.

print("Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.")

pergunta_linux = input("Seu SO anterior era Linux?\n(0) Não\n(1) Sim\n")
if pergunta_linux == "0":
    pergunta_macos = input("Seu SO anterior era um MacOS?\n(0) Não\n(1) Sim\n")
    if pergunta_macos == "1": 
        print("Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: ElementaryOS, ApricityOS.")
    elif pergunta_macos == "0": 
        print("Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro.")
    else:
        print("Opção inválida, recomece o questionário.")
elif pergunta_linux == "1":
    pergunta_prog = input("É programador/ desenvolvedor ou de áreas semelhantes?\n(0) Não\n(1) Sim\n(2) Sim, realizo testes e invasão de sistemas\n")
    if pergunta_prog == "2":
        print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Kali Linux, Black Arch.")
    elif pergunta_prog == "0":
        print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Ubuntu Mint, Fedora.")
    elif pergunta_prog == "1":
        pergunta_conf = input("Gostaria de algo pronto para uso ao invés de ficar configurando o SO?\n(0) Não\n(1) Sim\n")
        if pergunta_conf == "0":
            pergunta_arch = input("Já utilizou Arch Linux?\n(0) Não\n(1) Sim\n")
            if pergunta_arch == "0":
                print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Antergos, Arch Linux.")
            elif pergunta_arch == "1":
                print("Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Gentoo, CentOS, Slackware.")
            else:
                print("Opção inválida, recomece o questionário.")
        elif pergunta_conf == "1":
            pergunta_deb = input("Já utilizou Debian ou Ubuntu?\n(0) Não\n(1) Sim\n")
            if pergunta_deb == "0":
                print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu.")
            elif pergunta_deb == "1":
                print ("Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Manjaro, ApricityOS.")
            else:
                print("Opção inválida, recomece o questionário.")
        else:
            print("Opção inválida, recomece o questionário.")
    else:
        print("Opção inválida, recomece o questionário.")
else:
    print("Opção inválida, recomece o questionário.")