catalog = [
    {'name': 'Смартфон', 'price': 45000, 'rating': 4.8},
    {'name': 'Чехол', 'price': 500, 'rating': 4.2},
    {'name': 'Беспроводные наушники', 'price': 7000, 'rating': 4.8},
    {'name': 'Зарядное устройство', 'price': 1200, 'rating': 4.5},
]

price_sorted = sorted(catalog, key=lambda item: item['price'], reverse=True)
print(price_sorted)

rating_sorted = sorted(price_sorted, key=lambda item: item['rating'], reverse=False)
print(rating_sorted)

print(rating_sorted)

