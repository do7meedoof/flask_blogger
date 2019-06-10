from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from django.contrib.auth.decorators import login_required

def register(request):
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            new_user = form.save(commit=False)
            # form.save()
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()

            # username = form.cleaned_data['username']
            # messages.success(request, 'تهانينا يا {}، لقد تم تسجيلك بنجاح'.format(username))
            messages.success(request, f'تهانينا يا {new_user}، لقد تم تسجيلك بنجاح')
            # messages.success(request, f'تهانينا يا {username}، لقد تم تسجيلك بنجاح')

            #return redirect('home')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'user/register.html', {
        'title': 'التسجيل',
        'form': form,
    })

def login_user(request):
    if(request.method == 'POST'):
        #form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if(user is not None):
            login(request, user)
            # return redirect('home')
            return redirect('profile')
        else:
            messages.warning(request, 'هناك خطأ  في كلمة المرور أو اسم المستخدم')

    # else: form = LoginForm()

    return render(request, 'user/login.html', {
        'title': 'تسجيل الدخول',
        # 'form': form,
    })

def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html', {
        'title': 'تسجيل الخروج',
    })

@login_required(login_url='login')

def profile(request):
    posts = Post.objects.filter(author = request.user)
    return render(request, 'user/profile.html', {
        'title': 'الملف الشخصي',
        'posts': posts,
    })