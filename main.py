import services.supabase as supa_service
import services.whatsapp as whats_service

contatos = supa_service.getContacts()

print(contatos)