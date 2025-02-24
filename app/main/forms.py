from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'rating', 'text']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 10,
                'step': 0.1,  # Позволяет дробные числа
                'placeholder': 'Рейтинг от 0 до 10'
            }),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш комментарий', 'rows': 4}),
        }
