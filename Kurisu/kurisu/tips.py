from .search import *

k_ru = [[], []]
k_eng = [[], []]
k = [[], []]
tips = [[], []]
kirill = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def unif(s):
	return s.replace('.', '').replace(' ', '').replace('-', '').lower()

def init():
	with open('tips0.txt', 'r', encoding='utf-8') as f:
		tmp = [row.strip() for row in f]
		for i in range(len(tmp)//3):
			k_ru[0].append(unif(tmp[i*3]))
			k[0].append(tmp[i*3])
			k_eng[0].append(unif(tmp[i*3+1]))
			tips[0].append(tmp[i*3+2].replace('[linebreak]', '\n'))

	with open('tips.txt', 'r', encoding='utf-8') as f:
		tmp = [row.strip() for row in f]
		for i in range(len(tmp)//3):
			k_ru[1].append(unif(tmp[i*3]))
			k[1].append(tmp[i*3])
			k_eng[1].append(unif(tmp[i*3+1]))
			tips[1].append(tmp[i*3+2].replace('[linebreak]', '\n'))

def get_tip(index, sg=1):
	return tips[sg][index].split('|')

def search(tip, sg=1):
	tip = unif(tip)
	rus = len([x for x in kirill if x in tip]) > 0 and True or False
	
	s = rus and k_ru[sg] or k_eng[sg]

	exact = 0
	perc = 0
	try:
		i = s.index(tip)
		tip = tips[sg][i].split('|')
		exact = 1
		perc = 100
		dist = 0
	except:
		test = ['', 99999]
		for t in s:
			tmp = distance_3(t, tip)[0]
			if tmp < test[1]:
				test = [t, tmp]
		
		perc = (1 - float(test[1]) / float(len(test[0]))) * 100
		i = s.index(test[0])
		dist = test[1]
		tip = tips[sg][i].split('|')\

	if len(tip[1]) > 1000:
		tip[1] = tip[1][:900] + "... [не влезло :c]"

	return (
		(exact, perc, dist),
		k[sg][i],
		tip
	)
