import pytest
from requests_api import create_product, get_stats

# Тест для проверки работы ручки получения статистики по item id: в ответе содержится три поля: contacts, likes, viewCount.
def test_get_stats_check_params():
    sellerID = 314002
    name = "test6"
    price = 150
    contacts = 102
    likes = 37
    viewCount = 100

    response = create_product(sellerID, name, price, contacts, likes, viewCount)

    # Проверка статус-кода
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    # Получение статистики объявления по его идентификатору
    item_id = response.json()['status'].split()[-1]
    response = get_stats(item_id)

    # Проверка статус-кода
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    fields = set(response.json()[0].keys())
    # Проверка того, что в полученном отвте содержатся поля contacts, likes, viewCount
    assert ("contacts" in fields) and ("likes" in fields) and ("viewCount" in fields), f"Response doesn't contain all fields"


# Запуск теста
if __name__ == "__main__":
    pytest.main()