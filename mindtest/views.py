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
    question = get_object_or_404(Question, pk=mindtest_id)

    return render(request, 'mindtest/detail.html', {'mindtest': mindtest, 'question':question})


def vote(request, mindtest_id):
    mindtest = get_object_or_404(Mindtest, pk=mindtest_id)
    question = get_object_or_404(Question, pk=mindtest_id)
    choice = get_object_or_404(Choice, pk=mindtest_id)
    choice.votes = 0
    try:
        # print(selected_choice1)
        # selected_choice2 = question.choice_set.get(pk=request.POST['2'])
        # print(selected_choice2)
        # selected_choice3 = question.choice_set.get(pk=request.POST['3'])
        # selected_choice4 = question.choice_set.get(pk=request.POST['4'])
        # selected_choice5 = question.choice_set.get(pk=request.POST['5'])
        # selected_choice1 = request.POST.get('1', '')


        selected_choice1 = request.POST.get('1', '')

        choice1 = Choice.objects.get(pk=int(selected_choice1))

        selected_choice2 = request.POST.get('2', '')

        choice2 = Choice.objects.get(pk=int(selected_choice2))
        print(selected_choice2)
        selected_choice3 = request.POST.get('3', '')

        choice3 = Choice.objects.get(pk=int(selected_choice3))
        selected_choice4 = request.POST.get('4', '')

        choice4 = Choice.objects.get(pk=int(selected_choice4))
        selected_choice5 = request.POST.get('5', '')

        choice5 = Choice.objects.get(pk=int(selected_choice5))


    except (KeyError, Choice.DoesNotExist):
        return render(request, 'mindtest/detail.html', {
            'mindtest': mindtest,
            'error_message': "You didn't select a choice."
        })


    # selected_choice1.save()
    # selected_choice2.votes += 1
    choice1.votes+=1
    print(choice1.votes)
    choice1.save()

    choice2.votes+=1
    choice2.save()

    choice3.votes+=1
    choice3.save()

    choice4.votes+=1
    choice4.save()

    choice5.votes+=1
    choice5.save()
    # selected_choice2.save()
    # selected_choice3.votes += 1
    # selected_choice3.save()
    # selected_choice4.votes += 1
    # selected_choice4.save()
    # selected_choice5.votes += 1
    # selected_choice5.save()

    return HttpResponseRedirect(reverse('mindtest:results', args=(mindtest.id,)))


def results(request, mindtest_id):
    mindtest = get_object_or_404(Mindtest, pk=mindtest_id)

    return render(request, 'mindtest/results.html', {'mindtest': mindtest})
