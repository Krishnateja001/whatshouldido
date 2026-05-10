from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ShortText


def random_text_page(request):
    """Render the React page for displaying random text."""
    return render(request, 'random_text.html')


@api_view(['GET'])
def random_text(request):
    text = ShortText.objects.order_by('?').first()
    if not text:
        return Response({'detail': 'No short texts available.'}, status=404)

    return Response({'text': text.text})
