from tkinter import filedialog

def escolher_pasta():
    return filedialog.askdirectory(
        title="Escolha a pasta para salvar os áudios"
    )
