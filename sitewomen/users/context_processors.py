# sitewomen/users/context_processors.py
from women.utils import menu


def get_women_context(request):
    return {"mainmenu": menu}
