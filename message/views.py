from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from accounts.models import ProfileEmp, ProfileFree


# Create your views here.

@login_required
def message(request, user_id):
    user = User.objects.all()
    name = request.user


    all_messages = Message.objects.all()

    for message in all_messages:
        if name == message.post_user and message.viewed == False:
            message.viewed = True
            message.save()

    count_message_e = 0
    for message in all_messages:
        if name == message.post_user and message.viewed == False:
            count_message_e = count_message_e + 1


    free_all = ProfileFree.objects.all()
    emp_all = ProfileEmp.objects.all()

    for emp in emp_all:
        if name == emp.user:
            emp_user = True
            break
        else:
            emp_user = False

    for free in free_all:
        if name == free.user:
            free_user = True
            break
        else:
            free_user = False

    context = {
        'all_messages': all_messages,
        'count_message_e': count_message_e,
        'name': name,
        'user': user,
        'free_user': free_user,
        'emp_user': emp_user,
    }
    return render(request, 'message/message.html', context)
