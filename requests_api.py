import requests

# Базовый URL API
BASE_URL = "https://qa-internship.avito.com"

# Функция для создания объявления
def create_product(sellerID, name, price, contacts, likes, viewCount):
    url = f"{BASE_URL}/api/1/item"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "sellerID": sellerID,
        "name": name,
        "price": price,
        "statistics": {
            "contacts": contacts,
            "likes": likes,
            "viewCount": viewCount
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    return response

# Функция для создания объявления без указания статистики
def create_product_without_stats(sellerID, name, price):
    url = f"{BASE_URL}/api/1/item"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "sellerID": sellerID,
        "name": name,
        "price": price
    }
    response = requests.post(url, json=payload, headers=headers)
    return response

# Функция для получения объявления по идентификатору
def get_product(itemID):
    url = f"{BASE_URL}/api/1/item/{itemID}"
    headers = {}
    response = requests.get(url, headers=headers)
    return response

# Функция для получения статистики объявления по идентификатору
def get_stats(itemID):
    url = f"{BASE_URL}/api/1/statistic/{itemID}"
    headers = {}
    response = requests.get(url, headers=headers)
    return response

# Функция для получения всех объявлений по идентификатору продавца
def get_products_by_sellerId(sellerID):
    url = f"{BASE_URL}/api/1/{sellerID}/item"
    headers = {}
    response = requests.get(url, headers=headers)
    return response
