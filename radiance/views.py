from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join(q.question_text for q in latest_questions)
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("this is the detail vew of the question %s" % question_id)


def results(request, question_id):
    return HttpResponse("this are the results of the question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("vote on question %s" % question_id)

    # TODO: Pass variables DTL/Jinja2 to index.html
