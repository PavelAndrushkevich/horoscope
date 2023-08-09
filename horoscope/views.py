from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render
# Create your views here.
zodiac_dict = {

    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',

}
types_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f"вы передали число из четырех чисел - {sign_zodiac}")


def index(request):
    zodiacs = list(zodiac_dict)
    context = {
        'zodiacs': zodiacs
    }

        #li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"

    return render(request, 'horoscope/index.html', context=context)





def get_info_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    zodiacs = list(zodiac_dict)
    data = {
        "description_zodiac": description,
        "sign": sign_zodiac.title(),
        'zodiacs': zodiacs,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_sign_zodiac_by_number(ruquest, sign_zodiac: int):
    zadiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiac_dict):
        return HttpResponseNotFound(f"Неправильный порядковый номер {sign_zodiac}")
    name_zadiac = zadiacs[sign_zodiac - 1]
    redict_url = reverse("horoscope-name", args=[name_zadiac])
    return HttpResponseRedirect(redict_url)




def type_index(request):
    li_elements = ""
    for type in types_dict:
        li_elements += f"<li> <a href='{type}/'>{type.title()}</a></li>"
    return HttpResponse(f"<ol>{li_elements}</ol>")


def type(request, type_name: str):
    li_elements = ""
    for sign in types_dict[type_name]:
        redirect_path = reverse("horoscope-name", args=[sign])
        li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    return HttpResponse(f"<ol>{li_elements}</ol>")


def get_table(requst):
    return render(requst, 'horoscope/table.html')