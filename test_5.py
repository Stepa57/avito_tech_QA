import pytest
from requests_api import create_product, get_products_by_sellerId, get_product

# Тест для проверки работы ручки получения всех объявлений по идентификатору продавца
def test_get_products_by_sellerId():

    # Получение всех объявлений по идентификатору продавца 823054
    response_all = get_products_by_sellerId(823054)

    # Проверка статус-кода
    assert response_all.status_code == 200, f"Expected status code 200, but got {response_all.status_code}"

    # Запишем, сколько изначально объявлений существовало с этим sellerId
    response_all_json = response_all.json()
    before_add = len(response_all_json)

    # Создание первого объявления
    sellerID = 823054
    name = "test5_1"
    price = 1224
    contacts = 552
    likes = 7
    viewCount = 650

    response1 = create_product(sellerID, name, price, contacts, likes, viewCount)

    # Создание второго объявления
    sellerID = 823054 
    name = "test5_2" 
    price = 442
    contacts = 646
    likes = 675
    viewCount = 230

    response2 = create_product(sellerID, name, price, contacts, likes, viewCount)

    # Создание третьего объявления
    sellerID = 823054
    name = "test5_3"
    price = 334
    contacts = 22
    likes = 27
    viewCount = 60

    response3 = create_product(sellerID, name, price, contacts, likes, viewCount)

    # Проверка статус-кодов
    assert response1.status_code == 200, f"Expected status code 200, but got {response1.status_code}"
    assert response2.status_code == 200, f"Expected status code 200, but got {response2.status_code}"
    assert response3.status_code == 200, f"Expected status code 200, but got {response3.status_code}"

    # Получение всех объявлений по идентификатору продавца 823054
    response_all = get_products_by_sellerId(823054)

    # Проверка статус-кода
    assert response_all.status_code == 200, f"Expected status code 200, but got {response_all.status_code}"

    # Проверка того, что получено на 3 объявления больше
    response_all_json = response_all.json()
    assert len(response_all_json)-before_add == 3, f"Expected value = 3, but got {len(response_all_json)-before_add}"

# Запуск теста
if __name__ == "__main__":
    pytest.main()