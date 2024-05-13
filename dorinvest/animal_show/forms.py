from django.forms import ModelForm
from django import forms

from .models import Show, Animals, Feedback, EndedShow


class ShowForm(ModelForm):
    class Meta:
        model = Show
        fields = '__all__'


class AnimalsForm(ModelForm):
    class Meta:
        model = Animals
        fields = '__all__'


class FeedbackCreateForm(forms.ModelForm):
    """Форма отправки обратной связи"""
    class Meta:
        model = Feedback
        fields = ('user_phone', 'name')


class EndedShowForm(ModelForm):
    class Meta:
        model = EndedShow
        fields = '__all__'





