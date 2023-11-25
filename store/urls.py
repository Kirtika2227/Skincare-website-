from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
    path('', views.main_page, name="main"),
	path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('login/', views.login_view, name='login'),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]

