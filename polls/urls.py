from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("",views.list,name="index"),
    path('question/<int:id>',views.question,name="question"),
    path('tp',views.tp,name='tp'),
    path("show/<id>",views.show,name='show')
]
