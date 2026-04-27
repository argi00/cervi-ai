# Ce repos est pour le deployement local de gemma4 via Ollama pour pouvoir l'utiliser comme agent conversationel pour le cancer du col de l'utérus 



# Etape 1: Telecharger OLLAMA 

- LINUX
curl -fsSL https://ollama.com/install.sh | sh

- WINDOWS -----Dans powershell-----
irm https://ollama.com/install.ps1 | iex


# Etape 2: Telecharger gemma 4
Ollama pull gemma4

# Etape 3: Construction du modele de cancer de l'uterus
ollama create cervi-ai -f Modelfile

# Etape 4: Lancer ollama
ollama run cervi-ain 
    # En cas de problème faite
        ollama list --pour avoir le nom exacte du model--

# Etape 6 : fast api (En developpement) --Arriver a cette etape faite signe a argi pour continuer
pip install fastapi uvicorn requests
uvicorn main:app --reload

