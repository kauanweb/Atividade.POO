class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor

minha_bola = Bola(cor="azul", circunferencia=25, material="couro")

print("Cor da bola:", minha_bola.mostraCor())  

minha_bola.trocaCor("vermelho")
print("Cor da bola após troca:", minha_bola.mostraCor())  
