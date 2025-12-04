from django.contrib import admin
from . import models


# Actions


def publish(modeladmin, request, queryset):
    """
    Sets all selected objects in queryset to published
    """
    queryset.update(published=True)


publish.short_description = "Publish selected items (will appear on main site)"


def unpublish(modeladmin, request, queryset):
    """
    Sets all selected objects in queryset to not published
    """
    queryset.update(published=False)


unpublish.short_description = "Unpublish selected items (will not appear on main site)"


# ModelAdmins


@admin.register(models.StoryGroup)
class StoryGroupAdminView(admin.ModelAdmin):
    """
    Customise the admin interface for StoryGroup model
    """

    list_display = ('name',)
    search_fields = ('name',)


@admin.register(models.Story)
class StoryAdminView(admin.ModelAdmin):
    """
    Customise the admin interface for Story model
    """

    list_display = (
        'title',
        'author_name',
        'published',
        'created',
        'last_updated'
    )
    search_fields = (
        'title',
        'group__name',
        'text',
        'author_name',
        'admin_notes',
    )
    list_filter = ('published', 'group')
    readonly_fields = ('created', 'last_updated')
    actions = (publish, unpublish)

    def get_actions(self, request):
        """
        Remove 'delete' action
        """
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(models.ResourceStrand)
class ResourceStrandAdminView(admin.ModelAdmin):
    """
    Customise the admin interface for ResourceFeedback model
    """

    list_display = ('name', 'created', 'last_updated')
    search_fields = ('name',)

    def get_actions(self, request):
        """
        Remove 'delete' action
        """
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(models.Resource)
class ResourceAdminView(admin.ModelAdmin):
    """
    Customise the admin interface for Resource model
    """

    list_display = (
        'title',
        'strand',
        'file',
        'url',
        'published',
        'created',
        'last_updated'
    )
    search_fields = (
        'title',
        'description',
        'file',
        'url',
        'questionnaire',
        'author_name',
        'admin_notes',
    )
    list_filter = ('strand', 'published',)
    readonly_fields = ('created', 'last_updated')
    actions = (publish, unpublish)

    def get_actions(self, request):
        """
        Remove 'delete' action
        """
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(models.ResourceFeedback)
class ResourceFeedbackAdminView(admin.ModelAdmin):
    """
    Customise the admin interface for ResourceFeedback model
    """

    list_display = ('feedback', 'resource', 'created', 'last_updated')
    search_fields = ('resource__title', 'feedback')
    list_filter = ('resource',)

    def get_actions(self, request):
        """
        Remove 'delete' action
        """
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
