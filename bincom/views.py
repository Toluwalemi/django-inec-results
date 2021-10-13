from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView

from helpers.queryset import get_state_data
from .models import PollingUnit, AnnouncedPuResults


class HomePageView(TemplateView):
    template_name = 'bincom/home.html'


def polling_unit_view(request):
    """
    Function to display results for any individual polling unit.
    Specifically for Delta with id=25
    @return:
    @rtype:
    """
    qs = get_state_data(25)
    states = qs.get('state', '')
    lga = qs.get('lga', '')
    ward = qs.get('ward', '')
    pollings = qs.get('pollings', '')
    c = {'states': states, 'lga': lga, 'ward': ward,
         'pollings': pollings, 'action_type': 'unit', 'bool': True}

    if request.method == "POST":
        unit_id = request.POST['unit']
        polling_unit = PollingUnit.objects.filter(uniqueid=unit_id)[0]
        polling_results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=unit_id)
        c.update({'results': polling_results, 'polling_unit': polling_unit})
    else:
        return render(request, 'bincom/dashboard.html', c)

    return render(request, 'bincom/dashboard.html', c)
