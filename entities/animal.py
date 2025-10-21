class Animal:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    @classmethod
    def get_list(cls):
        animals = [cls("Jirafa", "Naranja"),
                   cls("Zebra", "Blanca y Negra"),
                   cls("Xenomorpho", "Negro"),
                   cls("Guacamaya", "Roja"),
                   cls("Cabra", "Blanca")
                   ]
        return animals
