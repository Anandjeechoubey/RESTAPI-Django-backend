from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('branches/', views.ByCityListView.as_view(), name='branches'),
    path('branches/autocomplete/', views.ByBranchListView.as_view(), name='branches'),
    # re_path(r'^branches/(?P<q>\w+)/$', views.getBranches, name='branches'),
    # path('branches/?q=<:var>', views.getBranches, name='branches'),
    path('summary/', views.getSummary, name='summary'),
]