import tkinter as tk
from tkinter import messagebox
import asyncio

from services.tts_service import TTSService
from utils.file_utils import escolher_pasta

MAX_CARACTERES = 300

class MainWindow:
    def __init__(self):
        self.tts_service = TTSService()

        self.janela = tk.Tk()
        self.janela.title("Text to Speech - Inglês (Múltiplas Frases)")
        self.janela.geometry("600x350")

        self._build_ui()

    def _build_ui(self):
        label = tk.Label(
            self.janela,
            text="Cole as frases em inglês (separadas por ';'):"
        )
        label.pack(pady=5)

        self.text_box = tk.Text(self.janela, height=10)
        self.text_box.pack(padx=10, pady=5)

        botao = tk.Button(
            self.janela,
            text="Gerar áudios MP3",
            command=self.converter
        )
        botao.pack(pady=15)

    def converter(self):
        texto = self.text_box.get("1.0", tk.END).strip()

        if not texto:
            messagebox.showwarning(
                "Atenção",
                "Cole pelo menos uma frase."
            )
            return

        # Divide por ponto e vírgula
        frases = [
            f.strip()
            for f in texto.split(";")
            if f.strip()
        ]

        if not frases:
            messagebox.showwarning(
                "Atenção",
                "Nenhuma frase válida encontrada."
            )
            return

        # Validação de tamanho
        frases_invalidas = [
            f for f in frases if len(f) > MAX_CARACTERES
        ]

        if frases_invalidas:
            messagebox.showerror(
                "Erro",
                f"Existem frases com mais de {MAX_CARACTERES} caracteres."
            )
            return

        pasta = escolher_pasta()
        if not pasta:
            return

        try:
            asyncio.run(
                self.tts_service.gerar_varios_mp3(
                    frases,
                    pasta
                )
            )
            messagebox.showinfo(
                "Sucesso",
                f"{len(frases)} áudios gerados com sucesso!"
            )
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def run(self):
        self.janela.mainloop()
