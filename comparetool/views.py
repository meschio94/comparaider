from django.shortcuts import render, redirect
from members.models import User
from .models import CompareItems, SizeItem

def comparator(request):
    try:
        user = request.user.user
    except:
        device = request.COOKIES['device']
        user, created = User.objects.get_or_create(device=device, username=device, email=device)

    compareItems, created = CompareItems.objects.get_or_create(user=user, complete=False)

    context = {'compareItems': compareItems}
    return render(request, 'comparaider/comparator.html', context)


def remove_size(request):
    if request.method == 'POST':
        sizeId = request.POST['sizeId']

        try:
            user = request.user.user
        except:
            device = request.COOKIES['device']
            user, created = User.objects.get_or_create(device=device)

        compareItems, created = CompareItems.objects.get_or_create(user=user, complete=False)
        sizeItem = SizeItem.objects.filter(id=sizeId).delete()



        return redirect('comparetool:compare')


    return render(request, 'comparaider/comparator.html')
