import pytest
from requests_api import create_product, get_products_by_sellerId

# Проверка работы ручки получения всех объявлений по идентификатору продавца: получены все параметры объявления
def test_get_products_by_sellerId_check_params():
    sellerID = 314009
    name = "test7"
    price = 150
    contacts = 102
    likes = 37
    viewCount = 100

    response = create_product(sellerID, name, price, contacts, likes, viewCount)

    # Проверка статус-кода
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    # Получение всех объявлений по идентификатору продавца 823054
    response_all = get_products_by_sellerId(314009)

    # Проверка статус-кода
    assert response_all.status_code == 200, f"Expected status code 200, but got {response_all.status_code}"

    # Проверка того, что в полученном ответе содержатся все параметры объявления
    fields = set(response_all.json()[-1].keys())
    assert ("createdAt" in fields) and ("id" in fields) and ("name" in fields) and ("price" in fields) and ("sellerId" in fields) and ("statistics" in fields), f"Response doesn't contain all fields"
    stats = set(response_all.json()[-1]["statistics"].keys())
    assert ("contacts" in stats) and ("likes" in stats) and ("viewCount" in stats), f"Response doesn't contain all fields"


# Запуск теста
if __name__ == "__main__":
    pytest.main()