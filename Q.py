import random, time, sys
from colorama import init, Fore
from os import system

init(convert=True)

time_memo = 5 # memorization time
nmbw = 7 # number of words to memorize

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
while True:
	print('\n\n\n')
	slprint('\tTHE WORDS ARE: \n\n\n', .24)

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

	qnn = random.randint(0, (len(wordlst)-1))
	q = wordlst[qnn]

	slprint ("\n\n\tWHAT IS WORD ", .2)
	print(Fore.RED + "#" + str(qnn+1) + Fore.GREEN + '?')

	print ('\n\t>>> ', end='')
	a = input()


	if (str(a.upper() + '\n') == str(q.upper())):
		slprint('\n\tCORRECT!', .2)

	else:

		print(Fore.RED, end='')
		slprint('\n\tWRONG!', .2)
		print(Fore.GREEN, end='')
		slprint('\n\tTHE CORRECT ANSWER IS: ',.2 )
		print(Fore.BLUE + str(q), end='')


	print(Fore.GREEN)
	time.sleep(1.4)
	bura()







