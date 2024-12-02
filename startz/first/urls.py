from django.urls import path

from . import views
app_name = "first"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/",views.choose, name="choose"),
    path("<int:question_id>/vote/",views.vote, name="vote"),
]