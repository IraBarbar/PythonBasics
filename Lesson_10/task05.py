# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.
class Mammals:
    skill = ''

    def __init__(self, name: str):
        self.name = name

    def show_name(self):
        print('Имя:', self.name)

    def skills(self):
        print('Навык:', self.skill)


class Birds(Mammals):
    skill = 'летаю'

    def __init__(self, name: str, color: str):
        self.color = color
        super().__init__(name)

    def show_color(self):
        print("Цвет:", self.color)


class Animals(Mammals):
    skill = 'бегаю'

    def __init__(self, name: str, age: int):
        super().__init__(name)
        self.age = age

    def show_age(self):
        print('Возраст(лет):', self.age)




