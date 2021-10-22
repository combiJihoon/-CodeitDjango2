from .models import Post


def validate_post():
    posts = Post.objects.all()

    for post in posts:
        if '&' in post.content:
            post.content = post.content.replace('&', '')
            post.save()
        if post.dt_modified < post.dt_created:
            post.save()
    print('실행 완료')
