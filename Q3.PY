class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarLados(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def retornarLados(self):
        return self.base, self.altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)


def main():
    base = float(input("Informe a base do retângulo: "))
    altura = float(input("Informe a altura do retângulo: "))

    retangulo = Retangulo(base, altura)

    area = retangulo.calcularArea()
    perimetro = retangulo.calcularPerimetro()

    print("Área do retângulo:", area)
    print("Perímetro do retângulo:", perimetro)

    tamanho_piso = float(input("Informe o tamanho do piso: "))
    tamanho_rodape = float(input("Informe o tamanho do rodapé: "))

    area_piso = tamanho_piso * tamanho_piso
    area_rodape = retangulo.calcularPerimetro() * tamanho_rodape

    quantidade_pisos = area / area_piso
    quantidade_rodapes = retangulo.calcularPerimetro() / tamanho_rodape

    print("Quantidade de pisos necessários:", quantidade_pisos)
    print("Quantidade de rodapés necessários:", quantidade_rodapes)

if __name__ == "__main__":
    main()
