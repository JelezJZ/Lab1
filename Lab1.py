
def task1():
	print("\nЗадание 1:")
	print("""Напишите скрипт, который преобразует введенное с клавиатуры
вещественное число в денежный формат. Например, число 12,5 должно
быть преобразовано к виду «12 руб. 50 коп.». В случае ввода
отрицательного числа выдайте сообщение «Некорректный формат!»
путем обработки исключения в коде.\n""")
	try:
		money = float(input("Введите вещественное число: "))
		assert money > 0 
		a,b = (int(x) for x in str(money).split(".",1))
		print(a, "руб.", b, "коп.", "\n")
	except assertionerror:
		print("Некорректный формат!")

def task2():
	print("\nЗадание 2:")
	print("""Написать скрипт, который выводит на экран «True», если элементы
программно задаваемого списка представляют собой возрастающую
последовательность, иначе – «False»\n""")
	def f(arr):
	    for i in range(len(arr) - 4):
	        el = arr[i:i + 4]
	        if el == list(range(min(el), max(el) + 1)):
	            return True, el[-1]
	    return False
	print(f([1, 2, 3, 4, 5]), "\n")

def task3():
	print("\nЗадание 3:")
	print("""Напишите скрипт, который позволяет ввести с клавиатуры номер
дебетовой карты (16 цифр) и выводит номер в скрытом виде: первые и
последние 4 цифры отображены нормально, а между ними – символы
«*» (например, 5123 **** **** 1212).\n""")
	arr = []
	m = 17
	for i in range(0, 4):
	    arr.append(input("Введите цифры: "))
	for i in range(4, 12):
	    arr.append(input("Введите цифры: ").replace('0', '*').replace('1', '*').replace('2', '*').replace('3', '*').replace('4', '*').replace('5', '*').replace('6', '*').replace('7', '*').replace('8', '*').replace('9', '*'))
	for i in range(12, 16):
	    arr.append(input("Введите цифры: "))
	print(arr, "\n")

def task4():
	print("\nЗадание 4:")
	print("""Напишите скрипт, который разделяет введенный с клавиатуры текст на
слова и выводит сначала те слова, длина которых превосходит 7
символов, затем слова размером от 4 до 7 символов, затем – все
остальные.\n""")
	text = input("Введите текст: ")
	words = text.split()
	words.sort(key=len, reverse=True)
	flag1, flag2 = 0, 0
	for word in words:
	    if flag1 == 0 and len(word)>7:
	        print('Больше 7: ', end='')
	        flag1 += 1
	    elif flag2 == 0 and 4<=len(word) <=7:
	        print('\nОт 4 до 7: ', end='')
	        flag2 += 1
	    elif (flag1 == 1 or flag2 == 1) and len(word) < 4:
	        print('\nВсе остальные: ', end='')
	        flag1 +=1
	        flag2 +=1
	    print(word, end=' ')
	print("\n")

def task5():
	print("\nЗадание 5:")
	print("""Напишите скрипт, который позволяет ввести с клавиатуры текст
предложения и сформировать новую строку на основе исходной, в
которой все слова, начинающиеся с большой буквы, приведены к
верхнему регистру. Слова могут разделяться запятыми или пробелами.
Например, если пользователь введет строку «город Донецк, река
Кальмиус», результирующая строка должна выглядеть так: «город
ДОНЕЦК, река КАЛЬМИУС».\n""")
	text = input("Введите предложения: ")
	words = text.split()
	text1 = []
	def is_upper(x):
	    for i in x:
	        if i.isupper():
	            text1.append(x.upper())
	        elif i.islower():
	            text1.append(x)
	        return
	for i in words:
	    is_upper(i)
	print(' '.join(text1), "\n")

def task6():
	print("\nЗадание 6:")
	print("""Напишите программу, позволяющую ввести с клавиатуры текст
предложения и вывести на консоль все символы, которые входят в этот
текст ровно по одному разу.\n""")
	text = str(input('Введите текст:\n')).lower()
	text1 = []
	for i in text:
	    if text.count(i) == 1:
	        text1.append(i)
	print(' '.join(text1), "\n")

def task7():
	print("\nЗадание 7:")
	print("""Напишите скрипт, который обрабатывает список строк-адресов
следующим образом: сначала определяет, начинается ли каждая строка
в списке с префикса «www». Если условие выполняется, то скрипт
должен вставить в начало этой строки префикс «http://», а затем
проверить, что строка заканчивается на «.com». Если у строки другое
окончание, то скрипт должен вставить в конец подстроку «.com». В
итоге скрипт должен вывести на консоль новый список с измененными
адресами. Используйте генераторы списков.\n""")
	list = ['github.com','www.google','www.youtube.com','gmail','metanit']
	print (list, '\n')
	for i in range(len(list)):
	    temp = list[i]
	    if temp[:4] != ('www.') and (temp[:8] != ('https://') or temp[:7] != ('http://')):
	        list[i] = 'www.' + list[i]
	    if temp[:8] != ('https://'):
	            list[i] = 'https://' + list[i]
	            if not list[i].endswith('.com'):
	                list[i] =list[i] + '.com'
	print(list, "\n")

def task8():
	print("\nЗадание 8:")
	print("""Напишите скрипт, генерирующий случайным образом число n в
диапазоне от 1 до 10000. Скрипт должен создать массив из n целых
чисел, также сгенерированных случайным образом, и дополнить
массив нулями до размера, равного ближайшей сверху степени двойки.
Например, если в массиве было n=100 элементов, то массив нужно
дополнить 28 нулями, чтобы в итоге был массив из 28=128 элементов
(ближайшая степень двойки к 100 – это число 128, к 35 – это 64 и т.д.).\n""")
	import random
	number = int(random.uniform(0, 10))
	print(number, " - Рандомное число")
	#Цикл заполняющий массив
	Array = [random.randrange(0, 100) for i in range(number)]
	print (Array)
	#Подсчет степени
	p = 2 
	i = 0
	while p**i <= number:
	    step = p**i
	    print('2^',i, '= ',step)
	    i = i + 1
	#Заполнение нулями массива
	zeros = step - number
	for i in range(zeros):
	    Array.append(0)
	print(Array, "\n")

def task9():
	print("\nЗадание 9:")
	print("""Напишите программу, имитирующую работу банкомата. Выберите
структуру данных для хранения купюр разного достоинства в заданном
количестве. При вводе пользователем запрашиваемой суммы денег,
скрипт должен вывести на консоль количество купюр подходящего
достоинства. Если имеющихся денег не хватает, то необходимо
напечатать сообщение «Операция не может быть выполнена!».
Например, при сумме 5370 рублей на консоль должно быть выведено
«5*1000 + 3*100 + 1*50 + 2*10».\n""")
	def cashInput():
	    print ('Сколько снять денег: ')
	    return int(input('Введите количество: '))
	bank = {1000:10, 100:100, 50:150, 10:500} #abstract money
	print ('Денег в банкомате:')
	print ('Купюры - \'1000\', количество -',bank[1000])
	print ('Купюры - \'100\', количество -',bank[100])
	print ('Купюры - \'50\', количество -',bank[50])
	print ('Купюры - \'10\', количество -',bank[10], "\n")
	normalBank = [10,100,150,500]
	out = False
	while out == False:
	    try:
	        cash = 0
	        cash = cashInput()
	        if cash % 10 != 0:
	            raise ValueError
	        else:
	            out = True
	    except ValueError:
	        cash = 0
	        print ('Операция не может быть выполнена!')
	listCash = list(str(cash))      
	#купюры номиналом 1000
	thousands = int(cash/1000)
	cashOut = 0
	i = 0
	while i<thousands:          
	    if normalBank[0] != 0:
	        cashOut = cashOut + 1000
	        normalBank[0] = normalBank[0]-1 
	    else:
	        print('Операция не может быть выполнена!')
	        input()
	        raise SystemExit
	    i = i + 1
	#купюры номиналом 100
	hundreds = int ((cash-cashOut)/100)
	i = 0
	while i<hundreds:
	    if normalBank[1] != 0:
	        cashOut = cashOut + 100
	        normalBank[1] = normalBank[1]-1
	    else:
	        print('Операция не может быть выполнена!')
	        input()
	        raise SystemExit
	    i = i + 1
	#купюры номиналом 50
	halfs = int((cash-cashOut)/50)
	i = 0
	while i<halfs:
	    if normalBank[2] != 0:
	        cashOut = cashOut + 50
	        normalBank[2] = normalBank[2]-1
	    else:
	        print('Операция не может быть выполнена!')
	        input()
	        raise SystemExit
	    i = i + 1
	#купюры номиналом 10
	tens = int((cash-cashOut)/10)
	i = 0
	while i<tens:
	    if normalBank[3] != 0:
	        cashOut = cashOut + 10
	        normalBank[3] = normalBank[3]-1
	    else:
	        print('Операция не может быть выполнена!')
	        input()
	    i = i + 1
	print('Выдано денег: ',cashOut, "\n")
	print ('Осталось денег в банкомате:')
	print ('Купюры - \'1000\', количество -',normalBank[0])
	print ('Купюры - \'100\', количество -',normalBank[1])
	print ('Купюры - \'50\', количество -',normalBank[2])
	print ('Купюры - \'10\', количество -',normalBank[3], "\n")
	print('«',thousands,'*1000 +',hundreds,'*100 +',halfs, '*50 +',tens,'*10', '»', "\n", sep='')

def task10():
	print("\nЗадание 10:")
	print("""Напишите скрипт, позволяющий определить надежность вводимого
пользователем пароля. Это задание является творческим: алгоритм
определения надежности разработайте самостоятельно.\n""")
	#Импортируем регулярные выражения
	import re
	pswrd = input('Введите пароль длиной минимум 6 символов: ') 
	while len(pswrd)<6:
	        print('Введите пароль заново:')
	        pswrd = input()
	#Проверка на символы
	i = -1
	#Счетчик
	if re.search(r'[A-Z]', pswrd):
	        i=i+1
	if re.search(r'[a-z]', pswrd):
	        i=i+1
	if re.search(r'[0-9]', pswrd):
	        i=i+1
	lvl = ['Новичок', 'Любитель', 'Тяжелый']
	print('Сложность вашего пароля:', lvl[i], "\n")


def task11():
	print("\nЗадание 11:")
	print("""Напишите генератор frange как аналог range() с дробным шагом.
Пример вызова:
	for x in frange(1, 5, 0.1):
	print(x)
	#выводит 1 1.1 1.2 1.3 1.4 … 4.9\n""")
	def frange(start, end, step):
	    st = start
	    start = float(start)
	    end = float(end)
	    step = float(step)
	    step = round(step, 2)
	    adD = []
	    adD.append(start)
	    end = int((end - start) / step)
	    for i in range(st, end):
	        adD.append(adD[i-1] + step)
	        round(adD[i-1], 2)
	    return adD
	for x in frange(1, 5, 0.1):
	    print(round(x, 2))
	print("\n")

def task12():
	print("\nЗадание 12:")
	print("""Напишите генератор get_frames(), который производит «оконную
декомпозицию» сигнала: на основе входного списка генерирует набор
списков – перекрывающихся отдельных фрагментов сигнала размера
size со степенью перекрытия overlap.
Пример вызова:
	for frame in get_frames(signal, size=1024, overlap=0.5):
	print(frame)\n""")
	def get_frames(signal, size, overlap):
	        print ('Step: ')
	        step = size * overlap
	        print(step)
	        i = 0
	        while i < len(signal):
	            print (signal[i:i+size])
	            i = i + int(step)
	size = 5
	signal = [i for i in range(0,1024)]
	overlap = 2.0
	get_frames(signal,size,overlap)
	print("\n")

def task13():
	print("\nЗадание 13:")
	print("""Напишите собственную версию генератора enumerate под названием
extra_enumerate. 
Пример вызова:
	for i, elem, cum, frac in extra_enumerate(x):
	print(elem, cum, frac)5
В переменной cum хранится накопленная сумма на момент текущей
итерации, в переменной frac – доля накопленной суммы от общей
суммы на момент текущей итерации. Например, для списка x=[1,3,4,2]
вывод будет таким:
(1, 1, 0.1) (3, 4, 0.4) (4, 8, 0.8) (2, 10, 1)\n""")
	def extra_enumerate(someArray, start):
	    n = start #номер
	    cum = 0 #хранится накопленная сумма на момент текущей итерации
	    for elem in someArray:   
	        yield n, elem
	        n += 1
	        cum = cum + elem
	        print(elem, ',', cum, ',', cum*0.1)
	x  = [1, 3, 4, 2] 
	for i in extra_enumerate(x, 0):
	    print()
	print("\n")

def task14():
	print("\nЗадание 14:")
	print("""Напишите декоратор non_empty, который дополнительно пров
списковый результат любой функции: если в нем содержатся пу
строки или значение None, то они удаляются.
Пример кода:
	@non_empty
	def get_pages():
	return ['chapter1', '', 'contents', '', 'line1']\n""")
	def non_empty(funcToDec):
	    def wrapper(): #Обертка
	        print ('Список с пустыми строками:')
	        print (funcToDec()) #Выводим не измененный список
	        temp = funcToDec()  #Переносим список в переменную
	        for index, data in enumerate(temp):  #Удаление пустых строк
	            if data == ' ' or data == '':
	                del temp[index]
	        print ('Список без пустых строк:') 
	        print (temp)
	    return wrapper()
	@non_empty 
	def get_pages():
	    return ['chapter1', ' ', 'contents', '', 'line1']
	print("\n")

def task15():
	print("\nЗадание 15:")
	print("""Напишите параметризированный декоратор pre_process, который
осуществляет предварительную обработку (цифровую фильтрацию)
списка по алгоритму: s[i] = s[i]–a∙s[i–1]. Параметр а можно задать в
коде (по умолчанию равен 0.97).
Пример кода:
	@pre_process(a=0.93)
	def plot_signal(s):
	for sample in s:
	print(sample)\n""")
	def pre_process(a):
	    def d_process(fn):
	        print ('Стартовый массив:')
	        print (s)
	        i = 0
	        for i in range(len(s)):
	            s[i] = s[i] - a*s[i-1] 
	        print ('Массив после предварительной обработки:')    
	        print (s)
	    return d_process
	s = [1.2, 3.0, 0.79] #Массив который задали
	@pre_process(a = 0.97)
	def plot_signal(s):
	    return 0
	print("\n")

def task16():
	print("\nЗадание 16:")
	print("""Напишите скрипт, который на основе списка из 16 названий
футбольных команд случайным образом формирует 4 группы по 4
команды, а также выводит на консоль календарь всех игр (игры
должны проходить по средам, раз в 2 недели, начиная с 14 сентября
текущего года). Даты игр необходимо выводить в формате «14/09/2016,
22:45». Используйте модули random и itertools.\n""")
	import random 
	import itertools 
	import time
	from datetime import datetime, timedelta
	
	#Список команд в файле
	f = open('text.txt', 'r')
	TeamList = [line.strip() for line in f]

	random.shuffle(TeamList) #Рандомная генерация списка
	TeamList = [TeamList[d:d+4] for d in range(0, len(TeamList), 4)] #Делим команды на 4 группы по 4 команды

	print ('\n----------------------Таблица групп:----------------------')
	print ('Группа A: ',TeamList[0])
	print ('Группа B: ',TeamList[1])
	print ('Группа C: ',TeamList[2])
	print ('Группа D: ',TeamList[3])
	print ('\n--------------------Рассписание матчей:-------------------')

	#Дата начала
	tempDate = "14.09.2022"
	#startDate = datetime.datetime.strptime(tempDate, "%d.%m.%Y")
	startTime = [14,9,2022]
	endTime = [14,4,2023]

	print ('Начало сезона', str(startTime[0])+'/'+str(startTime[1])+'/'+str(startTime[2])+' '+ str('22:45') )
	print ('Конец сезона', str(endTime[0])+'/'+str(endTime[1])+'/'+str(endTime[2])+' '+ str('22:45') )

	now_date = datetime.now()
	now_date = now_date.replace(2022,9,14)

	#Расписание
	t = open('text_rasp.txt', 'r+')
	a = datetime(2022, 9, 14) #Начало
	b = timedelta(days=7) #timedelta - разница между двумя моментами времени, с точностью до микросекунд(шаг)
	while a <= datetime(2023, 4, 14):
	    a = a + b
	    t.write('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45\n')

	f.close()
	t.close()
	print("\n")

while True:
	print("Задание 1 = 1\nЗадание 2 = 2\nЗадание 3 = 3\nЗадание 4 = 4\nЗадание 5 = 5\nЗадание 6 = 6\nЗадание 7 = 7\nЗадание 8 = 8\nЗадание 9 = 9\nЗадание 10 = 10\nЗадание 11 = 11\nЗадание 12 = 12\nЗадание 13 = 13\nЗадание 14 = 14\nЗадание 15 = 15\nЗадание 16 = 16\nВыход из приложения = 0")
	task = input("Введите номер задания: ")
	if task == "1":
		task1()
	elif task == "2":
		task2()
	elif task == "3":
		task3()
	elif task == "4":
		task4()
	elif task == "5":
		task5()
	elif task == "6":
		task6()
	elif task == "7":
		task7()
	elif task == "8":
		task8()
	elif task == "9":
		task9()
	elif task == "10":
		task10()
	elif task == "11":
		task11()
	elif task == "12":
		task12()
	elif task == "13":
		task13()
	elif task == "14":
		task14()
	elif task == "15":
		task15()
	elif task == "16":
		task16()
	elif task == "0":
		print("Пока!")
		break