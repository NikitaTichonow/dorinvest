from animal_show.models import Show


def upcoming_show(request):
    return {'upcoming_show': Show.get_upcoming_show()}