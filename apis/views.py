from collections import defaultdict
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Branch
from rest_framework import generics, filters

from .serializers import BranchSerializer
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/branches?q=<>',
        '/branches/autocomplete?q=<>',
    ]
    return Response(routes)

@api_view(['GET'])
def getBranches(self):
    branches = Branch.objects.filter(id__lte=50)
    serializer = BranchSerializer(branches, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSummary(self):
    data_length = len(Branch.objects.all())
    return Response(data_length)

class ByCityListView(generics.ListAPIView):
    queryset = Branch.objects.all().order_by('ifsc')
    serializer_class = BranchSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['city']

    def get_queryset(self):
        """
        Optionally restricts the queryset by filtering against
        query parameters in the URL.
        """
        query_params = self.request.query_params
        q = query_params.get('q', '')
        limit = int(query_params.get('limit', 10))
        offset = int(query_params.get('offset', 0))
        queryset = Branch.objects.filter( city__icontains = q).order_by('ifsc')[offset: offset + limit]
        print(query_params, limit, offset)
        return queryset

class ByBranchListView(generics.ListAPIView):
    queryset = Branch.objects.all().order_by('ifsc')
    serializer_class = BranchSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['branch']

    def get_queryset(self):
        """
        Optionally restricts the queryset by filtering against
        query parameters in the URL.
        """
        query_params = self.request.query_params
        q = query_params.get('q', '')
        limit = int(query_params.get('limit', 10))
        offset = int(query_params.get('offset', 0))
        queryset = Branch.objects.filter( branch__icontains = q).order_by('ifsc')[offset: offset + limit]
        print(query_params, limit, offset)
        return queryset

        # This dict will hold filter kwargs to pass in to Django ORM calls.
        # db_filters = {}
        # # update filters dict with incoming query params and then pass as
        # # **kwargs to queryset.filter()
        # db_filters.update(
        #     self.get_queryset_filters(
        #         query_params
        #     )
        # )
        # return queryset.filter(**db_filters)