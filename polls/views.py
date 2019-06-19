from django.shortcuts import render,get_object_or_404,redirect
from .models import Question,Choice
# Create your views here.

def list(request):
    questions = Question.objects.all()
    return render(request,"polls/index.html",{'questions':questions})

def question(request,id):
    res = get_object_or_404(Question,pk=id)
    return render(request,"polls/question.html",{'res':res})

def tp(request):
    if request.method == "POST":
        choice_id = request.POST['id']
        res = Choice.objects.filter(id=choice_id).all()
        if res:
            res[0].vote+=1
            res[0].save()
            return redirect("polls:show",id=res[0].id)

    return redirect("polls:index")

def show(request,id):
    res = get_object_or_404(Choice,pk=id)
    # res = Choice.objects.filter(id=id).all()
    return render(request,"polls/show.html",{'data':res.q})
