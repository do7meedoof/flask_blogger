from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label = 'اسم المستخدم', max_length = 30, help_text = 'يجب ألا يحتوي الاسم على فراغات')
    email = forms.EmailField(label = 'البريد الالكتروني')
    first_name = forms.CharField(label = 'الاسم الأول')
    last_name = forms.CharField(label = 'الاسم الأخير')
    password1 = forms.CharField(label = 'كلمة المرور', widget = forms.PasswordInput(), min_length = 8)
    password2 = forms.CharField(label = 'تأكيد كلمة المرور', widget = forms.PasswordInput(), min_length = 8)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', )
    
    def clean_password2(self):
        cd = self.cleaned_data
        if(cd['password1'] != cd['password2']):
            raise forms.ValidationError('كلمة المرور غير متطابقة')
            return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if(User.objects.filter(username=cd['username']).exists()):
            raise forms.ValidationError('المستخدم موجود بالفعل في المستخدمين')
            return cd['username']
        elif(User.objects.filter(username=cd['username']) == ''):
            raise forms.ValidationError('الحقل لا يمكن أن يكون فارغا')
            return cd['username']
        else:
            return cd['username']

class LoginForm(forms.ModelForm):
    username = forms.CharField(label = 'اسم المستخدم')
    password = forms.CharField(label = 'كلمة المرور', widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')