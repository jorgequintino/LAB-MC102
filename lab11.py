#  Link nas masmorras de Hyrule.

class Link:
    ''' Classe referente ao objeto Link.
        '''
    def __init__(self, life, damage, position, alive):
        ''' Inicia os parâmetros da classe Link.
            '''
        self._life = life
        self._damage = damage
        self._position = position
        self._alive = alive

    def walking_right(self):
        ''' Movimenta o personagem Link para a direita.
        Parâmetros:
        argumentos:
            self (class)
        retorno:
            None
            '''
        self.position = (self.position[0], self.position[1] + 1)

    def walking_left(self):
        ''' Movimenta o personagem Link para a esquerda.
        Parâmetros:
        argumentos:
            self (class)
        retorno:
            None
            '''
        self.position = (self.position[0], self.position[1] - 1)

    def walking_up(self):
        ''' Movimenta o personagem Link para cima.
        Parâmetros:
        argumentos:
            self (class)
        retorno:
            None
            '''
        self.position = (self.position[0] - 1, self.position[1])

    def walking_down(self):
        ''' Movimenta o personagem Link para baixo.
        Parâmetros:
        argumentos:
            self (class)
        retorno:
            None
            '''
        self.position = (self.position[0] + 1, self.position[1])

    def walking(self, dungeon):
        ''' Movimenta o mostro de acordo com as limitações dadas
        pela estrutura da masmorra. Nela, ele apenas pode se mover
        para cima, para a esquerda caso esteja em linha par e para
        a direita caso esteja em linha ímpar.
        Parâmetros:
        argumentos:
            self (class)
            dungeon (class)
        retorno:
            None
            '''
        if self.position[0] % 2 == 0:
            if (self.position[1] - 1) >= 0:
                self.walking_left()
            elif self.position[1] == 0 and self.position[0] != 0:
                self.walking_up()
        elif self.position[0] % 2 != 0:
            if (self.position[1] + 1) < dungeon.columns:
                self.walking_right()
            elif (self.position[1]) == dungeon.columns - 1 and self.position[0] != 0:
                self.walking_up()

    def living(self):
        ''' Averigua se Link está vivo de acordo com
        o valor de sua vida.
        Parâmetros:
        argumentos:
            self (class)
        retorno:
            self.alive (bool)
            '''
        if self.life == 0:
            self.alive = False
        else:
            self.alive = True
        return self.alive

    def collect_object(self, objects):
        ''' Para cada posição verifica se há objetos, e em caso
        de existẽncia, link os absorve. Essa ação tem consequência
        nos parametros de Link mediante o tipo de objeto absorvido.
        Para o objeto "v", há alteração da pontuação da vida de link,
        já para o tipo "d", seu dano é alterado. Retorna então a lista
        atualizada de objetos na masmorra e se Link está vivo.
        Parâmetros:
        argumentos:
            self (class)
            objects (list)
        retorno:
            objects (list)
            self.alive (bool)
            '''
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
        ''' Para cada posição verifica se há monstros, e em caso
        de existẽncia, link combate-os de acordo com a ordem de inserção
        na posição. Link é o primeiro a atacar, e caso sobreviva recebe o
        ataque do monstro. Na possibilidade de existência de mais de um
        monstro na posição esse processo se repete. Retorna então a lista
        atualizada de monstros na masmorra e se Link está vivo.
        Parâmetros:
        argumentos:
            self (class)
            monsters (list)
        retorno:
            monsters (list)
            self.alive (bool)
            '''
        dead_monsters = []
        for monster in monsters:
            if self.position == monster.position:
                m_death_value = monster.life
                monster.life -= self.damage
                monster.life = max(0, monster.life)
                monster.alive = monster.living()
                if monster.alive:
                    print("O Personagem deu ", self.damage, " de dano ao monstro na posicao ", self.position, sep='')
                    l_death_value = self.life
                    self.life -= monster.attack
                    self.life = max(0, self.life)
                    self.alive = self.living()
                    if self.alive:
                        print("O Monstro deu ", monster.attack, " de dano ao Personagem. Vida restante = ", self.life, sep='')
                    else:
                        print("O Monstro deu ", l_death_value, " de dano ao Personagem. Vida restante = ", self.life, sep='')
                        break
                else:
                    print("O Personagem deu ", m_death_value, " de dano ao monstro na posicao ", self.position, sep='')
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
    ''' Classe referente ao objeto Room (masmorras).
        '''
    def __init__(self, lines, columns, exit):
        ''' Inicia os parâmetros da classe Room.
            '''
        self._lines = lines
        self._columns = columns
        self._exit = exit

    def create_room(self, stamp_room, monsters, link, objects):
        ''' De acordo com a linhas e colunas, cria uma matriz de pontinhos para
        representar a masmorra. Coloca posteriormente nela os atifícios do jogo
        pela ordem de prioridade, sendo do menos prioritário para o mais
        (objetos, monstros, saída e personagem). Por fim, chama a função "stamp_room"
        responsável por imprimir a sala e retorna por meio de uma booleana se
        link está na posição de saída.
        Parâmetros:
        argumentos:
            self (class)
            stamp_room ()
            monsters (list)
            link (class)
            objects (list)
        retorno:
            end (bool)
            '''
        left_dungeon = False
        room = []
        for _ in range(self.lines):
            line = []
            for _ in range(self.columns):
                line.append('.')
            room.append(line)

        created = False
        while not created:

            for o in objects:
                room[o.position[0]][o.position[1]] = o.type

            for m in monsters:
                room[m.position[0]][m.position[1]] = m.type

            room[self.exit[0]][self.exit[1]] = "*"

            if link.alive:
                room[link.position[0]][link.position[1]] = "P"
                if link.position == self.exit:
                    left_dungeon = True
                created = True
            else:
                room[link.position[0]][link.position[1]] = "X"
                left_dungeon = True
                created = True
        stamp_room(room)
        return left_dungeon

    def stamp_room(self, room):
        ''' Imprime a sala criada.
        Parâmetros:
        argumentos:
            self (class)
            room (list)
        retorno:
            None
            '''
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
    ''' Classe referente ao objeto monstro.
        '''
    def __init__(self, life, attack, type, position, alive):
        ''' Inicia os parâmetros da classe monstro.
            '''
        self._life = life
        self._attack = attack
        self._type = type
        self._position = position
        self._alive = alive

    def walking_right(self):
        ''' Movimenta o mostro para a direita.
        Parâmetros:
        argumentos:
            self (class)
        retorno:
            None
            '''
        self.position = (self.position[0], self.position[1] + 1)

    def walking_left(self):
        ''' Movimenta o mostro para a esquerda.
        Parâmetros:
        argumentos:
            self (class)
        retorno:
            None
            '''
        self.position = (self.position[0], self.position[1] - 1)

    def walking_up(self):
        ''' Movimenta o mostro para cima.
        Parâmetros:
        argumentos:
            self (class)
        retorno:
            None
            '''
        self.position = (self.position[0] - 1, self.position[1])

    def walking_down(self):
        ''' Movimenta o mostro para baixo.
        Parâmetros:
        argumentos:
            self (class)
        retorno:
            None
            '''
        self.position = (self.position[0] + 1, self.position[1])

    def walking(self, dungeon):
        ''' Movimenta o mostro de acordo com as limitações dadas
        pelo o tipo do monstro.
        Parâmetros:
        argumentos:
            self (class)
            dungeon (class)
        retorno:
            None
            '''
        if self.type == "U":
            if self.position[0] != 0:
                self.walking_up()
        elif self.type == "D":
            if self.position[0] != dungeon.lines - 1:
                self.walking_down()
        elif self.type == "L":
            if self.position[1] != 0:
                self.walking_left()
        elif self.type == "R":
            if self.position[1] != dungeon.columns - 1:
                self.walking_right()

    def living(self):
        ''' Averigua se o monstro está vivo de acordo com
        o valor de sua vida.
        Parâmetros:
        argumentos:
            self (class)
        retorno:
            self.alive (bool)
            '''
        if self.life == 0:
            self.alive = False
        else:
            self.alive = True
        return self.alive

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
    ''' Classe referente aos objetos da classe Objeto.
        '''
    def __init__(self, name, type, position, status):
        ''' Inicia os parâmetros da classe objeto.
            '''
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
    left_dungeon = False

    left_dungeon = dungeon.create_room(dungeon.stamp_room, monster_details, link, object_details)

    while beginning:

        if link.position[0] != dungeon.lines - 1:

            link.walking_down()
            for monster in monster_details:
                monster.walking(dungeon)

            if link.position != dungeon.exit:
                object_details, link_alive = link.collect_object(object_details)
                monster_details, link_alive = link.combat(monster_details)
                left_dungeon = dungeon.create_room(dungeon.stamp_room, monster_details, link, object_details)
            else:
                beginning = False
                left_dungeon = dungeon.create_room(dungeon.stamp_room, monster_details, link, object_details)

            if not link_alive:
                beginning = False
                left_dungeon = True

        else:
            beginning = False

    while not left_dungeon:

        link.walking(dungeon)
        for monster in monster_details:
            monster.walking(dungeon)

        if link.position != dungeon.exit:
            object_details, link_alive = link.collect_object(object_details)
            monster_details, link_alive = link.combat(monster_details)
            left_dungeon = dungeon.create_room(dungeon.stamp_room, monster_details, link, object_details)
        else:
            left_dungeon = dungeon.create_room(dungeon.stamp_room, monster_details, link, object_details)

    if left_dungeon:
        if link_alive:
            print("Chegou ao fim!")


if __name__ == "__main__":
    main()
