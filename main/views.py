from accounts.models import Users
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from . import models

app_name = 'main'
class NotesListView(ListView):
    """ класс выводит список заметок и пользователей """
    model = models.Notes
    paginate_by = 20
    template_name = 'index_blog.html'

    def get_context_data(self, **kwargs):
        context = super(NotesListView, self).get_context_data(**kwargs)
        context['users'] = Users.objects.all()
        return context


class NotesDetailView(DetailView):
    """ класс показывает детальную информацию """
    model = models.Notes
    template_name = 'detail_blog.html'
