from ast import Try
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

# Busca todos os contatos do banco de dados
def getContacts():
    try:
        supabase = createClient();

        response = supabase.table("contacts").select("*").execute();
        
        return response.data;
    except Exception as e:
        print("Erro ao buscar contatos: ", e);
        return [];

# Cria a instacia do supabase com as informações do .env
def createClient():
    url = os.getenv("SUPABASE_URL") or "";
    key = os.getenv("SUPABASE_KEY") or "";

    return create_client(url, key);