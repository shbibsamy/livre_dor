from django.shortcuts import render
from .forms import CommentForm
from .models import Comment


def home(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cmt = Comment()
            cmt.__setattr__('email', form.cleaned_data['email'])
            cmt.__setattr__('comment', form.cleaned_data['comment'])
            if Comment.objects.filter(email=cmt.email).filter(comment=cmt.comment).exists():
                message = 'Vous aimez vous répéter !'
            else:
                cmt.save()
                message = 'Merci !'
    else:
        message = 'Veuillez laisser votre commentaire.'
    data = Comment.objects.all().values
    context = {'form' : CommentForm, 'message' : message, 'data' : data}
    return render(request, 'index.html', context)