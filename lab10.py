def damage(target, body_part, arrow_type, monster, attack_place):  # tá nesse dicionário
    ''' Calcula o dano que cada máquina sofre de acordo com o tipo de flecha
    que é atingida e o local do ataque.
    '''
    critic_reached = False
    critic_place = monster[target][body_part][2]
    arrow_critic = monster[target][body_part][0]
    if arrow_type == arrow_critic or monster[target][body_part][0] == "todas":
        damage = monster[target][body_part][1] - (abs(critic_place[0] - attack_place[0]) + abs(critic_place[1] - attack_place[1])) 
        damage = max(0, damage)  # cx e fx
    else:
        damage = (monster[target][body_part][1] - (abs(critic_place[0] - attack_place[0]) + abs(critic_place[1] - attack_place[1]))) // 2
        damage = max(0, damage)
    if attack_place == critic_place:
        critic_reached = True
    return damage, critic_reached, critic_place


def critic_place_listing(critics, li, critic_place, critic_reached):
    '''Retorna uma lista cuja posição corresponde a uma máquina, e nela
    está um dicionário cuja chave são seus pontos críticos e quantas
    vezes foram atingidos.'''
    if critic_reached:
        li[critic_place] += 1
    return critics


def arrows_type_listing(arrows, arrow_type):
    ''' Altera a quantidade de vezes que uma flecha de determinado tipo
    foi gasta.
    '''
    arrows[arrow_type][1] += 1
    return


def machines_attack(aloy_life_points, machines):
    '''Coordena os ataques da máquinas ainda viva em Aloy.'''
    aloy_alive = True
    for key in machines:
        if machines[key][0] > 0:
            aloy_life_points -= machines[key][1]
            aloy_life_points = max(0, aloy_life_points)
            if aloy_life_points == 0:
                aloy_life_points = False
                return aloy_life_points, aloy_alive
    return aloy_life_points, aloy_alive


def aloy_attack(target, body_part, monster, arrows, arrow_type, fx, fy, li, critics):
    ''' Estruturação da sequência de ataque de Aloy, calculando o dano,
    trazendo a possível presença de pontos críticos atingidos e alterando
    a contagem de flechas gastas.
    '''
    attack_place = (fx, fy)
    damages, critic_reached, critic_place = damage(target, body_part, arrow_type, monster, attack_place)
    critics = critic_place_listing(critics, li, critic_place, critic_reached)
    arrows_type_listing(arrows, arrow_type)
    return damages, critics


def get_arrow(arrows):
    '''Reseta a quantidade de flechas disparadas por Aloy.
    '''
    for key in arrows:
        arrows[key][1] = 0
    return arrows


def main():
    max_life = int(input())
    aloy_life_points = max_life
    arrow_amount = input().split()
    arrows = {}
    # arrows_listing = []
    for i in range(len(arrow_amount)):
        if i % 2 == 0:
            arrows[arrow_amount[i]] = [int(arrow_amount[i + 1]), 0]
            # arrows: {tipo: [quantidade dispònivel, quantidade gasta]}

    amount_monsters = int(input())
    monster_defeated = 0
    k = 0
    aloy_alive = True
    while k >= 0 and monster_defeated != amount_monsters and aloy_alive is True:  # monstros derrotados, aloy morta, com flecha
        arrows = get_arrow(arrows)
        machines = {}
        machines_parts = {}
        monster = []
        critics = []
        machines_combat = int(input())
        for perfil in range(machines_combat):
            life_points, attack_points, parts_quant = input().split()
            machines[perfil] = [int(life_points), int(attack_points), int(parts_quant)]
            li = {}
            critics.append(li)
            # maquinas {machines(número): [live_points, attack_points, parts_quant]}
            for _ in range(machines[perfil][2]):
                body_part, weakness, max_damage, x_coordenate, y_coordenate = input().split(sep=", ")
                machines_parts[body_part] = [weakness, int(max_damage), (int(x_coordenate), int(y_coordenate))]
                monster.append(machines_parts)
                critics[perfil][machines_parts[body_part][2]] = 0
                # parts {body_part: [weaknees, max_damage, (x_coordenate, y_coordenate)]}

        combat = True
        print("Combate ", k, ", vida = ", aloy_life_points, sep='')
        machines_defeated = 0

        while combat is True:
            target, body_part, arrow_type, fx, fy = input().split(sep=", ")
            target = int(target)
            # aloy_attack(target, body_part, arrow_type, fx, fy)
            damage, critics = aloy_attack(int(target), body_part, monster, arrows, arrow_type, int(fx), int(fy), li, critics)
            machines[target][0] -= damage
            machines[target][0] = max(0, machines[target][0])
            if machines[target][0] == 0:
                print("Máquina", target, "derrotada")
                machines_defeated += 1
                monster_defeated += 1

            if machines_defeated == machines_combat:
                print("Vida após o combate =", aloy_life_points)
                print("Flechas utilizadas:")
                for key in arrows:
                    if arrows[key][1] != 0:
                        print("- ", key, ": ", arrows[key][1], "/", arrows[key][0], sep='')

                critic_ocurred = False
                for n in range(len(critics)):
                    for t in critics[n]:
                        if critics[n][t] != 0:
                            critic_ocurred = True

                if critic_ocurred is True:
                    print("Críticos acertados:")
                    for i in range(len(critics)):
                        print("Máquina ", i, ":", sep='')

                        for m in critics[0]:
                            if critics[0][m] != 0:
                                print("- ", m, ": ", li[m], "x", sep='')

                combat = False

            elif machines_defeated != machines_combat:
                aloy_life_points, aloy_alive = machines_attack(aloy_life_points, machines)

                if not aloy_alive:
                    combat = False

            if aloy_alive:
                aloy_life_points += max_life // 2
                aloy_life_points = min(aloy_life_points, max_life)

        if not aloy_alive:
            print("Vida após o combate =", aloy_life_points)
            print("Aloy foi derrotada em combate e não retornará a tribo.")

        if aloy_alive and monster_defeated == amount_monsters:
            print("Aloy provou seu valor e voltou para sua tribo.")

        k += 1


if __name__ == "__main__":
    main()
