from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

from projects.forms import ProjectCreationForm
from projects.models import Project


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projects/create.html'

    def get_success_url(self):
        return reverse('projects:detail', kwargs={'pk':self.object.pk})

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projects/detail.html'

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projects/list.html'
    paginate_by = 25