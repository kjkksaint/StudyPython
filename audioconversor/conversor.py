from gtts import gTTS
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import threading
import time

# === Tema e Configuração Global ===
tema = {
    "claro": {
        "bg": "#f5f5f5",
        "fg": "#333333",
        "input_bg": "#ffffff",
        "button_bg": "#4CAF50",
        "button_fg": "white",
        "highlight": "#2196F3"
    },
    "escuro": {
        "bg": "#2b2b2b",
        "fg": "#dddddd",
        "input_bg": "#3c3f41",
        "button_bg": "#5C6BC0",
        "button_fg": "white",
        "highlight": "#7986CB"
    }
}

tema_atual = "claro"

def aplicar_tema():
    cores = tema[tema_atual]
    app.configure(bg=cores["bg"])
    text_area.configure(bg=cores["input_bg"], fg=cores["fg"], insertbackground=cores["fg"])
    frame_nome.configure(bg=cores["bg"])
    frame_opcoes.configure(bg=cores["bg"])
    frame_botoes.configure(bg=cores["bg"])
    
    for widget in frame_nome.winfo_children():
        try: widget.configure(bg=cores["bg"], fg=cores["fg"])
        except: pass

    for widget in frame_opcoes.winfo_children():
        try: widget.configure(bg=cores["bg"], fg=cores["fg"])
        except: pass

    for btn in botoes:
        btn.configure(bg=cores["button_bg"], fg=cores["button_fg"])

# === Função para gerar o áudio ===
def gerar_audio():
    texto = text_area.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Atenção", "Digite ou carregue um texto para converter!")
        return

    nome_arquivo = entry_nome.get().strip()
    if not nome_arquivo:
        nome_arquivo = "audio.mp3"
    elif not nome_arquivo.endswith(".mp3"):
        nome_arquivo += ".mp3"

    velocidade = var_velocidade.get()
    idioma = var_idioma.get()

    threading.Thread(target=processar_audio, args=(texto, nome_arquivo, idioma, velocidade)).start()

# === Processamento e barra de progresso ===
def processar_audio(texto, nome_arquivo, idioma, velocidade):
    try:
        barra_progresso["value"] = 0
        app.update_idletasks()

        for i in range(1, 80, 10):
            time.sleep(0.2)
            barra_progresso["value"] = i
            app.update_idletasks()

        slow = True if velocidade == "Lento" else False
        tts = gTTS(text=texto, lang=idioma, slow=slow)

        barra_progresso["value"] = 80
        app.update_idletasks()

        tts.save(nome_arquivo)

        barra_progresso["value"] = 100
        app.update_idletasks()
        messagebox.showinfo("Sucesso", f"Áudio salvo como: {nome_arquivo}")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao salvar o áudio.\n{e}")
    finally:
        barra_progresso["value"] = 0

# === Carregar texto de arquivo ===
def carregar_txt():
    caminho_arquivo = filedialog.askopenfilename(
        filetypes=[("Arquivos de Texto", "*.txt")],
        title="Selecione um arquivo .txt"
    )
    if caminho_arquivo:
        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                text_area.delete("1.0", tk.END)
                text_area.insert(tk.END, conteudo)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler o arquivo.\n{e}")

# === Reproduzir áudio ===
def reproduzir_audio():
    nome_arquivo = entry_nome.get().strip()
    if not nome_arquivo.endswith(".mp3"):
        nome_arquivo += ".mp3"

    if os.path.exists(nome_arquivo):
        try:
            if os.name == 'nt':
                os.startfile(nome_arquivo)
            else:
                os.system(f"xdg-open '{nome_arquivo}'")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível tocar o áudio.\n{e}")
    else:
        messagebox.showwarning("Atenção", "Arquivo de áudio não encontrado!")

# === Alternar Tema ===
def alternar_tema():
    global tema_atual
    tema_atual = "escuro" if tema_atual == "claro" else "claro"
    aplicar_tema()

# === Interface Principal ===
app = tk.Tk()
app.title("Conversor de Texto para Áudio (.mp3)")
app.geometry("550x510")
app.resizable(False, False)

# Ícone personalizado (substitua pelo seu .ico)
try:
    app.iconbitmap('icone.ico')
except:
    pass

# Área de texto
text_area = tk.Text(app, wrap=tk.WORD, height=15, width=65, font=("Arial", 10))
text_area.pack(pady=15)

# Nome do arquivo
frame_nome = tk.Frame(app)
frame_nome.pack()
tk.Label(frame_nome, text="Nome do arquivo MP3:").pack(side=tk.LEFT, padx=5)
entry_nome = tk.Entry(frame_nome, width=35)
entry_nome.pack(side=tk.LEFT)

# Configurações de voz
frame_opcoes = tk.Frame(app)
frame_opcoes.pack(pady=10)

var_velocidade = tk.StringVar(value="Normal")
tk.Label(frame_opcoes, text="Velocidade:").grid(row=0, column=0, padx=5)
menu_velocidade = ttk.Combobox(frame_opcoes, textvariable=var_velocidade, values=["Normal", "Lento"], state="readonly", width=10)
menu_velocidade.grid(row=0, column=1, padx=5)

var_idioma = tk.StringVar(value="pt-br")
tk.Label(frame_opcoes, text="Idioma:").grid(row=0, column=2, padx=5)
menu_idioma = ttk.Combobox(frame_opcoes, textvariable=var_idioma, values=["pt-br", "en"], state="readonly", width=10)
menu_idioma.grid(row=0, column=3, padx=5)

# Barra de progresso
barra_progresso = ttk.Progressbar(app, length=450, mode='determinate')
barra_progresso.pack(pady=15)

# Botões
frame_botoes = tk.Frame(app)
frame_botoes.pack(pady=10)

botoes = []

btn_gerar = tk.Button(frame_botoes, text="💾 Salvar MP3", command=gerar_audio, width=15)
btn_gerar.grid(row=0, column=0, padx=8)
botoes.append(btn_gerar)

btn_carregar = tk.Button(frame_botoes, text="📂 Carregar TXT", command=carregar_txt, width=15)
btn_carregar.grid(row=0, column=1, padx=8)
botoes.append(btn_carregar)

btn_reproduzir = tk.Button(frame_botoes, text="▶️ Tocar Áudio", command=reproduzir_audio, width=15)
btn_reproduzir.grid(row=0, column=2, padx=8)
botoes.append(btn_reproduzir)

btn_tema = tk.Button(app, text="🌓 Alternar Tema", command=alternar_tema, width=20)
btn_tema.pack(pady=10)
botoes.append(btn_tema)

# Aplicar o tema inicial
aplicar_tema()

# Iniciar app
app.mainloop()
