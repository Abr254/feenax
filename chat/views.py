# chat/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message

@login_required
def chat(request):
    # Fetch the user instance correctly based on the logged-in user
    user = request.user

    # Initialize the message form
    form = MessageForm()

    # Handle message creation if the form is submitted via POST
    if request.method == 'POST':
        form = MessageForm(request.POST)
        
        if form.is_valid():
            # Ensure you're associating the correct user object
            message = form.save(commit=False)
            message.user = user  # Associate the logged-in user
            message.save()
            return redirect('chat')  # Redirect to avoid resubmission of the form

    # Render the chat page (could include messages, form, etc.)
    messages = Message.objects.all()  # You can filter messages as needed
    return render(request, 'chat.html', {'form': form, 'messages': messages})