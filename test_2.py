import requests
import pytest
from requests_api import create_product_without_stats, get_product

# Тест для проверки создания объявления без статистики
def test_create_product_without_stats():
    sellerID = 680342
    name = "test_test"
    price = 100

    response = create_product_without_stats(sellerID, name, price)

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
    assert response_json["price"] == price, f"Expected price '{price}', but got '{response_json['price']}'"
    assert response_json["statistics"]["contacts"] == 0, f"Expected contacts '{0}', but got '{response_json['statistics']['contacts']}'"
    assert response_json["statistics"]["likes"] == 0, f"Expected likes '{0}', but got '{response_json['statistics']['likes']}'"
    assert response_json["statistics"]["viewCount"] == 0, f"Expected viewCount '{0}', but got '{response_json['statistics']['viewCount']}'"

# Запуск теста
if __name__ == "__main__":
    pytest.main()