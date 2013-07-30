from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from assignment.models import Assignment
from assignment.forms import AssignmentForm
from django.core.urlresolvers import reverse

def index(request):
    open_games_list =  list(Assignment.objects.exclude(status='CLOSED'))
    return render(request, 'assignment/index.html', {'open_games_list': open_games_list,})
 
def detail(request, game_id):
    if request.user.is_authenticated():
        game = AssignmentForm
    else:
        return HttpResponse('accounts/login/')
    return render(request, 'assignment/detail.html', {'game': game, 'id': game_id,})
    
def results(request, game_id):
    game = Assignment.objects.get(pk=game_id)
    return render(request, 'assignment/results.html', {'game': game}) 

def signup(request, game_id):
    if request.method == "POST":    
        form = AssignmentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                position = form.cleaned_data['position']
                username = request.user.get_username()
                a = Assignment.objects.get(pk=game_id)
                if (a.AR_1 != username) and (a.AR_2 != username) and (a.center != username):
                    if position == u'1':
                        a.center = username
                    elif position == u'2':
                        if a.AR_1:
                            a.AR_2 = username
                        else:
                            a.AR_1 = username
                    a.save()    
                    return HttpResponseRedirect('assigment/%s/results' % game_id)
                else:
                    return HttpResponse("You were not able to sign up for this game")
            else:
                return HttpResponseRedirect('/assignment/')
        else:
            form = AssignmentForm() # An unbound form

