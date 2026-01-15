import edge_tts
import os

class TTSService:
    async def gerar_varios_mp3(
        self,
        frases,
        pasta_destino,
        voice="en-US-AriaNeural"
    ):
        for index, frase in enumerate(frases, start=1):
            nome_arquivo = f"audio_{index}.mp3"
            caminho = os.path.join(pasta_destino, nome_arquivo)

            communicate = edge_tts.Communicate(
                text=frase,
                voice=voice
            )

            await communicate.save(caminho)
