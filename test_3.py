import requests
import pytest
from requests_api import create_product, get_product

# Тест для проверки создания объявлений с параметрами, тип данных которых не будет соответствовать ожидаемым
def test_create_product_bad_params():
    # Создание первого объявления
    sellerID = "680342"
    name = "test3"
    price = 100
    contacts = 12
    likes = 3
    viewCount = 10

    response1 = create_product(sellerID, name, price, contacts, likes, viewCount)

    # Создание второго объявления
    sellerID = True

    response2 = create_product(sellerID, name, price, contacts, likes, viewCount)

    # Создание третьего объявления
    sellerID = 680342
    price = "test3"

    response3 = create_product(sellerID, name, price, contacts, likes, viewCount)

    # Создание четвертого объявления
    price = 100
    contacts = "12"

    response4 = create_product(sellerID, name, price, contacts, likes, viewCount)

    # Создание пятого объявления
    contacts = 12
    likes = "3"

    response5 = create_product(sellerID, name, price, contacts, likes, viewCount)

    # Создание шестого объявления
    likes = 3
    viewCount = "10"

    response6 = create_product(sellerID, name, price, contacts, likes, viewCount)


    # Проверка статус-кодов
    assert response1.status_code == 400, f"Expected status code 400, but got {response1.status_code}"
    assert response2.status_code == 400, f"Expected status code 400, but got {response1.status_code}"
    assert response3.status_code == 400, f"Expected status code 400, but got {response1.status_code}"
    assert response4.status_code == 400, f"Expected status code 400, but got {response1.status_code}"
    assert response5.status_code == 400, f"Expected status code 400, but got {response1.status_code}"
    assert response6.status_code == 400, f"Expected status code 400, but got {response1.status_code}"
    

# Запуск теста
if __name__ == "__main__":
    pytest.main()