from django.views import View
from django.shortcuts import render, redirect

from .models import Measurements


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
        return render(request, '<h2>I learnt to use commits</h2>')