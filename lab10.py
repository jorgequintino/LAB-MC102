def damage(target, body_part, arrow_type, machines, machines_parts, monster, attack_place, critics):  # tá nesse dicionário
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
    keys = machines.keys()
    for key in keys:
        aloy_life_points -= machines[key][1]
        aloy_life_points = max(0, aloy_life_points)
        if aloy_life_points == 0:
            aloy_life_points = False
            return aloy_life_points, aloy_alive
    return aloy_life_points, aloy_alive


def aloy_attack(target, body_part, machines, machines_parts, monster, arrows, arrow_type, fx, fy, li, critics):
    attack_place = (fx, fy)
    damages, critic_reached, critic_place = damage(target, body_part, arrow_type, machines, machines_parts, monster, attack_place)
    critics = critic_place_listing(critics, li, critic_place, critic_reached)
    arrows_listing = arrows_type_listing(arrows, arrow_type)
    return damages, critics, arrows_listing


def main():
    aloy_life_points = max_life = int(input())
    arrow_amount = [input(sep=" ")]
    arrows = {}
    # arrows_listing = []
    for i in range(len(arrow_amount)):
        if i % 2 == 0:
            arrows[arrow_amount[i]] = [int(arrow_amount[i + 1]), 0]
            # arrows: {tipo: [quantidade dispònivel, quantidade gasta]}
            # onde eu reseto ?

    amount_monsters = int(input())
    i = 0
    while i < amount_monsters:  # While pode ser melhor
        machines = {}
        machines_parts = {}
        monster = []
        machines_combat = int(input())        # lista é melhor
        critics = []
        for perfil in range(machines_combat):
            machine_details = input().split(sep=" ")
            machines[perfil] = machine_details
            li = {}
            critics.append(li)
            # maquinas {machines(número): [live_points, attack_points, parts_quant]}
            for _ in range(machines[perfil][machine_details][2]):
                body_part, weakness, max_damage, x_coordenate, y_coordenate = input().split(sep=", ")
                machines_parts[body_part] = [weakness, max_damage, (x_coordenate, y_coordenate)]
                monster.append(machines_parts)
                li[machines_parts[body_part][2]] = 0
                # parts {body_part: [weaknees, max_damage, (x_coordenate, y_coordenate)]}

        while True:
            target, body_part, arrow_type, fx, fy = input().split(sep=", ")
            print("Combate", i, ", vida =", aloy_life_points)

            # aloy_attack(target, body_part, arrow_type, fx, fy)
            damage, critics, arrows_listing = aloy_attack(target, body_part, machines, machines_parts, monster, arrows, arrow_type, int(fx), int(fy))
            machines[target][0] -= damage
            machines[target][0] = max(0, machines[target][0])
            if machines[target][0] == 0:
                print("Máquina", target, "derrotada.")
                break

            #  retirar as maquinas que aloy matou
            if monster == []:
                print("Aloy provou seu valor e voltou para sua tribo.")
                break
            aloy_life_points, aloy_alive = machines_attack(aloy_life_points, machines)
            if not aloy_alive:
                print("Aloy foi derrotada em combate e não retornará a tribo.")
                break
            aloy_life_points += max_life // 2
            aloy_life_points = min(aloy_life_points, max_life)
        i += 1
        
        # chamar foco
        # chamar ataque aloy
        # chamar ataque maquinas
        # chamar living

        # aloy_set = {}
        # aloy_set[target] = [body_part, arrow_type, (fx, fy)]
        # aloy_set = {} # aloy = {max_life, arrows, aloy_set}
        # monster.append(machines)


# def focus(arrows, machines_parts):
#     critic_point = False
#     aloy_arrows = arrows.keys()
#     machines_body = machines_parts.keys()
#     for arrow in aloy_arrows:
#         if arrow in machines_body:
#             critic_point = True
#             return arrow, critic_point

#     # averiguar os pontos perdidos pelas maquinas, fraqueza
#     return None, critic_point
# def renew_life(max_life, aloy_life_points, machines):
#     life, alive = machines_attack(aloy_life_points, machines)
#     if alive:
#         life += max_life / 2
#         life = min(max_life, life)
#     return life