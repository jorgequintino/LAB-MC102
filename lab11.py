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

    def collect_object(self, objects):
        for object in objects:
            if self._position == object._position:
                if object._type == "v":
                    self._life += object._status
                    self._life = max(0, self._life)
                    self._alive = self.living(self)
                    if not self._alive:
                        # print()
                        # do the things of a dead body
                elif object._type == "d":
                    self._damage += object._status
                    self._damage = max(1, self._damage)
                    print([d]Personagem adquiriu o objeto joia com status de 2)
    # Link must first collect the object in the position
    # he's in and then fight the existing monsters there.
    
    def combat(self, monsters):
            dead_monsters = []
            for index, monster in enumerate(monsters):
                if self._position == monster._position:
                    monster._life -= self._damage
                    monster._alive = monster.living(monster)
                    if monster._alive:
                        self._life -= monster._attack
                        self._life = max(0, self._life)
                        self._alive = self.living(self)
                    elif not monster._alive:
                        dead_monsters.append(index)
                if not self._alive:
                    # fazer as coisas da morte de P
                    break
            for dead_index in dead_monsters:
                del monster[dead_index]
            # it only happens once per position.

class Room:
    def __init__(self, lines, columns, exit):
        self._lines = lines
        self._columns = columns
        self._exit = exit

    def create_room(self, stamp_room, link, monster_details, object_details):
        room = []
        for L in range(self._lines):
            line = []
            for C in range(self._columns):
                line.append('.')
            room.append(line)

        created = False
        while not created:
                
            for o in object_details:
                room[o._position[0]][o._position[1]] = o._type

            for m in monster_details:
                room[m._position[0]][m._position[1]] = m._type

            room[self._exit[0]][self._exit[1]] = "*"

            if link._alive:
                room[link._position[0]][link._position[1]] = "P"
                created = True
            elif not link._alive:
                room[link._position[0]][link._position[1]] = "X"
                created = True
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
    def __init__(self, life, attack, type, position, alive):
        self._life = life
        self._attack = attack
        self._type = type
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
        if self._type == "U":
            if self._position[0] != 0:
                Monster.walking_up(self)
        if self._type == "D":
            if self._position[0] != dungeon._lines - 1:  # problema
                Monster.walking_down(self)
        if self._type == "L":
            if self._position[1] != 0:
                Monster.walking_left(self)
        if self._type == "R":
            if self._position[1] != dungeon._columns - 1:
                Monster.walking_left(self)
        return self._position

    def living(self):
        if self._life == 0:
            self._alive = False
        elif self._life > 0:
            self._alive = True
        return self._alive


class Object:
    def __init__(self, o_name, o_type, o_position, o_status):
        self._name = o_name
        self._type = o_type
        self._position = o_position
        self._status = o_status

def main():
    initial_life, initial_damage = input().split()
    lines, columns = input().split()
    link_position = tuple([int(i) for i in input().split(',')])
    exit_position = tuple([int(i) for i in input().split(',')])

    monster_details = []  # [[vida, ataque, tipo, posição], [...], ...]
    monster_amount = int(input())
    for _ in range(monster_amount):
        m_life, m_attack, m_type, m_position = input().split()
        m_position = tuple([int(i) for i in m_position.split(',')])
        monster_alive = True
        monster_details.append(Monster(int(m_life), int(m_attack), m_type, m_position, monster_alive))

    object_details = []  # [[nome, tipo, posição, status], [...], ...]
    object_amount = int(input())
    for _ in range(object_amount):
        o_name, o_type, o_position, o_status = input().split()
        o_position = tuple([int(i) for i in o_position.split(',')])
        object_details.append(Object(o_name, o_type, o_position, int(o_status)))

    link_alive = True
    link = Link(int(initial_life), int(initial_damage), link_position, link_alive)
    dungeon = Room(lines, columns, exit_position)
    beginning = True
    
    while True:
        while beginning:
            if link._position[0] != dungeon._lines - 1:
                link.walking_down
                for m in monster_details:
                    m.walking
            elif link._position[0] == dungeon._lines - 1:
                beginning = False


        link.combat(monster_details)
        link.collect_object(object_details)


















# I DONT KNOW HOW TO EXACTLY CALL THE SHOTS HERE
# Link must attack first.
# Link must walk first than the monsters

# f = Link(2, 10, (2, 2), (4, 5))

# Room.stam_room()

if __name__ == "__main__":
    main()
