from django.urls import path

from appRecomendacion.views import AuthLizy, RecomendationView

urlpatterns=[
    path('recomendator/',RecomendationView.as_view(),name='recomendation_list'),
    path('login/',AuthLizy.as_view(),name='login_token')
]