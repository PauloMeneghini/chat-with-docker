# Instruções para rodar a IA

1. Intalar o Docker
  - `https://www.docker.com/products/docker-desktop/`
2. Configurar o WSL no windows
  - `https://learn.microsoft.com/pt-br/windows/wsl/install`
3. Rodar o comando no powershell como administador:
  - `Invoke-WebRequest https://raw.githubusercontent.com/milvus-io/milvus/refs/heads/master/scripts/standalone_embed.bat -OutFile standalone.bat`
  - `standalone.bat start`
4. Instalar o Ollama:
  - `https://ollama.com/`
5. Abrir o CMD como administrador e rodar o comando:
  - `ollama pull llama3`

6. ### Rodar os seguintes comandos:
  - `pip install langchain-huggingface`
  - `pip install langchain_community`
  - `pip install langchain_core`
  - `pip install Flask`
  - `pip install pypdf`

7. Após todas as bibliotecas instaladas, basta digitar e rodar o seguinte comando no terminal na pasta do projeto
  - `python app.py`
    Esse comando irá iniciar o servidor python na porta 5050

