from services import supabase as supa_service;
from services import whatsapp as whats_service;

try:
    response = supa_service.getContacts();

    if(response["type"] == "Error"):
        raise Exception(response["message"]);

    contacts = response["data"];

    for contact in contacts:
        name = contact["name"] or "";
        number = contact["number"];

        res = whats_service.sendMessage(number, name);

        if(res["type"] == "Error"):
            print("Falha ao enviar mensagem para numero: ", number);
        else:
            print("Mensagem enviada com sucesso para o numero: ", number);
    
except Exception as e:
    print("ERROR: ", e);