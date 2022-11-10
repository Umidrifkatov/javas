from django.shortcuts import render
from .forms import OrderForm
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import telebot

bot = telebot.TeleBot(settings.TOKEN, threaded=False)






@csrf_exempt
def worker(request):
    if request.META['CONTENT_TYPE'] == 'application/json':
        json_data = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])
        return HttpResponse("")
    else:
        raise PermissionDenied


def send_welcome(a):
    bot.send_message(settings.GROUP_ID, a, parse_mode='HTML')



def mainview(request):
    if request.method == "POST":
        phone = request.POST['phone']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        a = f"""Новый запрос 

Имя <strong>{name}</strong>
Телефон <strong>{phone}</strong>
Почта <strong>{email}</strong>
Сообщение <strong>{message}</strong>"""
        send_welcome(a)
        return render(request, 'done.html')
    else:
        return render(request, 'index.html')






