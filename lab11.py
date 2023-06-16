#  Link nas masmorras de Hyrule.


def main():
    vp, vd = input().split()
    line, column = input().split()
    x_link, y_link = input().split()
    x_out, y_out = input().split()
    link = [int(vp), int(vd), (int(x_link), int(y_link)), (int(x_out), int(y_out))]
    # link = [vida inicial, dano inicial, posição, saída]

    # monster = []
    monster_details = {}  # {monstro: [vida, ataque, tipo, posição]}
    monster_amount = int(input())
    for i in range(monster_amount):
        m_life, m_attack, m_type, x_m, y_m = input().split()
        monster_details[i] = [int(m_life), int(m_attack), m_type, (int(x_m), int(y_m))]

    object_details = {}  # {nome: [tipo, posição, status]}
    object_amount = int(input())
    for i in range(object_amount):
        o_name, o_type, x_o, y_o, o_status = input().split()
        object_details[o_name] = [o_type, (int(x_o), int(y_o)), o_status]








if __name__ == "__main__":
    main()
