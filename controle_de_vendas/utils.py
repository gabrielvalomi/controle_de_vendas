import json
import os

DATABASE_FILE = "database.json"


def carregar_dados():
    if not os.path.exists(DATABASE_FILE):
        return {"produtos": [], "clientes": [], "vendas": []}

    with open(DATABASE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_dados(dados):
    with open(DATABASE_FILE, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)


def gerar_id(lista):
    if not lista:
        return 1
    return max(item["id"] for item in lista) + 1
