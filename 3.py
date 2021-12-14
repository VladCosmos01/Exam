class Tomato:

    states = {1: "Зеленый", 2: "Светло-зеленый", 3: "Красный"}

    def __init__(self, index):
        self._index = index
        self._state = 1

    def grow(self):
        self._state += 1
        return self._state

    def is_ripe(self):
        if self._state >= 3:
            return "Созрел"
        else:
            return "Не созрел"


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(i) for i in range(0, num)]

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        return all([i.is_ripe() for i in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print("Не все плоды созрели")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству")

if __name__ == '__main__':
    Gardener.knowledge_base()
    a = TomatoBush(3)
    b = Gardener("Vlad", a)
    b.work()
    b.harvest()