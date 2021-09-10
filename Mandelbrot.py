from Complex import Complex
import matplotlib.pyplot as plt

# Print iterations progress
# source: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

width = 1920
height = 1080

realB = -2, 1
imagB = -1, 1

max_iter = 100
pr = 0

def calc_mand_esc(c):

	global pr

	if pr % 100 == 0: #There are an enormous number of iterations, so I don't want to call this TOO often
		printProgressBar(pr, width*height, prefix = 'Progress', decimals=2)

	i = 0
	pr += 1
	k = c
	while k.real ** 2 + k.imag ** 2 < 4 and i < max_iter:
		k = k.pow(Complex(2, 0)).add(c)
		i += 1

	return i

output = [[
	calc_mand_esc(
		Complex(
			(realB[0] + x * (realB[1] - realB[0]) / (width - 1)),
			(imagB[1] - y*(imagB[1]-imagB[0])/(height - 1))
		)
	)
	for x in range(width)] for y in range(height)]

printProgressBar(pr, width*height, prefix = 'Progress')

plt.imshow(output)
plt.show()