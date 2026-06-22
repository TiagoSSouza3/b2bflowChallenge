from services import supabase as supa_service
from services import whatsapp as whats_service

contacts = supa_service.getContacts()

res = whats_service.sendMessage(contacts["data"][1]["number"], contacts["data"][1]["name"])