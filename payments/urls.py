from django.urls import path
from . import views

urlpatterns = [
    path('create-wallet/', views.create_wallet, name='create_wallet'),
    path('view-wallet/', views.view_wallet, name='view_wallet'),
	path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
	path('verify-payment/<str:ref>/', views.verify_payment, name='verify_payment'),
]