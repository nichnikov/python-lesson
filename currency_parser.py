# https://smart-lab.ru/blog/894489.php

import time
import requests
from bs4 import BeautifulSoup
import smtplib
import matplotlib.pyplot as plt

# Добавляем информацию о валютах и пороговых значениях
currencies = {'USD': {'threshold': 1.0, 'rate': 0}, 
              'EUR': {'threshold': 1.0, 'rate': 0},
              'GBP': {'threshold': 1.0, 'rate': 0}}

# Функция отправки уведомлений через Telegram Bot API
"""
def send_notification(currency, rate):
    token = 'your_token'
    chat_id = 'your_chat_id'
    message = f'{currency} rate is {rate}'
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'
    requests.get(url)
"""
# Функция создания графиков
def create_graph(currency, rates):
    plt.plot(rates)
    plt.ylabel(f'{currency} rate')
    plt.show()

while True:
    # Парсим данные с сайта Центробанка
    url = 'https://www.cbr.ru/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.contents)
    
    # Получаем информацию о каждой валюте и ее курсе
    for currency, data in currencies.items():
        currency_rate = soup.find('div', {'class': f'currency_base{currency.lower()}'})
        rate = float(currency_rate.find('div', {'class': 'currency__rate__value'}).text.replace(',', '.'))
        
        # Если курс изменился больше, чем пороговое значение, отправляем уведомление
        """
        if abs(rate - data['rate']) > data['threshold']:
            send_notification(currency, rate)"""
            
        # Обновляем информацию о курсе валюты
        data['rate'] = rate
        
        # Добавляем курсы в список для создания графиков
        data.setdefault('rates_history', []).append(rate)
        
        # Создаем график, если есть достаточно данных
        if len(data['rates_history']) >= 10:
            create_graph(currency, data['rates_history'])
            
    # Ждем 1 минуту, чтобы не перегружать сервер Центробанка
    time.sleep(60)