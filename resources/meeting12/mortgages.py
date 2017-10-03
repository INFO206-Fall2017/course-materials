#!/usr/bin/env python3

"""
Program for building and plotting mortgages

Adapted from Guttag (2013). "Introducing to Computation and Programming Using Python"
"""

def calcPayment(loan, r, m):
	"""Returns the monthly payment for a mortgage of size
	loan at a monthly rate of r for m months.
	Assumes that loan and r are floats, m is an int."""
	return loan*(r*(1+r)**m)/((1+r)**m - 1)

class Mortgage(object):
	"""Abstract class for building different kinds of mortgages"""
	def __init__(self, loan, annualRate, months):
		"""Create a new mortgage"""
		self.loan = loan				# Loan value
		self.rate = annualRate / 12.0 	# Monthly rate
		self.months = months 			# Duration of loan in months
		self.paid = [0.0] 				# Start with none of the loan paid.
		self.owed = [loan]	# Initial loan amount owed.
		self.payment = calcPayment(self.loan, self.rate, self.months)
		self.legend = None 				# Destription of the loan

	def makePayment(self):
		"""Make a loan payment."""
		self.paid.append(self.payment)
		reduction = self.payment - self.owed[-1] * self.rate
		self.owed.append(self.owed[-1] - reduction)

	def getTotalPaid(self):
		"""Return the total amount paid to date"""
		return sum(self.paid)

	def __repr__(self):
		return self.legend


class Fixed(Mortgage):
	"""Fixed rate mortgate class"""
	def __init__(self, loan, r, months):
		Mortgage.__init__(self, loan, r, months)
		self.legend = 'Fixed rate, ' + str(r * 100) + '%'

class FixedWithPts(Mortgage):
	"""Fixed rate mortgage with discount points"""
	def __init__(self, loan, r, months, pts):
		Mortgage.__init__(self, loan, r, months)
		self.pts = pts
		self.paid = [loan * (pts / 100.0)]
		self.legend = 'Fixed rate, ' + str(r * 100) + '%, with ' + str(pts) + ' discount points'

class TwoRate(Mortgage):
	"""Class for dual-rate mortgage - teaser rate plus second/next rate."""
	def __init__(self, loan, r, months, teaserRate, teaserMonths):
		Mortgage.__init__(self, loan, teaserRate, months)
		self.teaserMonths = teaserMonths
		self.teaserRate = teaserRate
		self.nextRate = r / 12.0
		self.legend = 'Dual-rate ' + str(teaserRate * 100) + '% for ' + str(self.teaserMonths) + ' months, then ' + str(r * 100) + '%'

	def makePayment(self):
		"""Make a loan payment."""
		if len(self.paid) == self.teaserMonths + 1:
			self.rate = self.nextRate
			self.payment = calcPayment(self.owed[-1], self.rate, self.months - self.teaserMonths)
		Mortgage.makePayment(self)

def compareMortgages(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
	totMonths = years * 12
	fixed1 = Fixed(amt, fixedRate, totMonths)
	fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
	twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
	morts = [fixed1, fixed2, twoRate]

	for m in range(totMonths):
		for mort in morts:
			mort.makePayment()

	for m in morts:
		print('-------')
		print(m)
		print('--> Total payments = ${0:12,.2f}'.format(m.getTotalPaid()))
		print('-------')

		
if __name__ == '__main__':

	compareMortgages(amt = 200000, years = 30, fixedRate = 0.02, pts = 3.25, ptsRate = 0.01, varRate1 = 0.015, varRate2 = 0.05, varMonths = 48)