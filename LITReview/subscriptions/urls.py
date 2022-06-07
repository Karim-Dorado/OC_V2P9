from django.urls import path
from .views import SubscriptionDeleteView

from. import views


urlpatterns = [
    path('subscriptions', views.subscriptions, name='subscriptions'),
    path('<int:pk>/unsuscribe',
         SubscriptionDeleteView.as_view(),
         name='unsuscribe')
]