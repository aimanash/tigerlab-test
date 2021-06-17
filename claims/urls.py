from django.urls import path

from . import views

urlpatterns = [
    path('accounts/view', views.ClaimList.as_view(), name='claim_list'),
    path('view/<int:pk>', views.ClaimDetail.as_view(), name='claim_view'),
    path('new', views.ClaimCreate.as_view(), name='claim_new'),
    path('edit/<int:pk>', views.ClaimUpdate.as_view(), name='claim_edit'),
    path('delete/<int:pk>', views.ClaimDelete.as_view(), name='claim_delete'),
]
