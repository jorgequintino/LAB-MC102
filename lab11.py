#  Link nas masmorras de Hyrule.

class Link:
    def __init__ (self, life, damage, position):
        self.life = life
        self.damage = damage
        self.position = position


    def walking():
        pass
        # primeiro ele desce até a última linha

    
    def combat():
        pass
        # it only happens once per position.

    def collect_object():
        pass
    # Link must first collect the object in the position 
    # he's in and then fight the existing monsters there.


class Room:
    def __init__ (self, lines, columns, exit):
        self._lines = lines
        self._columns = columns
        self._exit = exit

    def create_room(self, stamp_room):
        room = []
        for _ in range(Room.lines):
            line = []
            for _ in range(Room.columns):
                line.append(".")
            room.append(line)
        return stamp_room(room)
   
    def stamp_room (self, room):
        for room_line in range(len(room)):
            print(*room[room_line])
        print()

    @property
    def lines(self):
        return self._lines
    
    @lines.setter
    def lines(self, lines):
        self._lines = lines

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def column(self, columns):
        self._columns = columns

    @property
    def exit(self):
        return self.exit

    @exit.setter
    def exit(self, exit):
        self._exit = exit


class monster:
    def __init__(self, monster_details):
        self.name = monster_details[]
        self.life = monster_details[][0]
        self.damage = monster_details[][2]

    def walking():
        pass # if it wants to walk past the room, it must stay still.


class object:
    def __init__(self, object_details):
        self.name = object_details.keys()


def main():
    initial_life, initial_damage = input().split()
    lines, columns = input().split()
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

    # Link must attack first.











f = Link(2, 10, (2, 2), (4, 5))

Room.stam_room()

if __name__ == "__main__":
    main()
