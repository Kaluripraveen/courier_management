from myapp import views
from django.urls import path
from .views import RegisterView,LogoutView

urlpatterns = [
    path('', views.homePage,name='welcomePage'),
    path('register',RegisterView.as_view()),
    path('login/',views.login,name="login"),
    path('user',views.loginUser,name='user'),
    path('home/',views.homePage2,name='home'),
    path('logout/',LogoutView.as_view())
]
