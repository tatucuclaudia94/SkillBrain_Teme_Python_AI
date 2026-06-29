# Exercitiul 1
# Logger Singleton care scrie in fisierul "istoric.txt"

class Logger:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, mesaj):
        with open("istoric.txt", "a") as f:
            f.write(mesaj + "\n")


logger1 = Logger()
logger2 = Logger()

logger1.log("Program pornit.")
logger2.log("Se scrie in acelasi logger.")


# Exercitiul 2
# Factory pentru animale

class Caine:
    def sunet(self):
        return "Ham ham"


class Pisica:
    def sunet(self):
        return "Miau"


class Vaca:
    def sunet(self):
        return "Muu"


class AnimalFactory:

    def creeaza_animal(self, tip):

        if tip == "caine":
            return Caine()

        elif tip == "pisica":
            return Pisica()

        elif tip == "vaca":
            return Vaca()

        else:
            return None


factory = AnimalFactory()

animal = factory.creeaza_animal("caine")
print(animal.sunet())


# Exercitiul 3
# Builder pentru Pizza

class Pizza:

    def __init__(self):
        self.toppinguri = []

    def adauga_topping(self, topping):
        self.toppinguri.append(topping)

    def afiseaza(self):
        print("Pizza cu:", ", ".join(self.toppinguri))


class PizzaBuilder:

    def __init__(self):
        self.pizza = Pizza()

    def cu_branza(self):
        self.pizza.adauga_topping("branza")
        return self

    def cu_salam(self):
        self.pizza.adauga_topping("salam")
        return self

    def cu_ciuperci(self):
        self.pizza.adauga_topping("ciuperci")
        return self

    def construieste(self):
        return self.pizza


builder = PizzaBuilder()

pizza = builder.cu_branza().cu_salam().cu_ciuperci().construieste()

pizza.afiseaza()
