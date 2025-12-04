from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
import json


class StoryListView(ListView):
    """
    Class-based view to show the Story list template
    """
    template_name = 'researchdata/story-list.html'
    queryset = models.Story.objects.filter(published=True).order_by('group')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['storygroups'] = models.StoryGroup.objects.all()
        return context


class StoryDetailView(DetailView):
    """
    Class-based view to show the Story detail template
    """
    template_name = 'researchdata/story-detail.html'
    queryset = models.Story.objects.filter(published=True)


class ResourceEducationListView(ListView):
    """
    Class-based view to show the Resource (Education) list template
    """
    template_name = 'researchdata/resource-list.html'

    def get_queryset(self):
        queryset = models.Resource.objects.filter(
            strand__name__iexact='education',
            published=True
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_subtitle'] = 'Education'
        return context


class ResourcePolicyListView(ListView):
    """
    Class-based view to show the Resource (Policy) list template
    """
    template_name = 'researchdata/resource-list.html'

    def get_queryset(self):
        queryset = models.Resource.objects.filter(
            strand__name__iexact='policy',
            published=True
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_subtitle'] = 'Policy'
        return context


class ResourceMensMentalHealthListView(ListView):
    """
    Class-based view to show the Resource (Men's Mental Health) list template
    """
    template_name = 'researchdata/resource-list.html'

    def get_queryset(self):
        queryset = models.Resource.objects.filter(
            strand__name__iexact="men's mental health",
            published=True
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_subtitle'] = "Men's Mental Health"
        return context


@csrf_exempt 
def resource_feedback_create(request):
    if request.method == 'POST':
        resource_id = request.POST.get('resourceId')
        feedback = request.POST.get('feedback')
        if resource_id and feedback:
            models.ResourceFeedback.objects.create(resource_id=resource_id, feedback=feedback)
            return JsonResponse({'status': 'success', 'message': 'Feedback saved successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Missing textData field'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
