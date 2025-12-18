from django.db import migrations
from .. import models


def insert_resource_strands(apps, schema_editor):
    """
    Inserts default ResourceStrand data
    """

    objects = [
        {
            'name': 'Resources for Educators',
            'navigation_link_name': 'Education',
            'navigation_link_order': 1,
            'introduction': 'Introduction...',
        },
        {
            'name': 'Resources for Policy Makers',
            'navigation_link_name': 'Policy',
            'navigation_link_order': 2,
            'introduction': 'Introduction...',
        },
        {
            'name': "Men's Mental Health Resources",
            'navigation_link_name': "Men's Mental Health",
            'navigation_link_order': 3,
            'introduction': 'Introduction...',
        },
        {
            'name': 'Resources for Parents and Carers',
            'navigation_link_name': 'Parents and Carers',
            'navigation_link_order': 4,
            'introduction': 'Introduction...',
        },
    ]
    for object in objects:
        models.ResourceStrand.objects.create(**object)


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0001_initial'),
    ]


    operations = [
        migrations.RunPython(insert_resource_strands),
    ]
