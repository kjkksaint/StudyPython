import pandas as pd
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# Carregar a planilha
file_path = "planilha_atualizada.xlsx"
df = pd.read_excel(file_path, sheet_name="esteira")

# Converter colunas de data para o formato datetime
df["DATA DE DESBLOQUEIO"] = pd.to_datetime(df["DATA DE DESBLOQUEIO"], dayfirst=True, errors='coerce')

# Definir a data limite para avisos (menos de 7 dias restantes)
data_atual = datetime.today()
data_limite = data_atual + timedelta(days=7)

# Filtrar os registros com desbloqueio em menos de 7 dias
avisos = df[(df["DATA DE DESBLOQUEIO"] >= data_atual) & (df["DATA DE DESBLOQUEIO"] <= data_limite)]

# Função para exibir pop-up
if not avisos.empty:
    root = tk.Tk()
    root.withdraw()  # Esconder a janela principal
    
    for index, row in avisos.iterrows():
        mensagem = f"Aviso: {row['NOME']} tem desbloqueio em {row['DATA DE DESBLOQUEIO'].strftime('%d/%m/%Y')}!"
        messagebox.showinfo("Aviso de Desbloqueio", mensagem)
    
    root.destroy()
