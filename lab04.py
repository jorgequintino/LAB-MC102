# Monitoramento "Veterinário & Pet Shop Focinhos":

# Quantidades de dias a serem analisados.
amount_days = int(input())
for i in range(amount_days):

    # Pares de animais que brigam.
    fight_pairs = int(input())
    fight_pairs_set = []
    for _ in range(fight_pairs):
        d = input().split()
        fight_pairs_set.append(d[0])
        fight_pairs_set.append(d[1])

    # Relação de procedimentos e suas respectivas quantidades.
    procedures_quant = input().split()
    procedures_available = []
    quant_available = []
    for p in range(len(procedures_quant)):
        if p % 2 == 0:
            procedures_available.append(procedures_quant[p])
        else:
            quant_available.append(int(procedures_quant[p]))

    # Quantos e quais animais foram recebidos e o procedimento desejado.
    amount_animals_that_day = int(input())
    animals_name = []
    procedures_desired = []
    for _ in range(amount_animals_that_day):
        animal, procedure = input().split()
        animals_name.append(animal)
        procedures_desired.append(procedure)

    # Brigas ocorridas
    amount_fights = 0
    for t in range(0, len(fight_pairs_set), 2):
         if fight_pairs_set[t] in animals_name and fight_pairs_set[t+1] in animals_name:
             amount_fights += 1

    # Atendimentos feitos
    animals_attended = []
    animals_not_attended = []
    animals_not_available = []
    for z in range(len(procedures_desired)):
        if procedures_desired[z] in procedures_available:
            for d in range(len(procedures_available)):
                procedure = procedures_desired[z]
                if procedures_available[d] == procedure and quant_available[d] > 0:
                    quant_available[d] += -1
                    animals_attended.append(animals_name[z])
                elif procedures_available[d] == procedure and quant_available[d] == 0:
                    animals_not_attended.append(animals_name[z])
        elif not procedures_desired[z] in procedures_available:
            animals_not_available.append(animals_name[z])

    # Saída da relação de cada dia
    print("Dia:", i+1)
    print("Brigas:", amount_fights)
    if animals_attended:
        print("Animais atendidos: ", end="")
        print(*animals_attended, sep=", ")
    if animals_not_attended:
        print("Animais não atendidos: ", end="")
        print(*animals_not_attended, sep=", ")
    if animals_not_available:
        for n in range(len(animals_not_available)):
            print("Animal", animals_not_available[n], "solicitou procedimento não disponível.")
    print("")