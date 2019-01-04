from django.http import HttpResponse
from django.template import loader
from .models import Message

def home(request):
    latest_question_list = Message.objects.order_by('created')[:5]
    print("==========")
    print(latest_question_list)
    print("==========")

    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse("Hello, Django!")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
