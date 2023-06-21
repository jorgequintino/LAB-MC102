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
        self._position = (self._position[0] - 1, self._position[1])

    def walking_down(self):
        self._position = (self._position[0] + 1, self._position[1])

    def walking(self, dungeon):
        if self._position[0] % 2 == 0:
            if (self._position[1] - 1) >= 0:
                self.walking_left()
            elif self._position[1] == 0 and self._position[0] != 0:
                self.walking_up()
        elif self._position[0] % 2 != 0:
            if (self._position[1] + 1) < dungeon.columns:
                self.walking_right()
            elif (self._position[1]) == dungeon.columns - 1 and self._position[0] != 0:
                self.walking_up()

    def living(self):
        if self._life == 0:
            self._alive = False
        elif self._life > 0:
            self._alive = True
        return self._alive

    def collect_object(self, objects):
        used_objects = []
        for object in objects:
            if self._position == object._position:
                if object._type == "v":
                    self._life += object._status
                    self._life = max(0, self._life)
                    self._alive = self.living()
                    used_objects.append(object)
                    print("[v]Personagem adquiriu o objeto ", object._name, " com status de ", object._status, sep='')
                elif object._type == "d":
                    self._damage += object._status
                    self._damage = max(1, self._damage)
                    used_objects.append(object)
                    print("[d]Personagem adquiriu o objeto ", object._name, " com status de ", object._status, sep='')

        for object in used_objects:
            objects.remove(object)
        return objects, self.alive

    def combat(self, monsters):
        dead_monsters = []
        for monster in monsters:
            if self._position == monster._position:
                monster._life -= self._damage
                print("O Personagem deu ", self._damage, " de dano ao monstro na posicao ", self._position, sep='')
                monster.life = max(0, monster.life)
                monster._alive = monster.living()
                if monster._alive:
                    self._life -= monster._attack
                    self._life = max(0, self._life)
                    print("O Monstro deu ", monster._attack, " de dano ao Personagem. Vida restante = ", self._life, sep='')
                    self._alive = self.living()
                elif not monster._alive:
                    dead_monsters.append(monster)
        for monster in dead_monsters:
            monsters.remove(monster)
        return monsters, self.alive

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, life):
        self._life = life

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, damage):
        self._damage = damage

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def alive(self):
        return self._alive

    @alive.setter
    def alive(self, alive):
        self._alive = alive

class Room:
    def __init__(self, lines, columns, exit):
        self._lines = lines
        self._columns = columns
        self._exit = exit

    def create_room(self, stamp_room, monster_details, link, object_details):
        end = False
        room = []
        for _ in range(self._lines):
            line = []
            for _ in range(self._columns):
                line.append('.')
            room.append(line)

        created = False
        while not created:

            for o in object_details:
                room[o._position[0]][o._position[1]] = o._type

            for m in monster_details:
                room[m._position[0]][m._position[1]] = m.type

            room[self._exit[0]][self._exit[1]] = "*"

            if link._alive:
                room[link._position[0]][link._position[1]] = "P"
                if link.position == self.exit:
                    end = True
                created = True
            elif not link._alive:
                room[link._position[0]][link._position[1]] = "X"
                end = True
                created = True
        stamp_room(room)
        return end

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
        return self._exit

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
        self._position = (self._position[0] - 1, self._position[1])

    def walking_down(self):
        self._position = (self._position[0] + 1, self._position[1])

    def walking(self, dungeon):
        if self._type == "U":
            if self._position[0] != 0:
                self.walking_up()
        elif self._type == "D":
            if self._position[0] != dungeon._lines - 1:
                self.walking_down()
        elif self._type == "L":
            if self._position[1] != 0:
                self.walking_left()
        elif self._type == "R":
            if self._position[1] != dungeon._columns - 1:
                self.walking_right()

    def living(self):
        if self._life == 0:
            self._alive = False
        elif self._life > 0:
            self._alive = True
        return self._alive

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, life):
        self._life = life

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, attack):
        self._attack = attack

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def alive(self):
        return self._alive

    @alive.setter
    def alive(self, alive):
        self._alive = alive

class Object:
    def __init__(self, name, type, position, status):
        self._name = name
        self._type = type
        self._position = position
        self._status = status

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def position(self):
        return self._position

    @property
    def status(self):
        return self._status

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
    dungeon = Room(int(lines), int(columns), exit_position)
    beginning = True
    end = False

    end = dungeon.create_room(dungeon.stamp_room, monster_details, link, object_details)
    while not end:

        while beginning:

            if link._position[0] != dungeon._lines - 1:
                link.walking_down()
                for monster in monster_details:
                    monster.walking(dungeon)
                object_details, link_alive = link.collect_object(object_details)
                monster_details, link_alive = link.combat(monster_details)
                end = dungeon.create_room(dungeon.stamp_room, monster_details, link, object_details)
                if not link_alive:
                    beginning = False
                    end = True
            elif link._position[0] == dungeon._lines - 1:
                beginning = False

        if not end:

            link.walking(dungeon)
            for monster in monster_details:
                monster.walking(dungeon)
            object_details, link_alive = link.collect_object(object_details)
            monster_details, link_alive = link.combat(monster_details)
            end = dungeon.create_room(dungeon.stamp_room, monster_details, link, object_details)
            # problema teste 5 para sair do loop

    if end:
        if link_alive:
            print("Chegou ao fim!")

#  se o Link está vivo, ataca
#  colocar apenas o dano necessário para matar link quando este morre




if __name__ == "__main__":
    main()