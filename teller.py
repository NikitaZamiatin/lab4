def convert(n):
    if n < 10:
        return ones[n] + ' '
    elif n < 20:
        return teens[n - 10] + ' '
    elif n < 100:
        if n % 10 == 0:
            return tens[n // 10] + ' '
        else:
            return tens[n // 10] + ' '  + convert(n % 10)
    elif n < 1000:
        if n % 100 == 0:
            return hundreds[n // 100] + ' '
        else:
            return hundreds[n // 100] + ' ' + convert(n % 100)
    else:
        m = n % 1000
        n //= 1000
            
        if n % 10 == 1 and n % 100 != 11:
            return convert(n) + thousands[1] + ' ' + convert(m)
        elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            return convert(n) + thousands[2] + ' ' + convert(m)
        else:
            return convert(n) + thousands[3] + ' ' + convert(m)

summ = int(input('Введите сумму выдачи в банкомате от 1 до 100 000: '))

ones = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
teens = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
tens = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
thousands = ['', 'тысяча', 'тысячи', 'тысяч']

summ_str = convert(summ)

if summ % 10 == 1 and summ % 100 != 11:
        summ_str += "рубль"
elif 2 <= summ % 10 <= 4 and (summ % 100 < 10 or summ % 100 >= 20):
        summ_str += "рубля"
else:
        summ_str += "рублей"

print(summ_str)