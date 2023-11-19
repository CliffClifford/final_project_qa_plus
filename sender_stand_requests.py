import requests
import configuration
import data

# Создание нового заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                               json=data.order_body)

#Сохранение номера заказа
def get_track():
    order_track = post_new_order().json()["track"]
    return order_track

#Получение заказа по его номеру
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + f"?t={track}")
