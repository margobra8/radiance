from django.conf.urls import url
from . import views

urlpatterns = [

    url(r"^$", views.index, name="index"),
    # host.com/polls/
    url(r"^(?P<question_id>[0-9]+)/$", views.detail, name="detail"),
    # host.com/polls/2
    url(r"^(?P<question_id>[0-9]+)/results$", views.results, name="results"),
    # host.com/polls/2/results
    url(r"^(?P<question_id>[0-9]+)/vote$", views.vote, name="vote"),
    # host.com/polls/2/vote
]
