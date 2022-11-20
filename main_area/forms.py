from django import forms
from .models import Question, Review


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'email', 'message']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'review', 'image']
        