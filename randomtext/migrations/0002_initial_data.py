from django.db import migrations


def create_sample_texts(apps, schema_editor):
    ShortText = apps.get_model('randomtext', 'ShortText')
    sample_texts = [
        'Try something new',
        'Take a short walk',
        'Write a quick note',
        'Call a friend now',
        'Read one page',
        'Drink some water',
        'Smile at a stranger',
    ]
    for text in sample_texts:
        ShortText.objects.create(text=text)


def delete_sample_texts(apps, schema_editor):
    ShortText = apps.get_model('randomtext', 'ShortText')
    ShortText.objects.filter(text__in=[
        'Try something new',
        'Take a short walk',
        'Write a quick note',
        'Call a friend now',
        'Read one page',
        'Drink some water',
        'Smile at a stranger',
    ]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('randomtext', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_texts, delete_sample_texts),
    ]
