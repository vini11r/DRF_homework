from rest_framework.serializers import ValidationError


def validate_links(value):
    if "youtube.com" not in value:
        raise ValidationError("Ссылки только на 'youtube.com'")
