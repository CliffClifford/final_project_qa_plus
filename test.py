import sender_stand_requests

#Проверка получения заказа по его номеру
def test_getting_order_by_track():
    order_track = str(sender_stand_requests.get_track())
    response = sender_stand_requests.get_order(order_track)
    assert response.status_code == 200
