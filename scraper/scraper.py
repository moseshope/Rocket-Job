# scraping recent posted jobs data from https://www.freelancer.com

from models import Job
import requests
from bs4 import BeautifulSoup


url = "https://www.freelancer.com/jobs/regions/?keyword=web%20development#"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")


#g_data = soup.find_all("div", {"class": "JobSearchCard-primary"})
#for item in g_data:
#    print(item.contents[1].find_all("a", {"class": "JobSearchCard-primary-heading-link"})[0].text)
#    print(item.contents[1].find_all("span", {"class": "JobSearchCard-primary-heading-Days"})[0].text)
#    print(item.contents[3].text)
#    print(item.contents[5].text.replace('\n', '  '))
#    print(item.contents[7].text.replace('\n', ' '))



# final product
g_data = soup.find_all("div", {"class": "JobSearchCard-primary"})
swebsite = 'freelancer.com'
i = 0

try:
    for item in g_data:
        if i == 3: #get 3 items
            break
        else:
            stitle = item.contents[1].find_all("a", {"class": "JobSearchCard-primary-heading-link"})[0].text
            stime = item.contents[1].find_all("span", {"class": "JobSearchCard-primary-heading-Days"})[0].text
            sdescription = item.contents[3].text
            sskill = item.contents[5].text.replace('\n', '  ')
            sbudget = item.contents[7].text.replace('\n', ' ')

            for job in all_jobs: #if item is already in the database
                if sdescription == job.short_text and sskill == job.skill:
                    found = True
                    break
                else:
                    found = False

            if not found :
                #adding data to database
                Job.objects.create(website=swebsite, title=stitle, short_text=sdescription, time=stime, skill=sskill, budget=sbudget)
            else:
                pass
        i+=1
except:
    pass




#######################################################



# scraping recent posted jobs data from https://www.upwork.com
# unfortunately, upwork is not giving permission to access their job list data

from models import Job
import requests
from bs4 import BeautifulSoup


url = "https://www.upwork.com/o/jobs/browse/c/web-mobile-software-dev/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

g_data = soup.find_all("div", {"class": "col-md-12"})
swebsite = 'Upwork.com'
