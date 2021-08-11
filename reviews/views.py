from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from members.decorators import person_required
from reviews.forms import ReviewCreation
from showcase.models import Glider
from .models import GliderReview


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

@person_required
def edit_review(request, pkg, pkr):

    user = request.user

    glider = Glider.objects.get(pk=pkg)
    review = glider.glider_review.get(pk=pkr)

    review = get_object_or_404(user.user_review, pk=review.pk)
    review = user.user_review.get(pk=review.pk)

    form = ReviewCreation(request.POST or None) #add



    if request.method == 'POST':
        form = ReviewCreation(request.POST, request.FILES, instance=review)

        if form.is_valid():
            form.save()

            return redirect('showcase:home')
        else:
            form = ReviewCreation()
    return render(request, 'reviews/edit_review.html', {'edit_review_form':form, 'glider':glider})