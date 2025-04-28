import subprocess
import sys

# Lista de pacotes necessários
pacotes = ["gTTS"]

# Função para instalar pacotes
def instalar_pacote(pacote):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])
        print(f"{pacote} instalado com sucesso!")
    except subprocess.CalledProcessError:
        print(f"Erro ao instalar o pacote: {pacote}")

# Instalar todos os pacotes
for pacote in pacotes:
    instalar_pacote(pacote)

print("Todos os pacotes necessários foram instalados!")
