from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question,Choice
# Create your views here.



def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
    context = {"latest_question_list" : latest_question_list} #上下文
    return render(request,"first/index.html",context)

def choose(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {"question": question_id}
    return render(request,"first/detail.html",context)

def vote(request, question_id):
    return HttpResponse("vote")
