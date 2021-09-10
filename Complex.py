from math import cos, sin, exp, log, atan2

class Complex:

	def __init__(self, real, imag):
		self.real = real
		self.imag = imag

	def mul(self, comp):
		n_real = self.real * comp.real - self.imag * comp.imag
		n_imag = self.real * comp.imag + self.imag * comp.real

		return Complex(n_real, n_imag)

	def add(self, comp):
		n_real = self.real + comp.real
		n_imag = self.imag + comp.imag

		return Complex(n_real, n_imag)

	def sub(self, comp):
		n_real = self.real - comp.real
		n_imag = self.imag - comp.imag

		return Complex(n_real, n_imag)

	def div(self, comp):
		if (comp.real ** 2 + comp.imag ** 2) != 0:
			n_real = (self.real * comp.real + self.imag * comp.imag) / (comp.real ** 2 + comp.imag ** 2)
			n_imag = (self.imag * comp.real - self.real * comp.imag) / (comp.real ** 2 + comp.imag ** 2)

			return Complex(n_real, n_imag)
		else:
			raise ZeroDivisionError("division by zero")


	def pow(self, comp):

		if self.real == 0 and self.imag == 0 and comp.real == 0 and comp.imag == 0:
			raise ArithmeticError("indefinite power")

		elif self.real == 0 and self.imag == 0:
			return Complex(0, 0)

		elif self.real == 1 and self.imag == 0:
			return Complex(1, 0)

		elif comp.real == 0 and comp.imag == 0:
			return Complex(1, 0)

		elif comp.real == 1 and comp.imag == 0:
			return Complex(self.real, self.imag)

		else:
			mult1 = (self.real ** 2 + self.imag ** 2) ** (comp.real / 2) * exp(-comp.imag * atan2(self.imag, self.real))
			real_mult = cos(comp.real * atan2(self.imag, self.real) + .5 * comp.imag * log(self.real**2 + self.imag**2))
			imag_mult = sin(comp.real * atan2(self.imag, self.real) + .5 * comp.imag * log(self.real**2 + self.imag**2))

			n_real = mult1 * real_mult
			n_imag = mult1 * imag_mult

			return Complex(n_real, n_imag)

	def __str__(self):

		msg = ""
		if self.real != 0:
			msg += f"{self.real} "

		if self.imag != 0:
			if self.imag > 0 and self.real != 0:
				msg += f"+ {self.imag}*i"
			elif self.imag < 0 and self.real != 0:
				msg += f"- {self.imag*-1}*i"
			elif self.imag > 0 and self.real == 0:
				msg += f"{self.imag}*i"
			elif self.imag < 0 and self.real == 0:
				msg += f"{self.imag}*i"

		elif msg == "":
				msg = "0"

		return msg