from django.views.decorators.csrf import csrf_exempt
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse

@csrf_exempt
def post(request: WSGIRequest):
    if request.method == 'GET':
		    return JsonResponse({'status': 'Get posts succeed', 'posts': _get_all_posts()})

# 把資料庫的 Post 資料，全部挖出來、包成 dict 的格式出去
def _get_all_posts():
    # all posts
    all_posts = Post.objects.all()

    posts = []

    for _post in all_posts:
        post_data = {
            'post_id': _post.id,
            'author': str(_post.author),
            'created': _format_time(_post.created),
            'last_updated': _format_time(_post.last_updated),
            'content': _post.content,
            'liked': _post.liked,
            'comments_count': len(_all_comments),
            'comments': _all_comments,
        }
        posts.append(post_data)

    return posts