import json
import unittest
import subprocess
from pathlib import Path

class MulaTestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        json_path = Path(__file__).resolve().parent / "test_properties.json"
        data = cls.__read_json(json_path)
        cls.username = data["tester-user"]
        cls.password = data["tester-password"]
        cls.course_id = data["course-id"]
        cls.fup_act = data["fup-activity"]
        cls.ed_act = data["ed-activity"]
        cls.poo_act = data["poo-activity"]

    @classmethod
    def __read_json(cls, json_path: Path):
        try:
            with open(json_path, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"Arquivo '{json_path}' não encontrado.")
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar o arquivo JSON: {e}")

    def build_command(self, parameters: str):
        return f"mula -u {self.username} -p {self.password} -i {self.course_id} {parameters}"

    def execute(self, command):
        result = subprocess.run(command, capture_output=True, text=True)
        return result