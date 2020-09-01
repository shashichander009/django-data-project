
from django.urls import path
from undata.views import home_view, problem1_view

app_name = 'undata'

urlpatterns = [
    path('', home_view, name='prob1'),
    path('prob1', problem1_view),
    # path('undata/prob2', render_initial_data, name='prob2'),
    # path('undata/prob3', dynamic_lookup_view, name='prob3'),
    # path('undata/prob4', product_delete_view, name='prob4'),
]
