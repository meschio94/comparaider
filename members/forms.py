from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from members.models import User

class PersonSignUpForm(UserCreationForm):


    class Meta(UserCreationForm):
        model = User
        fields = ['username','email']
        success_url = reverse_lazy('home')