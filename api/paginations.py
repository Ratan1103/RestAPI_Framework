from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page-num'
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_pagination_response(self,data):
        return response({
            'count':self.page.paginator.count,
            'next':self.get_next_link(),
            'previous':self.get_previous_link(),
            'page_size':self.page_size,
            'results':data
        })