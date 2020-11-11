from django.shortcuts import render, get_object_or_404
# from .forms import CreatePollForm
from .models import Question, Vote
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.views import View


class QuestionListView(ListView):
    model = Question
    context_object_name = 'question'
    template_name = 'docspoll/home.html'


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'docspoll/result.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.vote_set.get(pk=request.POST['choice'])

    except(KeyError, Vote.DoesNotExist):
        return render(request, 'docspoll/result.html', {
            'question': question,
            'error_message': 'You didnot select the choice.'
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('vote', args=(question.id,)))


class ChartView(ListView):
    model = Vote
    context_object_name = 'objects'
    template_name = 'docspoll/chartjs.html'


    

class FlotView(ListView):
    model = Vote
    context_object_name = 'objects'
    template_name = 'docspoll/flot.html'

def lte(request):
    return render(request, 'index.html')