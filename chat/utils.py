from .models import ChatParticipants


def add_participant_to_chat(chat, user, is_owner=False):
    chat.participants.add(
        user
    )
    chat.save()
    if is_owner:

        cp = ChatParticipants.objects.get(chat=chat, user=request.user)
        cp.is_owner = True
        cp.save()
