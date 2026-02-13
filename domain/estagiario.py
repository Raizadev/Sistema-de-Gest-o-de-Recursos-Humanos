from .funcionario import Funcionario

class Estagiario(Funcionario):
    def calcular_salario(self) -> float:
        return self._salario_base
