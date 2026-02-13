from .funcionario import Funcionario

class Gestor(Funcionario):
    def __init__(self, nome: str, salario_base: float, participacao: float):
        super().__init__(nome, salario_base)
        self.participacao = participacao

    def calcular_salario(self) -> float:
        return self._salario_base + self.participacao
