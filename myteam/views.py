import os

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page

from .serializers import *


ATT = r'\wS|\wF|\wW|\wT'
DEF = r'\wB|\w\wB'
MID = r'\wM|\w\wM'
GK = r'GK'

DEF_NUM = 4
MID_NUM = 3
ATT_NUM = 3
GK_NUM = 1


# @cache_page(60 * 60 * 24 * 10, cache='default', key_prefix='')
def index(request):
    players = Player.objects.all().order_by('-Overall')
    nat = players.values('Nationality', 'Flag').distinct()[:10]
    club = players.values('Club', 'ClubLogo').distinct()[:10]
    context = {
        'nat': nat,
        'club': club,
    }
    return render(request, 'myteam/team.html', context)


# @cache_page(60 * 60 * 24 * 10, cache='default', key_prefix='')
def get_team(request):
    nat = request.GET.get('nat', '*')
    club = request.GET.get('club', '*')
    over = request.GET.get('over', 50)
    age = request.GET.get('age', 15)
    agil = request.GET.get('agil', 50)
    speed = request.GET.get('speed', 50)
    shotp = request.GET.get('shotp', 50)

    player_filter = {
        'Nationality__regex': nat,
        'Club__regex': club,
        'Overall__gte': over,
        'Age__gte': age,
        'Agility__gte': agil,
        'SprintSpeed__gte': speed,
        'ShotPower__gte': shotp,
    }

    gk_filter = {
        'Nationality__regex': nat,
        'Club__regex': club,
        'Overall__gte': over,
        'Age__gte': age,
    }

    player = Player.objects.filter(**player_filter).order_by('-Overall')

    f = player.filter(Position__regex=ATT)[:ATT_NUM]
    m = player.filter(Position__regex=MID)[:MID_NUM]
    b = player.filter(Position__regex=DEF)[:DEF_NUM]
    gk = Player.objects.filter(**gk_filter, Position__regex=GK).order_by('-Overall')[:GK_NUM]

    status = False
    if f.count() >= ATT_NUM and m.count() >= MID_NUM and b.count() >= DEF_NUM and gk.count() >= GK_NUM:
        status = True

    response = {
        'status': status,
        'f': PlayerSerializer(f[:ATT_NUM], many=True).data,
        'm': PlayerSerializer(m[:MID_NUM], many=True).data,
        'b': PlayerSerializer(b[:DEF_NUM], many=True).data,
        'gk': PlayerSerializer(gk[:GK_NUM], many=True).data,
    }

    return JsonResponse(response)


def import_csv(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'static/myteam/csv/fifa.csv')
    MyCsvModel.import_data(data=open(file_path))


def delete(request):
    Player.objects.all().delete()
