words = 'LoveVladVova'    # Показать любовные ключевые слова
print("     ")
print("     ")
for item in words.split():
    item = item + ''  # Чтобы добиться эффекта распечатки пробелов между символами
    letterlist = []    # общий список всех печатных символов, который содержит подсписок y list_X
    for y in range(12, -12, -2):
        list_X = []    # список напечатанных символов на оси X, который содержит строку букв
        letters = ''    # строка в list_X, которая фактически является всеми символами, которые будут напечатаны в этой строке
        for x in range(-30, 30):    # * - умножение, ** - сила
            expression = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if expression <= 0:
                letters += item[(x-y) % len(item)]
            else:
                letters += ' '
        list_X.append(letters)
        letterlist += list_X
    print('\n'.join(letterlist))
