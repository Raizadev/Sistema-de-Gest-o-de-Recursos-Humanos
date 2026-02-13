from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str, salario_base: float):
        self.nome = nome
        self._salario_base = salario_base

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "nome": self.nome,
            "salario": self.calcular_salario()
        }
