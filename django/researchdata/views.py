from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models


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


class ResourceStrandDetailView(DetailView):
    """
    Class-based view to show the Resource Strand detail template
    """
    template_name = 'researchdata/resourcestrand-detail.html'
    queryset = models.ResourceStrand.objects.filter(published=True).prefetch_related('resources')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resources'] = self.object.resources.filter(published=True)
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
