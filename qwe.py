from abc import ABC, abstractmethod


class GameObject(ABC):
    def __init__(self, object_id, name, x, y):
        self.object_id = object_id
        self.name = name
        self.x = x
        self.y = y

    def getId(self):
        return self.object_id

    def getName(self):
        return self.name

    def getX(self):
        return self.x

    def getY(self):
        return self.y


# Интерфейс для юнитов, которые могут атаковать
class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass


# Интерфейс для объектов, которые могут двигаться
class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass


# Класс для юнитов
class Unit(GameObject):
    def __init__(self, object_id, name, x, y, hp):
        super().__init__(object_id, name, x, y)
        self.hp = hp
        self.alive = True

    def isAlive(self):
        return self.alive

    def getHp(self):
        return self.hp

    def receiveDamage(self, damage):
        if self.hp > damage:
            self.hp -= damage
        else:
            self.hp = 0
            self.alive = False


# Класс для лучника
class Archer(Unit, Attacker, Moveable):
    def __init__(self, object_id, name, x, y, hp, damage):
        super().__init__(object_id, name, x, y, hp)
        self.damage = damage

    def attack(self, unit):
        if unit.isAlive():
            unit.receiveDamage(self.damage)
            print(f"{self.name} атакует {unit.getName()} и наносит {self.damage} урона.")

    def move(self, x, y):
        self.x = x
        self.y = y
        print(f"{self.name} перемещается в точку ({x}, {y}).")


# Класс для постройки
class Building(GameObject):
    def __init__(self, object_id, name, x, y, built=False):
        super().__init__(object_id, name, x, y)
        self.built = built

    def isBuilt(self):
        return self.built


# Класс для крепости
class Fort(Building, Attacker):
    def __init__(self, object_id, name, x, y, built=False, damage=20):
        super().__init__(object_id, name, x, y, built)
        self.damage = damage

    def attack(self, unit):
        if unit.isAlive():
            unit.receiveDamage(self.damage)
            print(f"{self.name} атакует {unit.getName()} пушечным выстрелом и наносит {self.damage} урона.")


# Класс для дома на колёсах
class MobileHouse(Building, Moveable):
    def __init__(self, object_id, name, x, y, built=False):
        super().__init__(object_id, name, x, y, built)

    def move(self, x, y):
        self.x = x
        self.y = y
        print(f"{self.name} перемещается в точку ({x}, {y}).")

archer = Archer(1, "Лучник", 0, 0, 100, 10)
unit = Unit(2, "Пехотинец", 5, 5, 50)
fort = Fort(3, "Крепость", 10, 10, built=True)
archer.attack(unit)
archer.move(3, 3)
fort.attack(unit)
unit.receiveDamage(10)