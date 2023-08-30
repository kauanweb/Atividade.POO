class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Coordenadas do Ponto: ({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)

    def imprimir_centro(self):
        centro = self.encontrar_centro()
        centro.imprimir()


def criar_retangulo():
    x = float(input("Digite a coordenada x do ponto inicial do retângulo: "))
    y = float(input("Digite a coordenada y do ponto inicial do retângulo: "))
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    ponto_inicial = Ponto(x, y)
    return Retangulo(ponto_inicial, largura, altura)


def main():
    retangulos = []

    while True:
        print("\nMenu:")
        print("1 - Criar Retângulo")
        print("2 - Imprimir Centro de Retângulo")
        print("0 - Sair")
        choice = int(input("Escolha uma opção: "))

        if choice == 1:
            retangulo = criar_retangulo()
            retangulos.append(retangulo)
            print("Retângulo criado com sucesso!")
        elif choice == 2:
            if not retangulos:
                print("Nenhum retângulo criado ainda.")
            else:
                for i, retangulo in enumerate(retangulos, start=1):
                    print(f"Retângulo {i}:")
                    retangulo.imprimir_centro()
        elif choice == 0:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
