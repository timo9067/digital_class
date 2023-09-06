from django.core.exceptions import ValidationError


def check_rating_range(value):
    if value < 0 or value > 5:
        raise ValidationError(f"Value should be in range 0...5")
