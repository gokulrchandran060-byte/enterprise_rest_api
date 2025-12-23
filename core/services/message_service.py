from core.models import Message

def create_message(content):
    return Message.objects.create(content=content)

def list_all_messages():
    return Message.objects.all()
