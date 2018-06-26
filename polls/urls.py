from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name = "index"),
    path("<int:question_id>/",views.detail,name = "detail"),
    path("<int:question_id>/results/", views.results,name = "results"),
    path("<int:question_id>/vote/",views.vote, name = "vote"),
    url(r"^$",views.index,name = "index"),
    url(r"^(P<question_id>[0-9]+)/$",views.detail,name = "detail"),
    url(r"^(?P<question_id>[0-9]+)/results/$",views.results,name = "results"),
    url(r"^(?P<question_id>[0-9]+)/vote/$",views.vote,name = "vote"),
]
