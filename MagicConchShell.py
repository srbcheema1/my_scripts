import random
import datetime

random.seed(datetime.datetime.now())
choice = random.choice([True,False])

print("\t-----------------\n\tMagic Conch Shell\n\t-----------------")

if choice == True :
	print("\n\tDo It!\n")
else:
	print("\n\tDon't do it!\n")



