from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
	path('', views.IndexViews.as_view(), name='home'),
	path('contact/', views.ContactViews.as_view(), name='contact'),
	path('portfolio/', views.PortfolioViews.as_view(), name='portfolios'),
	path('portfolio/<slug:slug>', views.PortfolioDetailViews.as_view(), name='portfolio'),
	path('blog', views.BlogViews.as_view(), name='blogs'),
	path('blog/<slug:slug>', views.BlogDetailViews.as_view(), name='blog'),
]