from django.urls import path
from reports import views

urlpatterns = [
    path('', views.RatingFormView.as_view(), name='rate_form'),
    path('thanks', views.end_form, name='end_form'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('rate/detail/<int:pk>', views.DetailRatingView.as_view(), name='rate_detail'),
    path('rate/one', views.rate1_list, name="rate1_list"),
    path('rate/two', views.rate2_list, name="rate2_list"),
    path('rate/three', views.rate3_list, name="rate3_list"),
    path('rate/four', views.rate4_list, name="rate4_list"),
    path('rate/five', views.rate5_list, name="rate5_list"),
    path('dashboard', views.get_Details, name="dashboard"),
    path('search/', views.search, name='search'),

]
