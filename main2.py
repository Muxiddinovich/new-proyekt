from main1 import Company
from main2 import Product
from main3 import Basket

if __name__ == "__main__":
    # Kompaniyalarni yaratamiz
    apple = Company("Apple", 1976)
    samsung = Company("Samsung", 1938)

    iphone = Product("iPhone 13", 2, 12000000, apple)
    galaxy = Product("Samsung Galaxy S21", 1, 8000000, samsung)
    basket = Basket()