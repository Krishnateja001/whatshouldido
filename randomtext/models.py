from django.core.exceptions import ValidationError
from django.db import models


def validate_short_text(value):
    if len(value.split()) > 6:
        raise ValidationError('Text must contain at most 6 words.')


class ShortText(models.Model):
    text = models.CharField(max_length=120, validators=[validate_short_text])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='shorttext'
        
    def __str__(self):
        return self.text
