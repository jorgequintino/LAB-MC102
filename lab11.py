#  Link nas masmorras de Hyrule.

class Link:
    def __init__(self, life, damage, position, alive):
        self.life = life
        self.damage = damage
        self.position = position
        self.alive = alive

    def walking_right(self, position):
        return (position[0], position[1] + 1)

    def walking_left(self, position):
        return (position[0], position[1] - 1)

    def walking_up(self, position):
        return (position[0] + 1, position[1])

    def walking_down(self, position):
        return (position[0] - 1, position[1])

    def walking(self, position, dungeon):
        # call 'create_room'
        if position[0] % 2 == 0:
            if (position[1] + 1) < len(dungeon[0]):
                position = (position[0], position[1] - 1)
            elif (position[1]) == len(dungeon[0]) - 1 and position[0] != 0:
                position = (position[0] + 1, position[1])
        elif position[0] % 2 != 0:
            if (position[1] - 1) >= 0:
                position = (position[0], position[1] - 1)
            elif position[1] == 0 and position[0] != 0:
                position = (position[0] + 1, position[1])
        return position

        # primeiro ele desce até a última linha

    def living(self, life, alive):
        if life == 0:
            alive = False
        elif life > 0:
            alive = True
        return alive

    def combat(self, ):
        pass
        # it only happens once per position.

    def collect_object(self, ):
        pass
    # Link must first collect the object in the position
    # he's in and then fight the existing monsters there.


class Room:
    def __init__(self, lines, columns, exit, position_details):
        self._lines = lines
        self._columns = columns
        self._exit = exit
        self._details = position_details

    def create_room(self, stamp_room, link, position_details):
        room = []
        for L in range(Room.lines):
            line = []
            for C in range(Room.columns):
                if (L, C) == link.position:
                    line.append('P')
                elif (L, C) == Room.exit:
                    line.append('*')
                # igual a posição do monstro
                elif position_details[L, C][0] != []:
                    # averiguar o tipo para imprimir a letra correspondente
                    line.append(position_details[(L, C)][0][len(position_details[L, C][0]) - 1][(L, C)][2])
                else:
                    line.append('.')
            room.append(line)
        return stamp_room(room)

    def stamp_room(self, room):
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


class Monster:
    def __init__(self, monster_details):
        # [vida, ataque, tipo, posição]
        for name in monster_details:
            self.name = name
            self._life = monster_details[name][0]
            self.attack = monster_details[name][1]
            self.type = monster_details[name][2] 
            self.position = monster_details[name][3]

    def walking():
        pass # if it wants to walk past the room, it must stay still.

        # MAYBE SET SELF ON INPUT
    def living(self, ):
        if life == 0:
            alive = False
        elif life > 0:
            alive = True
        return alive
        pass


class Object:
    def __init__(self, o_name, o_type, o_position, o_status):
        self._name = o_name
        self._type = o_type
        self._position = o_position
        self._status = o_status

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, o_name):
        self._name = o_name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, o_type):
        self._type = o_type

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, o_position):
        self._position = o_position

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, o_status):
        self._status = o_status

def main():
    initial_life, initial_damage = input().split()
    lines, columns = input().split()
    link_position = input()
    exit_position = input()

    position_details = {}  # {position: [[mons, mons, ...], [obj, obj, ... ]]}
    for l in range(lines - 1):
        for c in range(columns - 1):
            position_details[(l, c)] = [[], []]

    monster_details = {}  # [[vida, ataque, tipo, posição], [...], ...]
    monster_amount = int(input())
    for i in range(monster_amount):
        m_life, m_attack, m_type, m_position = input().split()
        monster_details[i] = Monster(int(m_life), int(m_attack), m_type, m_position)
        # monster_details.append(m_details)

        monster_in_position = {}
        monster_in_position[m_position] = [int(m_life), int(m_attack), m_type, m_position]
        position_details[m_position][0].append(monster_in_position)
        # perhaps save it by the position, it could help get details better when needed.

    object_details = {}  # [[nome, tipo, posição, status], [...], ...]
    object_amount = int(input())
    for i in range(object_amount):
        o_name, o_type, o_position, o_status = input().split()
        object_details[i] = Object(o_name, o_type, o_position, int(o_status))
        # o_details =[o_name, o_type, o_position, o_status]
        # object_details.append(o_details)

        object_in_position = {}
        object_in_position[o_position] = [o_name, o_type, o_status]
        position_details[m_position][1].append(object_in_position)
        # salvar por posição, deve ser mais fácil checar


    link_alive = True
    link = Link(int(initial_life), int(initial_damage), link_position, link_alive)
    # link = [vida inicial, dano inicial, posição]
    dungeon = Room(lines, columns, exit_position, position_details)
    monster = Monster(monster_details)

    # I DONT KNOW HOW TO EXACTLY CALL THE SHOTS HERE
    # Link must attack first.
    # Link must walk first than the monsters


    






# f = Link(2, 10, (2, 2), (4, 5))

# Room.stam_room()

if __name__ == "__main__":
    main()
