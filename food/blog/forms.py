from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = "__all__" отображать в форме все поля
        exclude = ["create_at", "post"]  # отоброжать в форме все поля кроме перечисленных
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Message'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Website'}),
        }
