from datetime import date

print("Программа позволяет узнать кол-во дней в люьом месяце любого года")
month = input("""Введите порядковый номер месяца.
'Обратите внимание, что по умолчанию установлен 2023й год.
Чтобы изменить год, введите: *' """)

scratchDate = [2023, month, 2]

if month == "*":
    user_year = int(input("Пожалуйста введите год: "))
    month = int(input("Введите месяц: "))
    scratchDate = [user_year, month, 2]
else:
    scratchDate = [2023, month, 2]


def dayCounter(a):
    a = [int(i) for i in a]
    var1 = date(a[0], a[1], a[2])
    monthCorrector = 1 if a[1] >= 12 else a[1] + 1
    yearCorrector = a[0] + 1 if a[1] == 12 else a[0]
    var2 = date(yearCorrector, monthCorrector, a[2])
    result = var2 - var1
    return(result)


print(dayCounter(scratchDate))

