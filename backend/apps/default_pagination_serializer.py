from rest_framework import pagination


class DefaultPaginationSerializer(pagination.PageNumberPagination):
    page_size = 100
    max_page_size = 200
