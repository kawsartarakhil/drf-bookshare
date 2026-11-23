from rest_framework.pagination import PageNumberPagination

class Custompagination(PageNumberPagination):
    page_query_param = 'p'
    