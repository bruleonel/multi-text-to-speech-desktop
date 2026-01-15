# 🎧 TTS Desktop App (Text to Speech)

Aplicação **desktop em Python** que permite converter **várias frases em inglês** em **arquivos MP3 separados**, de forma simples e rápida.

O usuário pode colar várias frases de uma vez, escolher uma pasta de destino e o sistema gera automaticamente os áudios numerados.

---

## ✨ Funcionalidades

* Interface gráfica desktop (Tkinter)
* Conversão de **texto em inglês → áudio MP3**
* Suporte a **múltiplas frases de uma vez**
* Separação das frases por **ponto e vírgula (`;`)**
* Geração automática de arquivos:

  * `audio_1.mp3`, `audio_2.mp3`, `audio_3.mp3`, ...
* Usuário escolhe a **pasta de destino**
* Tratamento de erros e validações
* Arquitetura organizada e escalável

---

## 🖥️ Exemplo de uso

Cole no campo de texto:

```
Hello, how are you?;
This project focuses on QA automation;
I worked with APIs and databases;
123;
```

Resultado:

```
audio_1.mp3
audio_2.mp3
audio_3.mp3
audio_4.mp3
```

---

## 📁 Estrutura do projeto

```
tts_app/
├── app.py
├── requirements.txt
│
├── ui/
│   └── main_window.py
│
├── services/
│   └── tts_service.py
│
├── utils/
│   └── file_utils.py
```

---

## ⚙️ Requisitos

* Python **3.10+** (testado com Python 3.13)
* Windows
* Conexão com internet (para o motor de voz)

---

## 🚀 Como executar em modo desenvolvimento

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/tts-desktop-app.git
cd tts-desktop-app/tts_app
```

### 2️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Execute o aplicativo

```bash
python app.py
```

---

## 🧠 Regras importantes

* As frases **devem ser separadas por `;`**
* Cada frase gera **um MP3 separado**
* Existe um limite de caracteres por frase (configurável no código)
* Números são aceitos (ex: `123` → áudio em inglês)

---

## 📦 Tecnologias utilizadas

* Python
* Tkinter
* edge-tts (Microsoft Edge Text-to-Speech)

---

## 🔮 Próximas melhorias (roadmap)

* Seleção de voz (masculina / feminina)
* Suporte a outros idiomas
* Barra de progresso
* Player de áudio integrado
* Histórico de frases
* Empacotamento multiplataforma

---

## 📄 Licença

Este projeto é de uso livre para estudos e projetos pessoais.

---

## 🙌 Autor

Desenvolvido por **Bruna Leonel** 💙
