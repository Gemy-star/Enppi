import django_filters
from .models import *
from django_filters import CharFilter


class RatingFilter(django_filters.FilterSet):
    name_part = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Rating
        fields = ['date_added','itstaff' , 'rating']
