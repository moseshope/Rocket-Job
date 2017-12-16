from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import ProfileEmp, ProfileFree
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Job
from message.models import Message
import requests
from bs4 import BeautifulSoup


# Create your views here.


def ScraperView(request):
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



    all_jobs = Job.objects.all()

    url = "https://www.freelancer.com/jobs/regions/?keyword=web%20development#"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    # final product
    g_data = soup.find_all("div", {"class": "JobSearchCard-primary"})
    swebsite = 'freelancer.com'
    i = 0

    try:
        for item in g_data:
            if i == 5:
                break
            else:
                stitle = item.contents[1].find_all("a", {"class": "JobSearchCard-primary-heading-link"})[0].text
                slink = item.contents[1].find_all("a", {"class": "JobSearchCard-primary-heading-link"})[0].get("href")
                stime = item.contents[1].find_all("span", {"class": "JobSearchCard-primary-heading-Days"})[0].text
                sdescription = item.contents[3].text
                sskill = item.contents[5].text.replace('\n', '  ')
                sbudget = item.contents[7].text.replace('\n', ' ')


                for job in all_jobs:
                    if slink == job.link:
                        found = True
                        break
                    else:
                        found = False

                if not found :
                    #adding data to database
                    Job.objects.create(website=swebsite, title=stitle, link=slink, short_text=sdescription, time=stime, skill=sskill, budget=sbudget)
                else:
                    pass

            i+=1
    except:
        pass

    #calling all data from database
    all_jobs = Job.objects.all().order_by('-created_date')
    #all_jobs = Job.objects.filter('created_date')

    #pagination
    paginator = Paginator(all_jobs, 10) # Show 10 jobs per page
    page = request.GET.get('page')
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        jobs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        jobs = paginator.page(paginator.num_pages)


    context = {
        'all_jobs': all_jobs,
        'jobs': jobs,
        'name': name,
        'emp_user': emp_user,
        'free_user': free_user,
        'all_messages': all_messages,
        'count_message_e': count_message_e,
        
    }

    return render(request, 'scraper/ScraperView.html', context)
