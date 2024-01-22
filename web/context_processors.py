from .models import Updates  # Import the Updates model


def updates_context(request):
    updates = Updates.objects.filter(is_updates=True)
    return {"updates": updates}
