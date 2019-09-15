from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from .models import ArticleColumn, ArticlePost, Comment
from .forms import ArticleColumnForm, ArticlePostForm, CommentForm

from django.shortcuts import get_object_or_404
from django.shortcuts import render

import redis
from django.conf import settings
r = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

@csrf_exempt
@require_POST
@login_required(login_url='/account/login/')
def like_article(request):
    article_id = request.POST.get('id')
    action = request.POST.get('action')
    if article_id and action:
        try:
            article = ArticlePost.objects.get(id=article_id)
            if action == 'like':
                article.users_like.add(request.user)
                return HttpResponse("1")
            else:
                article.users_like.remove(request.user)
                return HttpResponse("2")
        except:
            return HttpResponse("no")



def article_detail(request, id, slug):
    #print(dir(request.session))
    #print(request.session.items())
    #useritem = request.session.items())
    article = get_object_or_404(ArticlePost, id=id, slug=slug)
    total_views = r.incr('article:{}:views'.format(article.id))
    #print(article.id)
    r.zincrby('article_ranking', 1, article.id)
    #print(total_views)

    article_ranking = r.zrange('article_ranking', 0, -1, desc=True)[:10]
    #print(article_ranking)
    article_ranking_ids = [int(id) for id in article_ranking]
    #print(article_ranking_ids)
    most_viewed = list(ArticlePost.objects.filter(id__in=article_ranking_ids))
    #print(most_viewed)
    most_viewed.sort(key=lambda x: article_ranking_ids.index(x.id))
    #print(most_viewed[0].title)
    print(id, "       ",slug)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        #print(comment_form)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'article/list/article_detail.html', {'article': article, 'total_views':total_views, 'most_viewed':most_viewed, "comment_form": comment_form})