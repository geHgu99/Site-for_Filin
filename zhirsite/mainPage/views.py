from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Measurements
from .forms import UserForm


class WelcomeView(View):
    @staticmethod
    def get(request):
        return render(
            request, 'mainPage/main.html'
        )

    @staticmethod
    def post(request):
        current_weight = request.POST.get('current_weight')
        current_data = request.POST.get('current_data')
        db = Measurements(
            weight=current_weight,
            data=current_data
        )
        db.save()
        return redirect('/graph')


class GraphView(View):
    @staticmethod
    def get(request):
        db = Measurements.measure.all()
        context = {
            'base': db
        }
        return render(request, 'mainPage/graph.html', context=context)

    @staticmethod
    def post(request):
        _ = request.POST.get('somebody')
        return redirect('/main')


class TryView(View):
    @staticmethod
    def get(request):
        id = request.GET.get("id", 112)
        context = {
            "id": id
        }
        return render(request, 'mainPage/try.html', context=context)


class FormView(View):
    @staticmethod
    def get(request):
        userform = UserForm()
        data = {
            "form": userform
        }
        return render(request, 'mainPage/index.html', context=data)

    @staticmethod
    def post(request):
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            measure = userform.cleaned_data["measure"]
            return HttpResponse("<h2>Hello, {0}</h2>".format(name))
        else:
            return HttpResponse("Invalid data")