from django.urls import path,include
from . import views


urlpatterns = [
    path('statement/', views.Statement.as_view(), name='statement'),
    path('deposit/', views.Deposit.as_view(), name='deposit'),
    path('withdraw/', views.Withdraw.as_view(), name='withdraw'),
    path('transfer_money/', views.TransferMoney.as_view(), name='transfer_money'),
    path('loan_request/', views.Loan.as_view(), name='loan_request'),
    # path('deposit/', views.YourView.as_view(), name='deposit'),
]