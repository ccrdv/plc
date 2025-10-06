class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mover(self):
        print(f"O {self.marca} {self.modelo} está se movendo de forma genérica.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas
    
    def mover(self):
        print(f"O carro {self.marca} {self.modelo} com {self.portas} portas está rodando na estrada.")

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas
    
    def mover(self):
        print(f"A moto {self.marca} {self.modelo} de {self.cilindradas}cc está acelerando velozmente.")

if __name__ == "__main__":
    carro = Carro("Toyota", "Corolla", 4)
    moto = Moto("Honda", "CBR", 600)
    
    veiculos = [carro, moto]
    
    print("Demonstração de Polimorfismo:")
    for veiculo in veiculos:
        veiculo.mover()
    
    veiculo_generico = Veiculo("Fiat", "Uno")
    veiculo_generico.mover()