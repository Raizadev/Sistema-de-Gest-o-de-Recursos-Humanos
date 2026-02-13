class FolhaPagamento:
    def __init__(self, funcionarios: list):
        self.funcionarios = funcionarios

    def calcular_total(self) -> float:
        return sum(f.calcular_salario() for f in self.funcionarios)

    def listar_salarios(self):
        return [f.to_dict() for f in self.funcionarios]
