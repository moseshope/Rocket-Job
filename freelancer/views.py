from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import ProfileEmp, ProfileFree
from employee.models import This_Job
from freelancer.models import Bid
from message.models import Message
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


@login_required
def f_home(request):
    user = User.objects.all()
    name = request.user
    free_all = ProfileFree.objects.all()

    for free in free_all:
        if name == free.user:
            this_user = True
            break
        else:
            this_user = False

    all_jobs = This_Job.objects.all().order_by('-created_date')

    #pagination
    paginator = Paginator(all_jobs, 5) # Show 10 jobs per page
    page = request.GET.get('page')
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        jobs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        jobs = paginator.page(paginator.num_pages)

    all_messages = Message.objects.all()
    count_message_e = 0

    for message in all_messages:
        if name == message.post_user and message.viewed == False:
            count_message_e = count_message_e + 1


    context = {
        'name': name,
        'this_user': this_user,
        'all_jobs': all_jobs,
        'jobs': jobs,
        'all_messages': all_messages,
        'count_message_e': count_message_e,

    }

    return render(request, 'freelancer/f_home.html', context)


@login_required
def profile(request, user_id):
    profile = get_object_or_404(User, pk=user_id)
    profile_free = ProfileFree.objects.get(user=profile)
    user = User.objects.all()
    name = request.user

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


    all_jobs = This_Job.objects.all()
    all_bids = Bid.objects.all()

    all_messages = Message.objects.all()
    count_message_e = 0

    for message in all_messages:
        if name == message.post_user and message.viewed == False:
            count_message_e = count_message_e + 1


    context = {
        'name': name,
        'user': user,
        'free_user': free_user,
        'emp_user': emp_user,
        'emp_all': emp_all,
        'profile': profile,
        'profile_free': profile_free,
        'all_jobs': all_jobs,
        'all_bids': all_bids,
        'all_messages': all_messages,
        'count_message_e': count_message_e,

    }
    return render(request, 'freelancer/profile.html', context)


@login_required
def edit_profile(request, user_id):
    profile = get_object_or_404(User, pk=user_id)
    profile_free = ProfileFree.objects.get(user=profile)
    user = User.objects.all()
    name = request.user

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

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        portfolio = request.POST['portfolio']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        city = request.POST['city']
        country = request.POST['country']
        about = request.POST['about']

        profile.first_name = first_name
        profile.last_name = last_name
        profile_free.portfolio = portfolio
        profile_free.address1 = address1
        profile_free.address2 = address2
        profile_free.city = city
        profile_free.country = country
        profile_free.about = about

        profile.save()
        profile_free.save()

        return redirect('freelancer:profile', profile.id)

    all_messages = Message.objects.all()
    count_message_e = 0

    for message in all_messages:
        if name == message.post_user and message.viewed == False:
            count_message_e = count_message_e + 1


    context = {
        'profile': profile,
        'profile_free': profile_free,
        'name': name,
        'user': user,
        'free_user': free_user,
        'emp_user': emp_user,
        'all_messages': all_messages,
        'count_message_e': count_message_e,

    }
    return render(request, 'freelancer/edit_profile.html', context)
