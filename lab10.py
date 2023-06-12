def damage(target, body_part, arrow_type, monster, attack_place):  # tá nesse dicionário
    critic_reached = False
    critic_place = monster[target][body_part][2]
    arrow_critic = monster[target][body_part][0]
    if arrow_type == arrow_critic or monster[target][body_part][0] == "todas":
        damage = monster[target][body_part][1] - (abs(critic_place[0] - attack_place[0]) + abs(critic_place[1] - attack_place[1]))  # cx e fx
    else:
        damage = (monster[target][body_part][1] - (abs(critic_place[0] - attack_place[0]) + abs(critic_place[1] - attack_place[1]))) // 2
    if attack_place == critic_place:
        critic_reached = True
    return damage, critic_reached, critic_place


def critic_place_listing(critics, li, critic_place, critic_reached):
    if critic_reached:
        li[critic_place] += 1
    return critics


def arrows_type_listing(arrows, arrow_type):
    arrows[arrow_type][1] += 1
    return


def machines_attack(aloy_life_points, machines):
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
    attack_place = (fx, fy)
    damages, critic_reached, critic_place = damage(target, body_part, arrow_type, monster, attack_place)
    critics = critic_place_listing(critics, li, critic_place, critic_reached)
    arrows_type_listing(arrows, arrow_type)
    return damages, critics


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
    i = 0
    while i < amount_monsters:  # While pode ser melhor
        arrows[arrow_amount[i]][1] = 0
        machines = {}
        machines_parts = {}
        monster = []       # lista é melhor
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
                li[machines_parts[body_part][2]] = 0
                # parts {body_part: [weaknees, max_damage, (x_coordenate, y_coordenate)]}

        combat = True
        print("Combate",i, ", vida =", aloy_life_points)
        machines_defeated = 0
        aloy_alive = True

        while combat is True:
            target, body_part, arrow_type, fx, fy = input().split(sep=", ")
            target = int(target)
            # aloy_attack(target, body_part, arrow_type, fx, fy)
            damage, critics = aloy_attack(int(target), body_part, monster, arrows, arrow_type, int(fx), int(fy), li, critics)
            machines[target][0] -= damage
            machines[target][0] = max(0, machines[target][0])
            if machines[target][0] == 0:
                print("Máquina", target, "derrotada.")
                machines_defeated += 1

            if machines_defeated == machines_combat:
                print("Vida após o combate =", aloy_life_points)
                print("Flechas utilizadas:")
                for i in arrows:
                    if arrows[i][1] != 0:
                        print("-", i,":", arrows[i][1],"/",arrows[i][0])
                print("Críticos acertados:")
                if not critics == []:
                    for i in range(len(critics)):
                        print("Máquina", i,":")

                        for m in critics[0]:
                            if critics[0][m] != 0:
                                print("-", m,":", li[m],"x")

                combat = False

            elif not monster == []:
                aloy_life_points, aloy_alive = machines_attack(aloy_life_points, machines)

            if not aloy_alive:
                combat = False

            aloy_life_points += max_life // 2
            aloy_life_points = min(aloy_life_points, max_life)

        if not aloy_alive:
            print("Vida após o combate =", aloy_life_points)
            print("Aloy foi derrotada em combate e não retornará a tribo.")
            break

        if aloy_alive:
            print("Aloy provou seu valor e voltou para sua tribo.")
            break

        i += 1

if __name__ == "__main__":
    main()

    # quando as flechas acabaram
    # quando ela termina viva, mas ainda tem outros cobtes para fazer
    # checar dano negativo
