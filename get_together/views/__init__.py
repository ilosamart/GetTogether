from django.utils.translation import ugettext_lazy as _

from django.contrib import messages
from django.contrib.auth import logout as logout_user
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from events.models.profiles import Team, UserProfile, Member
from events.forms import TeamForm, NewTeamForm, TeamEventForm, NewTeamEventForm, NewPlaceForm

from events.models.events import Event, Place, Attendee

import datetime
import simplejson

from .teams import *
from .events import *
from .places import *
from .user import *

# Create your views here.

def logout(request):
    if request.user.is_authenticated:
        logout_user(request)
    return redirect('home')

def home(request, *args, **kwards):
    if request.user.is_authenticated:
        user_teams = Team.objects.filter(owner_profile=request.user.profile)
        if len(user_teams) > 0:
            return redirect('events')
        else:
            return redirect('create-team')
    else:
        return render(request, 'get_together/index.html')

def places_list(request, *args, **kwargs):
    places = Place.objects.all()
    context = {
        'places_list': places,
    }
    return render(request, 'get_together/places/list_places.html', context)

def create_place(request):
    if request.method == 'GET':
        form = NewPlaceForm()

        context = {
            'place_form': form,
        }
        return render(request, 'get_together/places/create_place.html', context)
    elif request.method == 'POST':
        form = NewPlaceForm(request.POST)
        if form.is_valid:
            new_place = form.save()
            return redirect('places')
        else:
            context = {
                'place_form': form,
            }
            return render(request, 'get_together/places/create_place.html', context)
    else:
     return redirect('home')

