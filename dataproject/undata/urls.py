
from django.urls import path
from undata.views import problem1_view, problem1_response

app_name = 'undata'

urlpatterns = [
    path('prob1', problem1_view, name='prob1'),
    path('prob1response', problem1_response),

    # path('prob2', problem1_view, name='prob1'),
    # path('prob2response', problem1_response),


    # path('undata/prob2', render_initial_data, name='prob2'),
    # path('undata/prob3', dynamic_lookup_view, name='prob3'),
    # path('undata/prob4', product_delete_view, name='prob4'),
]
