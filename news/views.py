from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt


def welcome(request):
    return render(request, 'welcome.html')


# def convert_dates(dates):
#     day_number = dt.date.weekday(dates)
#     days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', "Sunday"]
#     day = days[day_number]
#     return day


def news_today(request):
    date = dt.date.today()

    return render(request, 'all-news/today-news.html', {"date": date})


def past_day_news(request, past_date):
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(news_today())

    return render(request, 'all-news/past-news.html', {"date": date})


