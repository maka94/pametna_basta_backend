from django.urls import path
from apps.basta import views

urlpatterns = [
    path('history', views.IstorijaZalivanjaView.as_view()),
    path('trenutni_uslovi', views.TrenutniUsloviView.as_view()),
    path('read_data', views.UpisiPodatkeSaSenzoraView.as_view()),
    path('relay', views.RelayOnView.as_view())
]