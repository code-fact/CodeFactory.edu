from django import forms
from .models import Posts, Categorys

def choice():
    try:
        choices = [topic for topic in Categorys.objects.all().values_list('title','title')]
    except:
        choices=[]
    return choices

class posts(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'author', 'icon', 'description', 'category', 'content')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.HiddenInput(attrs={'class':'form-control'}),
            'icon':forms.FileInput(attrs={'class':'form-control-file'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'})
        }
    def __init__(self, *args, **kwargs):
        super(posts, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ChoiceField(choices=choice())

class Edit(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'icon', 'description', 'category', 'content')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'icon':forms.FileInput(attrs={'class':'form-control-file'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'})
        }
    def __init__(self, *args, **kwargs):
        super(Edit, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ChoiceField(choices=choice())

class MSG(forms.Form):
    name = forms.CharField(max_length=255, label='user name', widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.EmailField(label='mail', widget=forms.EmailInput(attrs={'class':'form-control'}))
    post = forms.CharField(required=False, max_length=510, label='post title', widget=forms.HiddenInput())
    msg = forms.CharField(label='comment', widget=forms.Textarea(attrs={'class':'form-control'}))
