from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("testing!")


def detail(request, question_id):
    return HttpResponse("this is the detail vew of the question %s" % question_id)


def results(request, question_id):
    return HttpResponse("this are the results of the question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("vote on question %s" % question_id)
