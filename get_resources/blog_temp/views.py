from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import NewComment

posts = [
    {
        'title': 'التدوينة الأولى',
        'content': 'نص التدوينة الأولى كنص تجريبي',
        'post_date': '30-04-2019',
        'author': 'أحمد أبو عيسى',
    },
    {
        'title': 'التدوينة الثانية',
        'content': 'نص التدوينة الثانية كنص تجريبي',
        'post_date': '29-04-2019',
        'author': 'عبدالحميد محمد',
    },
    {
        'title': 'التدوينة الثالثة',
        'content': 'نص التدوينة الثالثة كنص تجريبي',
        'post_date': '28-04-2019',
        'author': 'ناصر منصور',
    },
    {
        'title': 'التدوينة الرابعة',
        'content': 'نص التدوينة الرابعة كنص تجريبي',
        'post_date': '30-04-2019',
        'author': 'سالم مصطفى',
    },
    
]

def home(request):
    context = {
        'title': ' الصفحة الرئيسة ',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'من أنا '})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    comments = post.comments.filter(active = True)
    
    # check before save comment if posted:
    if( request.method == 'POST'):
        comment_form = NewComment(data = request.POST)
        if(comment_form.is_valid()):
            new_comment = comment_form.save(commit = False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment()

    context = {
        'title': post, 
        'post': post, 
        'comments': comments,
        'comment_form': comment_form,
    }

    
    return render(request, 'blog/detail.html', context)