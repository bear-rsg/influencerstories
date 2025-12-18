from django.db import models
from django.urls import reverse
from django.db.models.functions import Upper
from django.utils.text import slugify


class StoryGroup(models.Model):
    """
    A group/category of a Story
    """

    related_name = 'story_groups'

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = [Upper('name'), 'id']


class Story(models.Model):
    """
    The primary model. Contains data about users' Stories of their mental health
    """

    related_name = 'stories'

    title = models.CharField(max_length=255, unique=True)
    group = models.ForeignKey(StoryGroup, related_name=related_name, on_delete=models.RESTRICT)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='researchdata-stories', blank=True, null=True)
    video_youtube_id = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Video (YouTube ID)',
        help_text="This can be found in the video URL. E.g. 'daUQPN5A2zA' in 'www.youtube.com/watch?v=daUQPN5A2zA'"
    )
    author_name = models.CharField(max_length=200, blank=True, null=True)
    author_name_show = models.BooleanField(default=True, help_text="Ticking this box will show the author's name on the public interface")
    published = models.BooleanField(default=True, help_text='Only published stories will appear on the public interface')
    admin_notes = models.TextField(blank=True, null=True, help_text='Optional. Used for internal notes. Only visible on this page and will not appear on public website.')
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('researchdata:story-detail', args=[str(self.id)])

    class Meta:
        ordering = [Upper('title'), 'id']
        verbose_name_plural = 'stories'


class ResourceStrand(models.Model):
    """
    A strand/category of Resource
    """

    related_name = 'resource_strands'

    name = models.CharField(max_length=255, unique=True)
    navigation_link_name = models.CharField(max_length=255, unique=True)
    navigation_link_order = models.IntegerField(default=0)
    introduction = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    published = models.BooleanField(default=True, help_text='Only published resource strands will appear on the public interface')
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('researchdata:resourcestrand-detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.navigation_link_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.navigation_link_name


class Resource(models.Model):
    """
    An downloadable resource (e.g. PDF)
    """

    related_name = 'resources'

    strand = models.ForeignKey(ResourceStrand, related_name=related_name, on_delete=models.RESTRICT)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='researchdata-resources', blank=True, null=True)
    video_youtube_id = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Video (YouTube ID)',
        help_text="This can be found in the video URL. E.g. 'daUQPN5A2zA' in 'www.youtube.com/watch?v=daUQPN5A2zA'"
    )
    url = models.URLField(blank=True, null=True)
    request_feedback = models.BooleanField(default=False, help_text='Check to display feedback box from users for this resource')
    published = models.BooleanField(default=True, help_text='Only published resources will appear on the public interface')
    admin_notes = models.TextField(blank=True, null=True, help_text='Optional. Used for internal notes. Only visible on this page and will not appear on public website.')
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = [Upper('title'), 'id']


class ResourceFeedback(models.Model):
    """
    A comment/feedback from a user about a Resource
    """

    related_name = 'resource_feedbacks'

    resource = models.ForeignKey(Resource, related_name=related_name, on_delete=models.RESTRICT)
    feedback = models.TextField()
    admin_notes = models.TextField(blank=True, null=True, help_text='Optional. Used for internal notes. Only visible on this page and will not appear on public website.')
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Resource Feedback #{self.id}'

    class Meta:
        verbose_name_plural = 'resource feedback'


class FileUpload(models.Model):
    """
    A file (e.g. image, pdf) uploaded so can be used somewhere on the website
    """

    file = models.FileField(upload_to='researchdata-files')
    admin_notes = models.TextField(blank=True, null=True, help_text='Optional. Used for internal notes. Only visible on this page and will not appear on public website.')
    created = models.DateTimeField(auto_now_add=True)

    @property
    def url(self):
        return self.file.url

    def __str__(self):
        return f'File: #{self.id}'
