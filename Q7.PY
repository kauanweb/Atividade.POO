class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
    
    def alterar_fome(self, nova_fome):
        self.fome = nova_fome
    
    def alterar_saude(self, nova_saude):
        self.saude = nova_saude
    
    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
    
    def retornar_nome(self):
        return self.nome
    
    def retornar_fome(self):
        return self.fome
    
    def retornar_saude(self):
        return self.saude
    
    def retornar_idade(self):
        return self.idade
    
    def calcular_humor(self):
        humor = (self.fome + self.saude) / 2
        return humor

tamagotchi = BichinhoVirtual("Tammy", 50, 80, 3)
print(f"Nome: {tamagotchi.retornar_nome()}, Fome: {tamagotchi.retornar_fome()}, Saúde: {tamagotchi.retornar_saude()}, Idade: {tamagotchi.retornar_idade()}")
print(f"Humor: {tamagotchi.calcular_humor()}")

tamagotchi.alterar_fome(30)
tamagotchi.alterar_saude(90)
tamagotchi.alterar_idade(4)
print(f"Fome após alteração: {tamagotchi.retornar_fome()}, Saúde após alteração: {tamagotchi.retornar_saude()}, Idade após alteração: {tamagotchi.retornar_idade()}")
print(f"Humor após alteração: {tamagotchi.calcular_humor()}")
