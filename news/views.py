from django.shortcuts import render, get_object_or_404,redirect
from .models import News
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def news_list(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    return render(request, 'news/news_detail.html', {'news': news_item})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('news_list')
    else:
        form = AuthenticationForm()
    return render(request, 'news/login.html', {'form': form})