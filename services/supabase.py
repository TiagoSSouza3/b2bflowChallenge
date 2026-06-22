import os;
from supabase import create_client;
from dotenv import load_dotenv;

load_dotenv();

# Busca todos os contatos do banco de dados
def getContacts():
    try:
        supabase = createClient();

        res = supabase.table("contacts").select("*").execute();
        
        return {"type":"Success", "data":res.data};
    except Exception as e:
        return {"type":"Error", "message":e};

# Cria a instacia do supabase com as informações do .env
def createClient():
    url = os.getenv("SUPABASE_URL") or "";
    key = os.getenv("SUPABASE_KEY") or "";

    return create_client(url, key);