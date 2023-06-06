from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index_name, name="index"),
    path('detail/',views.detail_name, name = "detail"),
    path('create/',views.new_product, name = "create"),
]