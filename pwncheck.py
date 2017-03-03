import pypwned
import json
import sys

# USAGE: $python3 pwncheck.py [email]

if len(sys.argv) > 1:
	emailtarget = sys.argv[1]
	pwn = pypwned.getAllBreachesForAccount(email=emailtarget)
	pwncount = len(pwn)

	if pwn == "404 - Not found - the account could not be found and has therefore not been pwned":
		print("\n\n" + '\033[91m' + "no results" + '\033[0m' + "\n\n")
	else:
		print("\n\nEmail: " + '\033[91m' + emailtarget + '\033[0m')
		for x in range(pwncount):
			print(pwn[x]['Name'])
		print("-----------")
		print("Leaks: " + str(pwncount))
		print("\n")

else:
	print("\n\nUsage: $ python3 pwncheck.py [email]\n\n")