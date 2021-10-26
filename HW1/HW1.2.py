# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч: мм:сс.
# Используйте форматирование строк.

num = int(input('Введите время в секундах :'))
minutes = int(num//60)
hours = int(minutes/60)
sec = int(num%60)
form = '{hours}:{minutes}:{sec}'
print(form.format(hours=hours, minutes=minutes, sec=sec))