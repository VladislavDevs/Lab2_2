shopsDictionary = {}
shopsList = input("Укажите список магазинов через запятую: ").split(",")
productsList = input("Укажите список товаров через запятую: ").split(",")
sumPricesDictionary = {}


for shop in shopsList:
    productsInShop = {}

    for item in productsList:
        price = input(f"Укажите цену {item} в магазине {shop}: ")
        productsInShop[item] = price

    shopsDictionary[shop] = productsInShop

purchasesList = input("Введите товары которые вы хотите купить через запятую: ").split(",")

for shop in shopsList:
    sumPrices = 0

    print(f"Магазин: {shop}")
    print("------------------------------------------")

    for purchase in purchasesList:
        price = shopsDictionary[shop][purchase]

        print(f"{purchase} : {price}")
        sumPrices += int(price)

    sumPricesDictionary[shop] = sumPrices

    print("------------------------------------------")
    print(f"Итого: {sumPrices}")
    print("------------------------------------------")

minPrice = min(sumPricesDictionary.values())
print(f"Вы сможете сэкономить больше всего денег в магазинах {[k for k, v in sumPricesDictionary.items() if v == minPrice]} : {minPrice} рублей")