"""
Name    : Take Home Test
Author  : Valentin Depoisier
Date    : 01/25/2018

Brief   : Some Unit tests for TakeHomeTest.py 
"""
import unittest
import math
from math import *


#Imports ----------------------------------------------------------------------
from TakeHomeTest import IntercomCustomerInvitation


#Class Definition -------------------------------------------------------------
class IntercomCustomerInvitation_Test(unittest.TestCase):

	def test_greatCircleDistanceFormula(self):
		it = IntercomCustomerInvitation()
		a_lat = radians(53.339428)
		a_lon = radians(-6.257664)
		b_lat = radians(53.2451022)
		b_lon = radians(-6.238335)
		d = it.greatCircleDistanceFormula(a_lat,a_lon,b_lat,b_lon)
		self.assertTrue(d<100)

	def test_parseJsonFile(self):
		it = IntercomCustomerInvitation()
		Customers = it.parseJsonFile('gistfile1.txt')
		self.assertTrue(len(Customers) > 0)

	def test_keepCustomersWhithinRange(self):
		it = IntercomCustomerInvitation()
		invitedCustomers = []
		Customers = it.parseJsonFile('gistfile1.txt')

		invitedCustomers = it.keepCustomersWhithinRange(Customers, 100)

		for customer in invitedCustomers:
			curr_lat = radians(float(customer['latitude']))
			curr_lon = radians(float(customer['longitude']))
			distance = it.greatCircleDistanceFormula(radians(53.339428), radians(-6.257664), curr_lat, curr_lon)
			self.assertTrue(distance < 100)
#------------------------------------------------------------------------------

#=================================== MAIN =====================================
if __name__ == '__main__':
	unittest.main()
#==============================================================================