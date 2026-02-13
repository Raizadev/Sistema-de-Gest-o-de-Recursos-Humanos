import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from domain.desenvolvedor import Desenvolvedor
from domain.gestor import Gestor
from domain.estagiario import Estagiario
from services.folha_pagamento import FolhaPagamento
from repository.funcionario_repository import FuncionarioRepository
import logging





def configurar_logging():
     
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def criar_funcionarios() -> list:
    return [
        Desenvolvedor("Ana", 2500, 700),
        Gestor("Carlos", 5000, 2000),
        Estagiario("João", 1200)
    ]


def executar():
    try:
        funcionarios = criar_funcionarios()
        folha = FolhaPagamento(funcionarios)
        repo = FuncionarioRepository()

        print("=== Folha Salarial ===")

        for funcionario in folha.listar_salarios():
            print(funcionario)

        total = folha.calcular_total()
        print(f"\nTotal da folha: {total}")

        repo.salvar(funcionarios)

        logging.info("Folha salarial calculada com sucesso.")

    except Exception as e:
        logging.error(f"Erro na execução: {e}")
        print("Ocorreu um erro. Verifique o log.")


if __name__ == "__main__":
    configurar_logging()
    executar()
