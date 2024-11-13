from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
# 这里面都是funcs 来处理requests和response

# def january(requests):
#     return HttpResponse("Singing")


monthly_challenges = {
    'january':"singing everyday",
    'february':'happy happy happy',
    'march': 'eat meat everyday',
    'april': 'play football everyday',
    'may': 'learn django everyday',
    'june': 'leetcoding everyday',
    'july': 'eat meat everyday',
    'august': 'play table tennis everyday',
    'september': 'leetcoding and django everyday',
    'october': 'drinking everyday',
    'november':None,
    'december':None,
}

def index(requests):
    month_list = list(monthly_challenges.keys())
    
    # list_items  =""
    # for month in month_list:
    #     cap_month = month.capitalize()
    #     month_path = reverse('month-challenge', args = [month])
    #     list_items += f'<li><a href="{month_path}">{cap_month}</a></li>'
    #     # generates a new link for each month.  anchor tag.. list of strings
    
    # response_data = f"<ul>{list_items}</ul>"

    return render(requests, "challenges/index.html", {
        "months":month_list
    })

def monthlychallenge_by_num(requests, month):
    months = list(monthly_challenges.keys())
    if month > 12 or month <1:
        return HttpResponseNotFound("Invalid Month")
    redirected_month = months[month-1]
    redirected_path = reverse('month-challenge', args = [redirected_month])         #获得url的name()
    return HttpResponseRedirect(redirected_path)

def monthlychallenge(requests, month):
    challenge_text = None 
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f"<h1>{challenge_text}</h1>"

        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(requests, "challenges/challenge.html", {
            "text":challenge_text,
            "month_name":month
        }) #必须有first argument

    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
