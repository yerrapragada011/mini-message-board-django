from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from django.utils import timezone

# Create your views here.

def index(request):
    messages = Message.objects.order_by('-added')
    return render(request, 'board/index.html', {'messages': messages})

def new_message(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        text = request.POST.get('text')
        Message.objects.create(user=user, text=text, added=timezone.now())
        return redirect('index')
    return render(request, 'board/new_message.html')

def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    return render(request, 'board/message_detail.html', {'message': message})