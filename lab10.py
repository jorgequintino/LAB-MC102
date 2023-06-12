def damage(machines_parts, arrows, fx, fy):  # tá nesse dicionário
    # same type of arrow
    arrow_critic, critic_point = focus(arrows, machines_parts)
    keys = machines_parts.keys()
    for k in keys:
        damage = machines_parts[k][1] - (abs(cx - fx) + abs(cy - fy)) # cx e fx

    # build for different types of arrows
    return damage


def focus(arrows, machines_parts):
    critic_point = False
    aloy_arrows = arrows.keys()
    machines_body = machines_parts.keys()
    for arrow in aloy_arrows:
        if arrow in machines_body:
            critic_point = True
            return arrow, critic_point

    # averiguar os pontos perdidos pelas maquinas, fraqueza
    return None, critic_point


def machines_attack(aloy_life_points, machines):
    aloy_alive = True
    keys = machines.keys()
    for k in keys:
        aloy_life_points -= machines[k][1]
        aloy_life_points = max(0, aloy_life)
        if aloy_life_points == 0:
            aloy_life_points = False
            return aloy_life_points, aloy_alive

    return aloy_life_points, aloy_alive


def renew_life(max_life, aloy_life, machines):
    life, alive = machines_attack(aloy_life, machines)
    if alive:
        life += life + max_life / 2
        life = min(max_life, life)
    return life


# def machines_attack():
#     # chamar life_points
#     pass


def aloy_attack(target, body_part, arrow_type, fx, fy):
    attack_point = (fx, fy)

    # chamar damage
    pass


def main():
    aloy_life_points = max_life = int(input())
    arrow_amount = [input(sep=" ")]
    arrows = {}
    for i in range(len(arrow_amount)):
        if i % 2 == 0:
            arrows[arrow_amount[i]] = int(arrow_amount[i + 1])

    amount_monsters = int(input())
    machines = {}
    machines_parts = {}
    # aloy_set = {}
    monster = []
    for i in range(amount_monsters):  # While pode ser melhor
        machines_combat = int(input())        # lista é melhor
        for m in range(machines_combat):
            machine_details = input(sep=" ")
            machines[m] = machine_details
            # maquinas {machines(número): [live_points, attack_points, parts_quant]}
            for _ in range(machines[m][machine_details][2]):
                body_part, weakness, max_damage, x_coordenate, y_coordenate = input().split(sep=", ")
                machines_parts[body_part] = [weakness, max_damage, (x_coordenate, y_coordenate)]
                monster.append(machines_parts)
                # parts {body_part: [weaknees, max_damage, (x_coordenate, y_coordenate)]}
        while True:
            target, body_part, arrow_type, fx, fy = input().split(sep=", ")
            arrow, critic_point = focus(arrows, machines_parts)
            aloy_attack(target, body_part, arrow_type, fx, fy)
            aloy_life_points, aloy_alive = machines_attack(aloy_life_points, machines)
            if not aloy_alive:
                print("fnmjfvkfdvkfd") 
        


        # chamar foco
        # chamar ataque aloy
        # chamar ataque maquinas
        # chamar living



        # aloy_set[target] = [body_part, arrow_type, (fx, fy)]
        # aloy = {max_life, arrows, aloy_set}
        # monster.append(machines)
