def damage(machines): # tá nesse dicionário
    # same type of arrow
    keys = machines.keys()
    machines[m][machine_details][body_part]
    if (cx - fx) < 0:
        x = (-1)*(cx - fx)
    elif (cx - fx) >= 0:
        x = (cx - fx)
    if (cy - fy) < 0:
        y = (-1)*(cy - fy)
    elif (cy - fy) >= 0:
        y = (cy - fy)
    damage = max_damage - (x + y)
    # build for different types of arrows
    return damage


def foco():
    #averiguar os pontos perdidos pelas maquinas, fraqueza
    pass


def life_points():
    # perde o os pontos de ataque



def living(max_lives):
    # chamar life points e somar com extra
    extra_lives = max_lives / 2

    pass


def attack():
    # chamar damage
    # chamar life_points
    pass


def main():
    max_lives = int(input())
    arrow_amount = [input(sep=" ")]
    arrows = {}
    for i in range(len(arrow_amount)):
        if i % 2 == 0:
            arrows[arrow_amount[i]] = arrow_amount[i+1]

    amount_monsters = int(input())
    machines = {}
    machines_parts = {}
    aloy_attack = {}
    monster = []
    for i in range(amount_monsters): # While pode ser melhor
        machines_combat = int(input())        # lista é melhor
        for m in range(machines_combat):
            machine_details = input(sep=" ")
            machines[m] = {}
            machines[m][machine_details]
            # um dicionário {machines(número): [live_points, attack_points, parts_quant]}
            for _ in range(machines[m][machine_details][2]):
                body_part, weaknees, max_damage, x_coordenate, y_coordenate = input().split(sep=", ")
                machines_parts[body_part] = [weaknees, max_damage, (x_coordenate, y_coordenate)]
                # parts {body_part: [weaknees, max_damage, (x_coordenate, y_coordenate)]}
        monster.append(machines)
        monster.append(machines_parts)
        target, body_part, arrow_type, fx, fy = input().split(sep=", ")
        aloy = {max_lives, arrows}

        # chamar foco
        # chamar ataque aqui
        # chamar living




# Provavelmente vou ter que chamar os ataques na main dentro de cada for.