from django.shortcuts import render
from django.views import generic

from .models import User, Buys

def index(request):
    num_user = User.objects.all().count()
    num_buys = Buys.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={'num_user': num_user, 'num_buys': num_buys, 'num_visits':num_visits},
    )

class UserListView(generic.ListView):
    model = User
    paginate_by = 2

    def get_queryset(self):
        return User.objects.all()

class UserDetailView(generic.DetailView):
    model = User