from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from twits.models import Tweet, User_view
from twits.forms import TweetModelForm
from authorizations.models import User
# Create your views here.


def index(request):
    return render(request, 'base.html')

@login_required(login_url='login')
def get_all_twits(request):
    context = {
        'twits': Tweet.objects.order_by('-created_at'),
        'title': 'All twits',
        'user': request.user,
    }
    return render(request, 'all.html', context)


@login_required(login_url='login')
def user(request):
    context = {
        'user_twits': Tweet.objects.filter(creator=request.user).order_by('-created_at'),
        'title': 'All twits',
        'twit_form': TweetModelForm(),
        'user': request.user
    }
    return render(request, 'user.html', context)

def create_twit(request):
    if request.method == 'POST':
        form = TweetModelForm(request.POST)
        if form.is_valid():
            Tweet.objects.create(
                creator = request.user,
                content = form.data['content']
            )
        return redirect(request.headers.get('Referer'))