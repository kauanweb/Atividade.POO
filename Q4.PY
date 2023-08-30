class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.altura += anos * 0.5  
    
    def engordar(self, kg):
        self.peso += kg
    
    def emagrecer(self, kg):
        self.peso -= kg
    
    def crescer(self, cm):
        self.altura += cm

pessoa1 = Pessoa("João", 18, 70, 170)
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Peso: {pessoa1.peso}, Altura: {pessoa1.altura}")
pessoa1.envelhecer(2)
print(f"Idade após envelhecer: {pessoa1.idade}, Altura após crescer: {pessoa1.altura}")
pessoa1.engordar(5)
print(f"Peso após engordar: {pessoa1.peso}")
pessoa1.emagrecer(3)
print(f"Peso após emagrecer: {pessoa1.peso}")
pessoa1.crescer(2)
print(f"Altura após crescer: {pessoa1.altura}")
