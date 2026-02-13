from .funcionario import Funcionario

class Desenvolvedor(Funcionario):
    def __init__(self, nome: str, salario_base: float, bonus: float):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self) -> float:
        return self._salario_base + self.bonus
