# from main3 import Company, Product, Basket

# menu=(
#     "1.Add\n"
#     "2.View\n"
#     "3.Remove\n"
#     "4.Total\n"
#     "5.Exit\n"
# )
# basket=Basket()

# while True:
#     print(menu)
#     choise=input(">>> ")
#     if choise == "1":
#         company=Company("Apple", 2025)
#         name=input("name = ")
#         price=int(input("price = "))
#         amout=int(input("amout = "))
#         product=Product(name, price, amout, company)
#         basket.add_product(product)

#     elif choise=="2":
#         basket.view_products()
#     elif choise=="3":
#         product_name=input("O'chiriladigan name = ")
#         basket.remove(product_name)

#     elif choise == "4":
#         print(basket.total())



#     elif choise=="5":
#         break


    








from mainuy import Pupil, Student, PDPManager

menu=(
    "1. Talaba qo'shish\n"
    "2. O'quvchi qo'shish\n"
    "3. Talabalarni ko'rish\n"
    "4. O'quvchilarni ko'rish\n"
    "5. Talabani o'chirish\n"
    "6. O'quvchini o'chirish\n"
    "7. Chiqish\n"
)

manager=PDPManager()

while True:
    print("\n"+menu)
    tanlov=input("Tanlang >>> ")

    if tanlov=="1":
        name=input("Ismi: ")
        familiya=input("Familiyasi: ")
        yil=int(input("Tug'ilgan yili: "))
        kurs=int(input("Kursi: "))
        fakultet=input("Fakulteti: ")

        student=Student(name, familiya, yil, kurs, fakultet)
        print(manager.add_student(student))

    elif tanlov=="2":
        name=input("Ismi: ")
        familiya=input("Familiyasi: ")
        yil=int(input("Tug'ilgan yili: "))
        maktab=int(input("Maktab raqami: "))

        pupil=Pupil(name, familiya, yil, maktab)
        print(manager.add_pupil(pupil))

    elif tanlov=="3":
        print("\nBarcha talabalar:")
        for info in manager.get_all_students():
            print(info)

    elif tanlov=="4":
        print("\nBarcha o'quvchilar:")
        for info in manager.get_all_pupils():
            print(info)

    elif tanlov=="5":
        student_id=int(input("O'chiriladigan talaba ID si: "))
        print(manager.remove_student(student_id))

    elif tanlov=="6":
        pupil_id=int(input("O'chiriladigan o'quvchi ID si: "))
        print(manager.remove_pupil(pupil_id))

    elif tanlov=="7":
        print("Dastur tugatildi!")
        break

    else:
        print("Notog'ri tanlov. Qaytadan urinib ko'ring!")

        