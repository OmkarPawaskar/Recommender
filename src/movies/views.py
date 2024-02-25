from typing import Any
from django.views import generic

# Create your views here.
from .models import Movie

class MovieListView(generic.ListView):
    template_name = "movies/list.html"
    paginate_by = 100
    # context -> object_list
    queryset = Movie.objects.all().order_by('-rating_avg')

    def get_context_data(self, *args, **kwargs):
        """
        This method is used to populate a dictionary to use as the template context. 
        For example, ListViews will populate the result from get_queryset() as object_list in the above example.
        You will probably be overriding this method most often to add things to display in your templates.
        """
        context =  super().get_context_data(*args, **kwargs)
        request = self.request
        user = request.user
        if user.is_authenticated:
            object_list = context['object_list']
            object_ids = [x.id for x in object_list]
            my_ratings = user.rating_set.movies().as_object_dict(object_ids=object_ids)
            context["my_ratings"] = my_ratings
        return context

movie_list_view = MovieListView.as_view()

class MovieDetailView(generic.ListView):
    template_name = "movies/detail.html"
    # context -> object -> id
    queryset = Movie.objects.all()

    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        request = self.request
        user = request.user
        if user.is_authenticated:
            object_list = context['object']
            object_ids = [object.id]
            my_ratings = user.rating_set.movies().as_object_dict(object_ids=object_ids)
            context["my_ratings"] = my_ratings
        return context

movie_detail_view = MovieDetailView.as_view()

