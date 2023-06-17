#  Link nas masmorras de Hyrule.

class Link:
    def __init__ (self, life, damage, position, alive):
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
    
    def combat(self,):
        pass
        # it only happens once per position.

    def collect_object(self, ):
        pass
    # Link must first collect the object in the position 
    # he's in and then fight the existing monsters there.


class Room:
    def __init__ (self, lines, columns, exit):
        self._lines = lines
        self._columns = columns
        self._exit = exit

    def create_room(self, stamp_room, link, exit):
        room = []
        for l in range(Room.lines):
            line = []
            for c in range(Room.columns):
                if (l, c) == link.position:
                    line.append('P')
                elif (l, c) == Room.exit:
                    line.append('*')
                # igual a posição do monstro
                elif (l, c) == monster:
                    # averiguar o tipo para imprimir a letra correspondente
                    line.append('')
                else:
                    line.append('.')
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


class Monster:
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
    link_position= input()
    exit_position = input()
    link_alive = True
    link = Link(int(initial_life), int(initial_damage), link_position, link_alive)  # link = [vida inicial, dano inicial, posição]
    dungeon = Room(lines, columns, exit_position)
    

    # monster = []
    monster_details = {}  # {monstro: [vida, ataque, tipo, posição]}
    monster_amount = int(input())
    for i in range(monster_amount):
        m_life, m_attack, m_type, m_position = input().split()
        monster_details[i] = [int(m_life), int(m_attack), m_type, m_position]
        # perhaps save it by the position, it could help get details better when needed.

    object_details = {}  # {nome: [tipo, posição, status]}
    object_amount = int(input())
    for i in range(object_amount):
        o_name, o_type, o_position, o_status = input().split()
        object_details[o_name] = [o_type, o_position, o_status]
        # salvar por posição, deve ser mais fácil checar

    # I DONT KNOW HOW TO EXACTLY CALL THE SHOTS HERE
    # Link must attack first.
    # Link must walk first than the monsters


    






# f = Link(2, 10, (2, 2), (4, 5))

Room.stam_room()

if __name__ == "__main__":
    main()
