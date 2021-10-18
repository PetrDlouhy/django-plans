from django.conf import settings
from django.urls import path, re_path

from plans.views import CreateOrderView, OrderListView, InvoiceDetailView, AccountActivationView, \
    OrderPaymentReturnView, CurrentPlanView, UpgradePlanView, OrderView, BillingInfoRedirectView, \
    BillingInfoCreateView, BillingInfoUpdateView, BillingInfoDeleteView, CreateOrderPlanChangeView, ChangePlanView, \
    PricingView, FakePaymentsView, billing_info_create_or_update

urlpatterns = [
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('account/', CurrentPlanView.as_view(), name='current_plan'),
    path('account/activation/', AccountActivationView.as_view(), name='account_activation'),
    path('upgrade/', UpgradePlanView.as_view(), name='upgrade_plan'),
    re_path(r'^order/extend/new/(?P<pk>\d+)/$', CreateOrderView.as_view(), name='create_order_plan'),
    re_path(r'^order/upgrade/new/(?P<pk>\d+)/$', CreateOrderPlanChangeView.as_view(), name='create_order_plan_change'),
    re_path(r'^change/(?P<pk>\d+)/$', ChangePlanView.as_view(), name='change_plan'),
    path('order/', OrderListView.as_view(), name='order_list'),
    re_path(r'^order/(?P<pk>\d+)/$', OrderView.as_view(), name='order'),
    re_path(r'^order/(?P<pk>\d+)/payment/success/$', OrderPaymentReturnView.as_view(status='success'),
            name='order_payment_success'),
    re_path(r'^order/(?P<pk>\d+)/payment/failure/$', OrderPaymentReturnView.as_view(status='failure'),
            name='order_payment_failure'),
    path('billing/', BillingInfoRedirectView.as_view(), name='billing_info'),
    path('billing/create/', BillingInfoCreateView.as_view(), name='billing_info_create'),
    path('billing/update/', BillingInfoUpdateView.as_view(), name='billing_info_update'),
    path('billing/create_or_update/', billing_info_create_or_update, name='billing_info_create_or_update'),
    path('billing/delete/', BillingInfoDeleteView.as_view(), name='billing_info_delete'),
    re_path(r'^invoice/(?P<pk>\d+)/preview/html/$', InvoiceDetailView.as_view(), name='invoice_preview_html'),
]

if getattr(settings, 'DEBUG', False):
    urlpatterns += [
        re_path(r'^fakepayments/(?P<pk>\d+)/$', FakePaymentsView.as_view(), name='fake_payments'),
    ]
