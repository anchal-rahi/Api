
from django.urls import path
from myapiis import views

urlpatterns = [
  path('fetchdata',views.fetchall),
  path("save", views.savedata),
  path("single/<int:id>", views.singledata)

]