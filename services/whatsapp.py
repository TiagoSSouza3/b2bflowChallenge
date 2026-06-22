import os;
from dotenv import load_dotenv;
import requests;

load_dotenv();

# Envia a mensagem padrão ao numero passado
def sendMessage(number, name):
    if(number == ""): return {"type":"Error", "message":"parametro 'number' invalido"};
    if(name == ""): return {"type":"Error", "message":"parametro 'name' invalido"};
    
    payload = {
        "phone": number,
        "message": f"Ola, {name} tudo bem com você?"
    };

    url = getURL();

    try:
        res = requests.post(url, json=payload);

        return {"type":"Success", "message":res.text};
    except Exception as e:
        return {"type":"Error", "message":e};

# Cria o URL com os dados do .env
def getURL():
    id = os.getenv("ZAPI_INSTANCE_ID") or "";
    token = os.getenv("ZAPI_INSTANCE_TOKEN") or "";

    return f"https://api.z-api.io/instances/{id}/token/{token}/send-text";