class TV:
    def __init__(self, max_channel, max_volume):
        self.channel = 1
        self.volume = 50
        self.max_channel = max_channel
        self.max_volume = max_volume

    def change_channel(self, new_channel):
        if 1 <= new_channel <= self.max_channel:
            self.channel = new_channel
            print(f"Canal alterado para {self.channel}")
        else:
            print("Canal inválido")

    def increase_volume(self):
        if self.volume < self.max_volume:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")
        else:
            print("Volume no máximo")

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")
        else:
            print("Volume no mínimo")

    def display_status(self):
        print(f"Canal: {self.channel}, Volume: {self.volume}")


def main():
    max_channel = 100
    max_volume = 100
    tv = TV(max_channel, max_volume)

    while True:
        print("\nControle Remoto da TV")
        print("1 - Trocar de canal")
        print("2 - Aumentar volume")
        print("3 - Diminuir volume")
        print("4 - Exibir status")
        print("0 - Desligar TV")
        choice = int(input("Escolha uma opção: "))

        if choice == 1:
            new_channel = int(input("Digite o número do novo canal: "))
            tv.change_channel(new_channel)
        elif choice == 2:
            tv.increase_volume()
        elif choice == 3:
            tv.decrease_volume()
        elif choice == 4:
            tv.display_status()
        elif choice == 0:
            print("TV desligada.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
