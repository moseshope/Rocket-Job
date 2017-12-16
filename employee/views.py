from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.utils import timezone
from django.contrib.auth.models import User
from .models import This_Job
from freelancer.models import Bid
from message.models import Message
from accounts.models import ProfileEmp, ProfileFree
from .forms import Add_Job_Form
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.


@login_required #used to protect views
def e_home(request):
    user = User.objects.all()
    name = request.user

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


    emp_all = ProfileEmp.objects.all()
    for emp in emp_all:
        if name == emp.user:
            this_user = True
            break
        else:
            this_user = False

    all_messages = Message.objects.all()
    count_message_e = 0

    for message in all_messages:
        if name == message.post_user and message.viewed == False:
            count_message_e = count_message_e + 1


    context = {
        'user': user,
        'name': name,
        'all_jobs': all_jobs,
        'jobs': jobs,
        'emp_all': emp_all,
        'this_user': this_user,
        'all_messages': all_messages,
        'count_message_e': count_message_e,

    }
    return render(request, 'employee/e_home.html', context)



@login_required
#def add_job(request, pk):
def add_job(request):
    #user = get_object_or_404(User, pk=pk)
    user = User.objects.all()

    name = request.user
    poster = request.user #get the currently logged in user
    if request.method == 'POST':
        form = Add_Job_Form(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = poster
            job.save()
            return redirect('employee:e_home')
    else:
        form = Add_Job_Form()

    emp_all = ProfileEmp.objects.all()
    for emp in emp_all:
        if name == emp.user:
            this_user = True
            break
        else:
            this_user = False

    all_messages = Message.objects.all()
    count_message_e = 0

    for message in all_messages:
        if name == message.post_user and message.viewed == False:
            count_message_e = count_message_e + 1


    context = {
        'username': poster,
        'form': form,
        'name': name,
        'this_user': this_user,
        'all_messages': all_messages,
        'count_message_e': count_message_e,

    }
    return render(request, 'employee/add_job.html', context)




@login_required
def profile(request, user_id):
    profile = get_object_or_404(User, pk=user_id)

    profile_emp = ProfileEmp.objects.get(user=profile)

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

    all_messages = Message.objects.all()
    count_message_e = 0

    for message in all_messages:
        if name == message.post_user and message.viewed == False:
            count_message_e = count_message_e + 1



    all_jobs = This_Job.objects.all()
    all_bids = Bid.objects.all()

    context = {
        'name': name,
        'user': user,
        'free_user': free_user,
        'emp_user': emp_user,
        'emp_all': emp_all,
        'profile': profile,
        'profile_emp': profile_emp,
        'all_jobs': all_jobs,
        'all_messages': all_messages,
        'count_message_e': count_message_e,

    }
    return render(request, 'employee/profile.html', context)


@login_required
def edit_profile(request, user_id):
    profile = get_object_or_404(User, pk=user_id)
    profile_emp = ProfileEmp.objects.get(user=profile)
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
        company = request.POST['company']
        website = request.POST['website']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        city = request.POST['city']
        country = request.POST['country']
        about = request.POST['about']

        profile.first_name = first_name
        profile.last_name = last_name
        profile_emp.company = company
        profile_emp.website = website
        profile_emp.address1 = address1
        profile_emp.address2 = address2
        profile_emp.city = city
        profile_emp.country = country
        profile_emp.about = about

        profile.save()
        profile_emp.save()

        return redirect('employee:profile', profile.id)

    all_messages = Message.objects.all()
    count_message_e = 0

    for message in all_messages:
        if name == message.post_user and message.viewed == False:
            count_message_e = count_message_e + 1


    context = {
        'profile': profile,
        'profile_emp': profile_emp,
        'name': name,
        'user': user,
        'free_user': free_user,
        'emp_user': emp_user,
        'all_messages': all_messages,
        'count_message_e': count_message_e,

    }
    return render(request, 'employee/edit_profile.html', context)
