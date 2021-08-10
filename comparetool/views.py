from django.shortcuts import render

from members.models import User
from .models import CompareItems
# Create your views here.

def comparator(request):
	try:
		user = request.user
	except:
		device = request.COOKIES['device']
		user, created = User.objects.get_or_create(device=device)

	compareItems, created = CompareItems.objects.get_or_create(user=user, complete=False)

	context = {'compareItems':compareItems}
	return render(request, 'comparaider/comparator.html', context)