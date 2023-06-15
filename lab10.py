#  Caçadora e arqueira Aloy combate máquinas ao explorar seu mundo.

def damage(aloy, monster):
    '''Calcula o dano que cada máquina sofre de acordo com o tipo de flecha
    que é atingida e o local do ataque. Caso o ataque seja no ponto crítico,
    salva a ocorrência para a criação de um dicionário correspondente.
    Parâmetros:
    argumentos:
        aloy (list)
        monster (list)
        column (int)
    retorno:
        damage (int)
        critic_reached (bool)
        critic_place (tuple)
        '''
    critic_reached = False
    critic_place = monster[aloy[0]][aloy[1]][2]
    arrow_critic = monster[aloy[0]][aloy[1]][0]
    if aloy[2] == arrow_critic or monster[aloy[0]][aloy[1]][0] == "todas":
        damage = (monster[aloy[0]][aloy[1]][1] -
                  (abs(critic_place[0] - aloy[3][0]) +
                   abs(critic_place[1] - aloy[3][1])))
        damage = max(0, damage)
    else:
        damage = ((monster[aloy[0]][aloy[1]][1] -
                   (abs(critic_place[0] - aloy[3][0]) +
                    abs(critic_place[1] - aloy[3][1])))) // 2
        damage = max(0, damage)
    if aloy[3] == critic_place:
        critic_reached = True
    return damage, critic_reached, critic_place


def critic_place_listing(critics, critic_place, critic_reached, critic_ocurred, aloy):
    '''Retorna uma lista cuja posição corresponde a uma máquina, e nela
    está um dicionário cuja chave são seus pontos críticos e quantas
    vezes foram atingidos. Utiliza também uma variável booleana para
    salvar se há algum ponto crítico no combate.
    Parâmetros:
    argumentos:
        critics (list)
        critic_place (tuple)
        critic_reached (bool)
        critic_ocurred (bool)]
        aloy (list)
    retorno:
        critics (list)
        critic_ocurred (bool)
        '''
    if critic_reached:
        critic_ocurred = True
        critics[aloy[0]][critic_place] += 1
    return critics, critic_ocurred


def arrows_type_listing(arrows, aloy):
    '''Altera a quantidade de vezes que uma flecha de determinado tipo
    foi gasta.
    Parâmetros:
    argumentos:
        arrows (dic)
        aloy (list)
    retorn:
        None
        '''
    arrows[aloy[2]][1] += 1
    return


def machines_attack(aloy_life_points, machines):
    '''Coordena os ataques das máquinas ainda viva em Aloy e verifica se ela
    está viva após o confronto.
    Parâmetros:
    argumentos:
        aloy_life_points (int)
        machines (dic)
    retorno:
        aloy_life_points (int)
        aloy_alive (bool)
        '''
    aloy_alive = True
    for key in machines:
        if machines[key][0] > 0:
            aloy_life_points -= machines[key][1]
            aloy_life_points = max(0, aloy_life_points)
            if aloy_life_points == 0:
                aloy_alive = False
                return aloy_life_points, aloy_alive
    return aloy_life_points, aloy_alive


def aloy_attack(aloy, monster, arrows, critics, critic_ocurred):
    '''Estruturação da sequência de ataque de Aloy, calculando o dano,
    trazendo a possível presença de pontos críticos atingidos e alterando
    a contagem de flechas gastas.
    Parâmetros:
    argumentos:
        aloy (list)
        monster (list))
        arrows (dic)
        critics (list)
        critic_ocurred (bool)
    retorno:
        damages (int)
        critics (list)
        critic_ocurred (bool)
        '''
    damages, critic_reached, critic_place = damage(aloy, monster)
    critics, critic_ocurred = critic_place_listing(critics, critic_place, critic_reached, critic_ocurred, aloy)
    arrows_type_listing(arrows, aloy)
    return damages, critics, critic_ocurred


def reset_arrows(arrows):
    '''Reseta a quantidade de flechas disparadas por Aloy após cada combate.
    Parâmetros:
    argumentos:
        arrows (tdic)
    retorno:
        arrows (dic)
        '''
    for key in arrows:
        arrows[key][1] = 0
    return arrows


def main():
    max_life = int(input())
    aloy_life_points = max_life
    arrow_amount = input().split()
    arrows = {}
    for i in range(len(arrow_amount)):
        if i % 2 == 0:
            arrows[arrow_amount[i]] = [int(arrow_amount[i + 1]), 0]
            # arrows: {tipo: [quantidade disponível, quantidade gasta]}

    amount_monsters = int(input())
    monster_defeated = 0
    combat_numb = -1
    aloy_alive = True

    while True:  # sair do loop: monstros derrotados, aloy morta, aloy sem flecha
        combat_numb += 1
        arrows = reset_arrows(arrows)
        machines = {}  # maquinas {machines(número): [live_points, attack_points, parts_quant]}
        monster = []  # [machine_parts(maq 0), machine_parts(maq 1), ...]
        critics = []  # [critics_amount(maq 0), critics_amount(maq 1), ...]
        machines_combat = int(input())

        for perfil in range(machines_combat):
            critics_amount = {}  # critics_amount {ponto crítico: quantidade de vezes atingido}
            machines_parts = {}  # machine_parts {body_part: [weaknees, max_damage, (x_coordenate, y_coordenate)]}

            life_points, attack_points, parts_quant = input().split()
            machines[perfil] = [int(life_points), int(attack_points), int(parts_quant)]
            for _ in range(machines[perfil][2]):
                body_part, weakness, max_damage, x_coordenate, y_coordenate = input().split(sep=", ")
                machines_parts[body_part] = [weakness, int(max_damage), (int(x_coordenate), int(y_coordenate))]
                critics_amount[machines_parts[body_part][2]] = 0

            monster.append(machines_parts)
            critics.append(critics_amount)

        in_combat = True

        machines_defeated = 0
        attack = 0
        critic_ocurred = False
        print("Combate ", combat_numb, ", vida = ", aloy_life_points, sep='')

        while in_combat:
            target, body_part, arrow_type, fx, fy = input().split(sep=", ")
            aloy = [int(target), body_part, arrow_type, (int(fx), int(fy))]

            damage, critics, critic_ocurred = aloy_attack(aloy, monster, arrows, critics, critic_ocurred)
            attack += 1
            machines[aloy[0]][0] -= damage
            machines[aloy[0]][0] = max(0, machines[aloy[0]][0])

            if machines[aloy[0]][0] == 0:
                print("Máquina", aloy[0], "derrotada")
                machines_defeated += 1
                monster_defeated += 1

            if machines_defeated == machines_combat:
                print("Vida após o combate =", aloy_life_points)
                print("Flechas utilizadas:")

                for key in arrows:
                    if arrows[key][1] != 0:
                        print("- ", key, ": ", arrows[key][1], "/", arrows[key][0], sep='')

                if critic_ocurred is True:
                    print("Críticos acertados:")
                    for i in range(len(critics)):
                        first_out = True
                        for critics_key in critics[i]:
                            if critics[i][critics_key] != 0:
                                if first_out:
                                    print("Máquina ", i, ":", sep='')
                                    first_out = False
                                print("- ", critics_key, ": ", critics[i][critics_key], "x", sep='')

                in_combat = False

            elif machines_defeated != machines_combat and attack == 3:
                aloy_life_points, aloy_alive = machines_attack(aloy_life_points, machines)
                attack = 0

                if not aloy_alive:
                    in_combat = False

            arrows_spent = 0
            for x in arrows:
                if arrows[x][0] == arrows[x][1]:
                    arrows_spent += 1
            if arrows_spent == len(arrows.keys()):
                in_combat = False

        if arrows_spent == len(arrows.keys()):
            print("Vida após o combate =", aloy_life_points)
            print("Aloy ficou sem flechas e recomeçará sua missão mais preparada.")
            break

        if aloy_alive and not in_combat:
            aloy_life_points += max_life // 2
            aloy_life_points = min(aloy_life_points, max_life)

        if not aloy_alive:
            print("Vida após o combate =", aloy_life_points)
            print("Aloy foi derrotada em combate e não retornará a tribo.")
            break

        if aloy_alive and monster_defeated == amount_monsters:
            print("Aloy provou seu valor e voltou para sua tribo.")
            break


if __name__ == "__main__":
    main()
