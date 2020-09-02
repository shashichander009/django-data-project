
from django.urls import path
from undata.views import problem1_view, problem2_view, problem3_view, problem4_view
from undata.response import problem1_response, problem2_response, problem3_response, problem4_response

app_name = 'undata'

urlpatterns = [
    path('', problem1_view),

    path('prob1', problem1_view, name='prob1'),
    path('prob1response', problem1_response),

    path('prob2', problem2_view, name='prob2'),
    path('prob2response', problem2_response),

    path('prob3', problem3_view, name='prob3'),
    path('prob3response', problem3_response),

    path('prob4', problem4_view, name='prob4'),
    path('prob4response', problem4_response),
]
