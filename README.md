# Instruções para rodar a IA

1. Intalar o Docker e configurar o WSL no windows
2. Rodar o comando no powershell como administador:
   - `Invoke-WebRequest https://raw.githubusercontent.com/milvus-io/milvus/refs/heads/master/scripts/standalone_embed.bat -OutFile standalone.bat`
3. Instalar o Ollama:
   - `https://ollama.com/`
4. Abrir o CMD como administrador e rodar o comando:
   - `ollama pull llama3`

5. ### Rodar os seguintes comandos:
  - `pip install langchain-huggingface`
  - `pip install langchain_community`
  - `pip install langchain_core`
  - `pip install Flask`
  - `pip install pypdf`

6. Após todas as bibliotecas instaladas, basta digitar e rodar o seguinte comando no terminal na pasta do projeto
  - `python app.py`
    Esse comando irá iniciar o servidor python na porta 5050

