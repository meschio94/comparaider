from django.shortcuts import render, redirect

# Create your views here.
from members.decorators import person_required
from reviews.forms import ReviewCreation
from showcase.models import Glider


@person_required
def add_review(request, pk):

    form = ReviewCreation(request.POST or None) #add
    glider = Glider.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewCreation(request.POST, request.FILES)

        if form.is_valid():
            Review = form.save(commit=False)
            user = request.user
            Review.user = user
            Review.glider = glider
            Review.save()

            return redirect('showcase:home')
        else:
            form = ReviewCreation()
    return render(request, 'reviews/add_review.html', {'add_review_form':form, 'glider':glider})