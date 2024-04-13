from .models import Report
import django_filters


class ReportFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Report
        fields = ['title',]