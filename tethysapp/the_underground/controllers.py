from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import RangeSlider

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'the_underground/home.html', context)
