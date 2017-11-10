from charative.models import Profile, RomanceType, Genres, Chara
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class MatchingQuestions(forms.ModelForm):

    class Meta:
        model = Profile
        fields=
