def damage(max_damage, cx, fx):
    # same type of arrow
    if (cx - fx) < 0:
        x = (-1)*(cx - fx)
    elif (cx - fx) >= 0:
        x = (cx - fx)
    if (cy - fy) < 0:
        y = (-1)*(cy - fy)
    if (cy - fy) >= 0:
        y = (cy - fy)
    damage = max_damage - (x + y)
    # build for different types of arrows
    return damage


def main():
    aloy_max_lives = int(input())
    arrow_amount = [input(sep=" ")]
    arrows  = {}
    for i in arrow_amount:
        if i % 2 == 0:
            arrows = {arrow_amount[i]: arrow_amount[i+1]}
    amount_monsters = int(input())
    machines = int(input())
    for _ in range(machines):
        # lista é melhor
        live_points, attack_points, parts_quant = input(sep=" ")
        # um dicionário {machines(número): [live_points, attack_points, parts_quant]}
        for _ in range(parts_quant):
            body_part, weaknees, max_damage, x_coordenate, y_coordenate = input(sep=", ")
            # parts {body_part: [weaknees, max_damage, (x_coordenate, y_coordenate)]}
        target, body_part, arrow_type, fx, fy = input(sep=", ")
    # confuso a parte final da entrada