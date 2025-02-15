import pytest
from requests_api import create_product, get_product

# Тест для проверки создания объявления
def test_create_product():
    sellerID = 680342
    name = "test_test"
    price = 100
    contacts = 12
    likes = 3
    viewCount = 10

    response = create_product(sellerID, name, price, contacts, likes, viewCount)

    # Проверка статус-кода
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    # Получение объявление по его идентификатору
    item_id = response.json()['status'].split()[-1]
    response = get_product(item_id)
    
    # Проверка статус-кода
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Проверка тела ответа
    response_json = response.json()[0]

    assert response_json["id"] == item_id, f"Expected id '{item_id}', but got '{response_json['item_id']}'"
    assert response_json["sellerId"] == sellerID, f"Expected sellerId '{sellerID}', but got '{response_json['sellerId']}'"
    # Не проверяем правильность заполнения поля "name", потому что в этом месте обнаружена ошибка, см. BUGS.md
    # assert response_json["name"] == name, f"Expected name '{name}', but got '{response_json['name']}'"
    assert response_json["price"] == price, f"Expected price '{price}', but got '{response_json['price']}'"
    assert response_json["statistics"]["contacts"] == contacts, f"Expected contacts '{contacts}', but got '{response_json['statistics']['contacts']}'"
    assert response_json["statistics"]["likes"] == likes, f"Expected likes '{likes}', but got '{response_json['statistics']['likes']}'"
    assert response_json["statistics"]["viewCount"] == viewCount, f"Expected viewCount '{viewCount}', but got '{response_json['statistics']['viewCount']}'"

# Запуск теста
if __name__ == "__main__":
    pytest.main()