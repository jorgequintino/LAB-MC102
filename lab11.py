#  Link nas masmorras de Hyrule.

class Link:
    def __init__ (self, life, damage, position):
        self.life = life
        self.damage = damage
        self.position = position


class Room:
    def __init__ (self, line, column, exit):
        self._line = line
        self._column = column
        self._exit = exit

    @property
    def line(self):
        return self._line

    @line.setter
    def line(self, line):
        self._line = line

    @property
    def column(self):
        return self._column

    @column.setter
    def column(self, column):
        self._column = column

    @property
    def exit(self):
        return self.exit

    @exit.setter
    def exit(self, exit):
        self._exit = exit

    def stamp_room (self):
        pass


class monster:
    def __init__(self, monster_details):
        self.name = monster_details[]
        self.life = monster_details[key][0]
        self.damage = monster_details[][2]



def main():
    initial_life, initial_damage = input().split()
    line, column = input().split()
    position_link= input()
    exit_position = input()
    link = [int(initial_life), int(initial_damage), position_link, exit_position]
    # link = [vida inicial, dano inicial, posição, saída]

    # monster = []
    monster_details = {}  # {monstro: [vida, ataque, tipo, posição]}
    monster_amount = int(input())
    for i in range(monster_amount):
        m_life, m_attack, m_type, m_position = input().split()
        monster_details[i] = [int(m_life), int(m_attack), m_type, m_position]

    object_details = {}  # {nome: [tipo, posição, status]}
    object_amount = int(input())
    for i in range(object_amount):
        o_name, o_type, o_position, o_status = input().split()
        object_details[o_name] = [o_type, o_position, o_status]
    
    f = Link(2, 10, (2, 2), (4, 5))

    Room.stam_room()







if __name__ == "__main__":
    main()
