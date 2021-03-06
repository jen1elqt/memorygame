import random, time, sys
from colorama import init, Fore
from os import system

init(convert=True)

time_memo = 7 # memorization time
time_pass = 5 # time gap 
nmbw = 4 # number of words to memorize
nmbslv = 3 # number of items to solve correctly

# open file to list
with open('s.txt') as fd:
	ss = fd.readlines()

def bura():
	system('cls')

bura()

cols = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

def randc():
	fd = random.choice(cols)
	return fd


def slprint(w, t):
    for c in w:
        print(c, end='')
        sys.stdout.flush() # defeat buffering
        time.sleep(random.random() * float(t))


def solvm_add_sub(solveam): #additional difficulty
	f = 0
	slprint ('\n\nYOU NEED ', .2)
	print (Fore.RED + str(solveam) + Fore.GREEN, end='')
	slprint(' CORRECT ANSWERS TO CONTINUE.\n\n', .2)

	while f != solveam:
		sew = random.randint(0, 1)
		print('\n\n')
		if sew == 0:
			ad1 = random.randint(1, 100)
			ad2 = random.randint(1, 100)

			print('\t\t' + str(ad1) + ' + ' + str(ad2) + ' = ', end='') 
			ad3 = ad1 + ad2
			ssd = input(' ')
			if int(ssd) != ad3:
				print(Fore.RED + '\t\t\tWRONG!' + Fore.MAGENTA)
				slprint('\t\t\tCORRECT ANSWER IS: ' + str(ad3), .3)
				print(Fore.GREEN)
			else:
				print(Fore.BLUE + '\t\tCORRECT!' + Fore.GREEN)
				f = f + 1
		if sew == 1:
			asx = random.randint(1, 100)
			asy = random.randint(1, 100)
			if (asx < asy):
				asw2 = asx 
				asx = asy 
				asy = asw2
			ad33 = asx - asy
			print('\t\t' + str(asx) + ' - ' + str(asy) + ' = ', end='')
			ssdd = input(' ')
			if int(ssdd) != ad33:
				print(Fore.RED + '\t\t\tWRONG!' + Fore.MAGENTA)
				slprint('\t\t\tCORRECT ANSWER IS: ' + str(ad33), .3)
				print(Fore.GREEN)
			else:
				print(Fore.BLUE + '\t\tCORRECT!' + Fore.GREEN)
				f = f + 1


# clean the list, select only words greater than 4 characters
lis2 = []
for i in ss:
	if len(i) > 4:
		lis2.append(i)

# function to take random words
def taknmbw(sw):
	dssx = []
	for fucku in range(int(sw)):
		dssx.append(str(random.choice(lis2)))
	return dssx
'''
print('\n\n\n\t' + Fore.RED + str(nmbw) + Fore.GREEN, end='') 
slprint(' RANDOM WORDS SHALL BE PRINTED', .2)
slprint('\n\tYOU SHALL HAVE ', .2)
print(Fore.RED + str(time_memo) + Fore.GREEN, end='')
slprint(' SECONDS TO MEMORIZE THEM.', .23)
'''


score = 0
count = 0
while True:
	print(  Fore.MAGENTA)
	slprint('\n\n\t\t\t\tSCORE: ', .1)
	print(randc() + str(score) + randc() + ' / ' + randc() + str(count))
	print(Fore.GREEN, end='')
	slprint('\n\n\tTHE WORDS ARE: \n\n\n', .24)
	print(Fore.YELLOW)

	wordlst = taknmbw(nmbw)
	dcnt = 1

	for s in wordlst:
			slprint('[' + str(dcnt) + ']', .12)
			print(randc(), end='')
			slprint('\t\t' + str(s), .23)
			print(Fore.GREEN)
			dcnt += 1
	time.sleep(time_memo)

	bura()
	# activate for additional difficulty

	solvm_add_sub(nmbslv)
	# change range how many times to solve



	time.sleep(time_pass) # time gap
	bura()


	qnn = random.randint(0, (len(wordlst)-1))
	q = wordlst[qnn]
	print(randc(), end='')
	slprint ("\n\n\tWHAT IS WORD ", .2)
	print(Fore.RED + "#" + str(qnn+1) + Fore.GREEN + '?')

	print ('\n\t>>> ' + randc(), end='')
	a = input()


	if (str(a.upper() + '\n') == str(q.upper())):
		print(Fore.BLUE, end='')
		slprint('\n\tCORRECT!', .2)
		score = score + 1

	else:

		print(Fore.RED, end='')
		slprint('\n\tWRONG!', .2)
		print(Fore.GREEN, end='')
		slprint('\n\tTHE CORRECT ANSWER IS: ',.2 )
		print(Fore.BLUE + str(q), end='')


	print(Fore.GREEN)
	time.sleep(1.4)
	bura()
	count = count + 1








