def damage(max_damage, cx, fx, cy, fy):
    # same type of arrow
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
    pass


def living():
    pass


def attack():
    pass


def main():
    max_lives = int(input())
    arrow_amount = [input(sep=" ")]
    arrows = {}
    for i in arrow_amount:
        if i % 2 == 0:
            arrows[arrow_amount[i]] = arrow_amount[i+1]
    aloy = {max_lives, arrows}
    amount_monsters = int(input())
    machines_combat = int(input())
    machines = {}
    for i in range(machines_combat):
        # lista é melhor
        machine_details = input(sep=" ")
        machines[i] = {}
        machines[i][machine_details]
        # um dicionário {machines(número): [live_points, attack_points, parts_quant]}
        for _ in range(machines[i][machine_details][2]):
            body_part, weaknees, max_damage, x_coordenate, y_coordenate = input().split(sep=", ")
            machines[i][machine_details][body_part] = [weaknees, max_damage, x_coordenate, y_coordenate]
            # parts {body_part: [weaknees, max_damage, (x_coordenate, y_coordenate)]}
        target, body_part, arrow_type, fx, fy = input().split(sep=", ")
        # chamar ataque aqui




# Provavelmente vou ter que chamar os ataques na main dentro de cada for.