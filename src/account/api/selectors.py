from django.db.models.query import QuerySet
from django.contrib.auth import get_user_model, models


def user_list() -> QuerySet[models.User]:
    qs = get_user_model().objects.all()
    return qs