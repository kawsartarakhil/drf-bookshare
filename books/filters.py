import django_filters

class BookFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(field_name="author",lookup_expr="icontains")
    category = django_filters.CharFilter(field_name="category",lookup_expr="icontains")