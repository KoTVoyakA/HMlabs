from django.shortcuts import render, redirect
from django.http import Http404
from .models import Article


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if request.user.is_anonymous:
        raise Http404  # не авторизован — гуляй

    if request.method == "POST":
        form = {
            'text': request.POST.get("text"),
            'title': request.POST.get("title")
        }

        # Проверяем, что поля не пустые
        if not form['title'] or not form['text']:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})

        # Проверяем уникальность названия
        if Article.objects.filter(title=form['title']).exists():
            form['errors'] = "Статья с таким названием уже существует"
            return render(request, 'create_post.html', {'form': form})

        # Создаём статью
        article = Article.objects.create(
            text=form['text'],
            title=form['title'],
            author=request.user
        )

        return redirect('get_article', article_id=article.id)

    # GET-запрос — просто показать форму
    return render(request, 'create_post.html', {})