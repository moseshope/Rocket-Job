from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from employee.models import This_Job
from freelancer.models import Bid
from message.models import Message
from django.contrib.auth.models import User
from accounts.models import ProfileEmp, ProfileFree
from freelancer.forms import Bid_Form
from employee.forms import Add_Job_Form

# Create your views here.

@login_required
def job_details(request, job_id):
    job = get_object_or_404(This_Job, pk=job_id)
    user = User.objects.all()
    name = request.user

    all_bids = Bid.objects.all()

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


    #submit bid form
    if request.method == 'POST':
        form = Bid_Form(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.bid_poster = name
            bid.job = job
            bid.save()

            Message.objects.create(post_user=job.user, comment_user=name, job=job)

            #return redirect('details:job_details')
            return HttpResponseRedirect(request.path_info)
    else:
        form = Bid_Form()


    count_bid = 0

    for bid in all_bids:
        if job == bid.job:
            count_bid = count_bid+1

    for bid in all_bids:
        if job == bid.job and name == bid.bid_poster:
            bid_limit = True
            break
        else:
            bid_limit = False

    all_messages = Message.objects.all()
    count_message_e = 0

    for message in all_messages:
        if name == message.post_user and message.viewed == False:
            count_message_e = count_message_e + 1


    context = {
        'form': form,
        'user': user,
        'job': job,
        'name': name,
        'all_bids': all_bids,
        'count_bid': count_bid,
        'bid_limit': bid_limit,
        'emp_user': emp_user,
        'free_user': free_user,
        'all_messages': all_messages,
        'count_message_e': count_message_e,

    }
    return render(request, 'details/job_details.html', context)


@login_required
def edit_job(request, job_id):
    job = get_object_or_404(This_Job, pk=job_id)

    user = User.objects.all()
    name = request.user

    all_jobs = This_Job.objects.all()

    if request.method == 'POST':

        title = request.POST['title']
        short_text = request.POST['short_text']
        time = request.POST['time']
        skill = request.POST['skill']
        budget = request.POST['budget']

        job.title = title
        job.short_text = short_text
        job.time = time
        job.skill = skill
        job.budget = budget
        job.user = name
        job.save()
        return redirect('details:job_details', job.id)
        #return HttpResponseRedirect(request.path_info)

    else:
        form = Add_Job_Form()



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
        'user': user,
        'name': name,
        'all_jobs': all_jobs,
        'job': job,
        'free_user': free_user,
        'emp_user': emp_user,
        'all_messages': all_messages,
        'count_message_e': count_message_e,

    }
    return render(request, 'details/edit_job.html', context)



@login_required
def edit_bid(request, bid_id):
    bid = get_object_or_404(Bid, pk=bid_id)

    user = User.objects.all()
    name = request.user

    job = bid.job
    #submit bid form
    if request.method == 'POST':

        bid_text = request.POST['bid_text']
        bid_time = request.POST['bid_time']
        bid_budget = request.POST['bid_budget']

        bid.bid_text = bid_text
        bid.bid_time = bid_time
        bid.bid_budget = bid_budget
        bid.bid_poster = name
        bid.job = job
        bid.save()
        return redirect('details:job_details', job.id)
        #return HttpResponseRedirect(request.path_info)

    else:
        form = Bid_Form()



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
        'name': name,
        'free_user': free_user,
        'emp_user': emp_user,
        'bid': bid,
        'job': job,
        'all_messages': all_messages,
        'count_message_e': count_message_e,
        
    }
    return render(request, 'details/edit_bid.html', context)
