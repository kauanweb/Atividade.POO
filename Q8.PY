class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)
        print(f"{self.nome} comeu {alimento}")

    def verBucho(self):
        print(f"Conteúdo do bucho de {self.nome}: {', '.join(self.bucho)}")

    def digerir(self):
        if self.bucho:
            print(f"{self.nome} está digerindo...")
            self.bucho = []
        else:
            print(f"{self.nome} não tem nada no bucho para digerir")


if __name__ == "__main__":
    macaco1 = Macaco("Macaco1")
    macaco2 = Macaco("Macaco2")

    alimentos = ["banana", "maçã", "laranja"]

    for alimento in alimentos:
        macaco1.comer(alimento)
        macaco2.comer(alimento)

    macaco1.verBucho()
    macaco2.verBucho()

    macaco1.digerir()
    macaco2.digerir()

    macaco1.verBucho()
    macaco2.verBucho()
