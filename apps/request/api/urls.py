from django.urls import path
from apps.request.api.views import DatesTimesAlgorithm, MyTokenObtainPairView
#DateTimeAlgorithm, DateAlgorithm, TimeAlgorithm, 



urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('<slug:algoritmo>/', DatesTimesAlgorithm.as_view(), name='search_dates_times'),
    #path('search-dates-times/', DatesTimesAlgorithm.as_view(), name='search_dates_times'),
    #path('search-date-time/', DateTimeAlgorithm.as_view(), name='search_date_time'),
    #path('search-date/', DateAlgorithm.as_view(), name='search_date_time'),
    #path('search-time/', TimeAlgorithm.as_view(), name='search_date_time'),
]