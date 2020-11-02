fnum = int(input("Enter the first number: "))
nterms = int(input("Enter the number of terms: "))

for i in range(fnum, nterms + 1):
	if i > 1:
		for j in range(2, i):
			if (i%j)==0:
				break
		else:
			print(i)