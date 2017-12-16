from django.shortcuts import render
from django.contrib.auth.models import User
from message.models import Message
from accounts.models import ProfileEmp, ProfileFree


# Create your views here.



def index(request):
    user = User.objects.all()
    name = request.user
    emp_all = ProfileEmp.objects.all()
    free_all = ProfileFree.objects.all()

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

    all_messages = Message.objects.all()
    count_message_e = 0

    for message in all_messages:
        if name == message.post_user and message.viewed == False:
            count_message_e = count_message_e + 1


    context = {
        'emp_user': emp_user,
        'free_user': free_user,
        'name': name,
        'all_messages': all_messages,
        'count_message_e': count_message_e,

    }

    return render(request, 'appMarketplace/home.html', context)


def about(request):
    user = User.objects.all()
    name = request.user
    emp_all = ProfileEmp.objects.all()
    free_all = ProfileFree.objects.all()

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

    all_messages = Message.objects.all()
    count_message_e = 0

    for message in all_messages:
        if name == message.post_user and message.viewed == False:
            count_message_e = count_message_e + 1


    context = {
        'emp_user': emp_user,
        'free_user': free_user,
        'name': name,
        'all_messages': all_messages,
        'count_message_e': count_message_e,

    }

    return render(request, 'appMarketplace/about.html', context)


def contact_us(request):
    user = User.objects.all()
    name = request.user
    emp_all = ProfileEmp.objects.all()
    free_all = ProfileFree.objects.all()

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

    all_messages = Message.objects.all()
    count_message_e = 0

    for message in all_messages:
        if name == message.post_user and message.viewed == False:
            count_message_e = count_message_e + 1


    context = {
        'emp_user': emp_user,
        'free_user': free_user,
        'name': name,
        'all_messages': all_messages,
        'count_message_e': count_message_e,

    }

    return render(request, 'appMarketplace/contact_us.html', context)
