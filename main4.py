from main3 import Company, Product, Basket

menu=(
    "1.Add\n"
    "2.View\n"
    "3.Remove\n"
    "4.Total\n"
    "5.Exit\n"
)
basket=Basket()

while True:
    print(menu)
    choise=input(">>> ")
    if choise == "1":
        company=Company("Apple", 2025)
        name=input("name = ")
        price=int(input("price = "))
        amout=int(input("amout = "))
        product=Product(name, price, amout, company)
        basket.add_product(product)

    elif choise=="2":
        basket.view_products()
    elif choise=="3":
        product_name=input("O'chiriladigan name = ")
        basket.remove(product_name)

    elif choise == "4":
        print(basket.total())



    elif choise=="5":
        break


    