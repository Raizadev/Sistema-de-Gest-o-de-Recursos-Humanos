import json

class FuncionarioRepository:
    def __init__(self, file_path="funcionarios.json"):
        self.file_path = file_path

    def salvar(self, funcionarios):
        with open(self.file_path, "w") as f:
            json.dump([func.to_dict() for func in funcionarios], f, indent=4)
