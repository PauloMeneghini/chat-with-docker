import subprocess
import sys

# Lista das bibliotecas a serem instaladas
packages = [
    "langchain-huggingface",
    "langchain_community",
    "langchain_core",
    "langchain_milvus",
    "Flask",
    "pypdf"
]

def install_packages():
    for package in packages:
        try:
            print(f"Instalando {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Erro ao instalar {package}: {e}")

if __name__ == "__main__":
    install_packages()
    print("Instalação concluída!")
