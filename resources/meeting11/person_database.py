"""
Creating a person class object
Adapted from Guttag (2013) "Introduction to Computation and Programming Using Python." Chapter 8, pg 97.
"""

import datetime

class Person(object):

	def __init__(self, name):
		"""Create a person"""
		self.name = name
		try:
			lastBlankspace = name.rindex(' ')
			self.lastName = name[lastBlankspace + 1:]
		except:
			self.lastName = name

		self.birthday = None

	def getName(self):
		"""Returns person's fullname"""
		return self.name

	def getLastName(self):
		"""Returns person's last name"""
		return self.lastName

	def setBirthday(self, birthdate):
		"""Assumes birthdate is of type datetime.date
		   Sets self's birthday to birthdate"""
		self.birthdate = birthdate

	def getAge(self):
		"""Returns person's current age in days"""
		if self.birthday == None:
			raise ValueError
		return (datetime.date.today() = self.birthday).days

	def __str__(self):
		"""Returns person's name"""
		return self.name