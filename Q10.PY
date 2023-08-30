class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor_abastecido):
        litros_abastecidos = valor_abastecido / self.valorLitro
        if litros_abastecidos <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros_abastecidos
            return f"Abastecidos {litros_abastecidos:.2f} litros."
        else:
            return "Quantidade de combustível insuficiente na bomba."

    def abastecerPorLitro(self, litros_abastecidos):
        valor_a_pagar = litros_abastecidos * self.valorLitro
        if litros_abastecidos <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros_abastecidos
            return f"A pagar: R${valor_a_pagar:.2f}."
        else:
            return "Quantidade de combustível insuficiente na bomba."

    def alterarValor(self, novo_valor_litro):
        self.valorLitro = novo_valor_litro
        return f"Valor do litro alterado para R${novo_valor_litro:.2f}."

    def alterarCombustivel(self, novo_tipo_combustivel):
        self.tipoCombustivel = novo_tipo_combustivel
        return f"Tipo de combustível alterado para {novo_tipo_combustivel}."

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade
        return f"Quantidade de combustível alterada para {nova_quantidade:.2f} litros."


bomba = bombaCombustivel("Gasolina", 5.0, 1000)

print(bomba.abastecerPorValor(50))
print(bomba.abastecerPorLitro(20))
print(bomba.alterarValor(5.5))
print(bomba.alterarCombustivel("Etanol"))
print(bomba.alterarQuantidadeCombustivel(800))
