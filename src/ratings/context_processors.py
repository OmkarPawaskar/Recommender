"""
In Django, context processors are functions that are executed before rendering a template, 
and they add specific data to the context that is available to every template in your project. 
They provide a way to include common context variables across multiple views, making it easier to share data with templates without duplicating code in each view.
"""
from .models import RatingChoice

def rating_choices(request):
    return {
        "rating_choices" : RatingChoice.values
    }