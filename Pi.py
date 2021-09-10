from Complex import Complex
import matplotlib.pyplot as pl

max_iter = 100000000

def calc_mand_esc(c):

	i = 0
	k = c
	while k.real ** 2 + k.imag ** 2 < 4 and i < max_iter:
		k = k.pow(Complex(2, 0)).add(c)
		i += 1

	return i

c1 = calc_mand_esc(Complex(-.75 , .1))
print("Done c1")

c2 = calc_mand_esc(Complex(-.75 , .01))
print("Done c2")

c3 = calc_mand_esc(Complex(-.75 , .001))
print("Done c3")

c4 = calc_mand_esc(Complex(-.75 , .0001))
print("Done c4")

c5 = calc_mand_esc(Complex(-.75 , .00001))
print("Done c5")

c6 = calc_mand_esc(Complex(-.75 , .000001))
print("Done c6")

#Each iteration takes exponentially longer, so I stopped at 6. Try out 7 if you dare
# c7 = calc_mand_esc(Complex(-.75 , .0000001))
# print("Done c7")


print(f"c1: {c1}\nc2: {c2}\nc3: {c3}\nc4: {c4}\nc5: {c5}\nc6: {c6}\n")