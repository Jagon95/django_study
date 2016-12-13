from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
from django.utils import timezone
from .strings import *
from .forms import NameForm, TestForm, QuestionForm, ChoiceForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = latest_question_list

    def get_queryset(self):
        """Return the last five published question. not including those set to be published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Excludes any questions that aren't published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        """Excludes any questions that aren't published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # selected_choice.votes += 1
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def like(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.likes = F('likes') + 1
    question.save()
    return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'polls/name.html', {'form': form})


def test_form(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            # print(form['question_text'])
            return HttpResponseRedirect('polls:index')
    else:
        form = TestForm

    return render(request, 'polls/test_form.html', {'form': form})


def test_form2(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        choice_form = ChoiceForm(request.POST)
        if question_form.is_valid() and choice_form.is_valid():
            question = question_form.save()
            choice = Choice(
                choice_text=choice_form.cleaned_data['choice_text'],
                question=question, )
            choice.save()
            # messages.success(request, _('Your profile was successfully updated!'))
            return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))
        # else:
            # messages.error(request, _('Please correct the error below.'))
    else:
        question_form = QuestionForm()
        choice_form = ChoiceForm()
    return render(request, 'polls/test_form2.html', {
        'question_form': question_form,
        'choice_form': choice_form
    })
