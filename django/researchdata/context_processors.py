from .models import ResourceStrand


def resources_navigation_menu(request):
    resource_strands = ResourceStrand.objects.filter(published=True).order_by('navigation_link_order')

    return {
        'resource_strands': resource_strands
    }
