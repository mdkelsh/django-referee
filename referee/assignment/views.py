from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from assignment.models import Assignment
from django.core.urlresolvers import reverse

def index(request):
    open_games_list =  list(Assignment.objects.exclude(status='Closed'))
    template = loader.get_template('assignment/index.html')
    context = RequestContext(request, {'open_games_list': open_games_list,})
    return HttpResponse(template.render(context))

def detail(request, game_id):
    if request.user.is_authenticated():
	game = get_object_or_404(Assignment, pk=game_id)
	return render(request, 'assignment/detail.html', {'game': game})
    else:
	return HttpResponse('accounts/login/')

def results(request, game_id):
    return HttpResponse("You're looking at referees assigned to %s." % game_id)

def signup(request, game_id):
    if request.method == "POST":

	u = User()
	post = request.POST['signup']
	match = Assignment(post = request.session['uname'])
	match.save()
	
    return HttpResponseRedirect(reverse('detail', args=(game_id,)))
