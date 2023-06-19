#  Link nas masmorras de Hyrule.

class Link:
    def __init__(self, life, damage, position, alive):
        self._life = life
        self._damage = damage
        self._position = position
        self._alive = alive

    def walking_right(self):
        self._position = (self._position[0], self._position[1] + 1)

    def walking_left(self):
        self._position = (self._position[0], self._position[1] - 1)

    def walking_up(self):
        self._position = (self._position[0] + 1, self._position[1])

    def walking_down(self):
        self._position = (self._position[0] - 1, self._position[1])

    def walking(self, dungeon):
        # call 'create_room'
        if self._position[0] % 2 == 0:
            if (self._position[1] + 1) < len(dungeon[0]):
                self._position = (self._position[0], self._position[1] - 1)
            elif (self._position[1]) == len(dungeon[0]) - 1 and self._position[0] != 0:
                self._position = (self._position[0] + 1, self._position[1])
        elif self._position[0] % 2 != 0:
            if (self._position[1] - 1) >= 0:
                self._position = (self._position[0], self._position[1] - 1)
            elif self._position[1] == 0 and self._position[0] != 0:
                self._position = (self._position[0] + 1, self._position[1])
        return self._position

        # primeiro ele desce até a última linha

    def living(self):
        if self._life == 0:
            self._alive = False
        elif self._life > 0:
            self._alive = True
        return self._alive

    def combat(self):
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
        for L in range(self._lines):
            line = []
            for C in range(self._columns):
                if (L, C) == link.position:
                    if Link.alive:  # confirmar a sintaxe
                        line.append('P')
                    else:
                        line.append('X')
                elif (L, C) == Room.exit:
                    line.append('*')
                # igual a posição do monstro
                elif position_details[(L, C)][0] != []:
                    # averiguar o tipo para imprimir a letra correspondente
                    line.append(position_details[(L, C)][0][len(position_details[L, C][0]) - 1][(L, C)][2])
                elif position_details[(L, C)][1] != []:
                    line.append(position_details[(L, C)][1][len(position_details[L, C][1]) - 1][(L, C)][2])
                else:
                    line.append('.')
            room.append(line)
        stamp_room(room)

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

    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, o_name):
    #     self._name = o_name

    # @property
    # def type(self):
    #     return self._type

    # @type.setter
    # def type(self, o_type):
    #     self._type = o_type

    # @property
    # def position(self):
    #     return self._position

    # @position.setter
    # def position(self, o_position):
    #     self._position = o_position

    # @property
    # def status(self):
    #     return self._status

    # @status.setter
    # def status(self, o_status):
        self._status = o_status

def main():
    initial_life, initial_damage = input().split()
    lines, columns = input().split()
    link_position = tuple([int(i) for i in input().split(',')])
    exit_position = tuple([int(i) for i in input().split(',')])

    position_details = {}  # {position: [[mons, mons, ...], [obj, obj, ... ]]}
    for L in range(lines - 1):
        for C in range(columns - 1):
            position_details[(L, C)] = [[], []]

    monster_details = []  # [[vida, ataque, tipo, posição], [...], ...]
    monster_amount = int(input())
    for _ in range(monster_amount):
        m_life, m_attack, m_type, m_position = input().split()
        m_position = tuple([int(i) for i in m_position.split(',')])
        monster_details.append(Monster(int(m_life), int(m_attack), m_type, m_position))

        monster_in_position = {}
        monster_in_position[m_position] = [int(m_life), int(m_attack), m_type, m_position]
        position_details[m_position][0].append(monster_in_position)
        # perhaps save it by the position, it could help get details better when needed.

    object_details = []  # [[nome, tipo, posição, status], [...], ...]
    object_amount = int(input())
    for _ in range(object_amount):
        o_name, o_type, o_position, o_status = input().split()
        o_position = tuple([int(i) for i in o_position.split(',')])
        object_details.append(Object(o_name, o_type, o_position, int(o_status)))

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