from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Mindtest, Question, Choice


def index(request):
    latest_mindtest_list = Mindtest.objects.all().order_by('-pub_date')[:1]
    context = {'latest_mindtest_list': latest_mindtest_list}
    return render(request, 'mindtest/index.html', context)


def detail(request, mindtest_id):
    mindtest = get_object_or_404(Mindtest, pk=mindtest_id)
    return render(request, 'mindtest/detail.html', {'mindtest': mindtest})


def vote(request, mindtest_id):
    question = get_object_or_404(Question, pk=mindtest_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['question.id'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'mindtest/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('mindtest:results', args=(question.id, )))


def results(request, mindtest_id):
    mindtest = get_object_or_404(Mindtest, pk=mindtest_id)
    return render(request, 'mindtest/results.html', {'mindtest': mindtest})
