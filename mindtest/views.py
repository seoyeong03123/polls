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
    # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'mindtest/detail.html', {'mindtest': mindtest})


def vote(request, mindtest_id):
    mindtest = get_object_or_404(Mindtest, pk=mindtest_id)
    return HttpResponseRedirect(reverse('mindtest:results', args=(mindtest.id, )))


def results(request, mindtest_id):
    mindtest = get_object_or_404(Mindtest, pk=mindtest_id)
    return render(request, 'mindtest/results.html', {'mindtest': mindtest})
