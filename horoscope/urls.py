from django.urls import path, register_converter
from . import views, converters



register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [

    path("", views.index, name="horoscope-index"),


    path("type/", views.type_index),
    path("type/<str:type_name>/", views.type, name="type_name"),
    path("<yyyy:sign_zodiac>", views.get_yyyy_converters),
    path("<int:sign_zodiac>", views.get_info_sign_zodiac_by_number),
    path("<str:sign_zodiac>", views.get_info_sign_zodiac, name="horoscope-name"),



]
