"""
Name    : Take Home Test
Author  : Valentin Depoisier
Date    : 01/25/2018

Brief   : Read the full list of customers from a file. Calculate the distance 
between the Dublin office and each customer with the great-circle distance
formula. Output the names and user ids of customers within 100km,
sorted by User ID (ascending).

Notes   : Here are the main reasons why I chose to code this exercise in Python.
First, because it is easy to scan a JSON-encoded file with it (just use the json
package which is available with most versions of python).
In addition, the math functions useful for calculating the formula of the 
Great-Circle distance are present and this makes the development much faster.
Finally, python is popular and its portability is very good, which makes it a
good candidate for this kind of small applications.

"""

#Imports ----------------------------------------------------------------------
import json
import math
from math import *

#Class Definition -------------------------------------------------------------
class IntercomCustomerInvitation():
    
    #Dublin office coordinates
    off_lat = radians(53.339428)
    off_lon = radians(-6.257664)

    def parseJsonFile(self, fileName):
        """
        This function opens and parses the file passed as parameter. 
        The contents of the file is returned in a dictionary.
        """
        Customers = []
        f=open(fileName)

        for line in f:
            Customers.append(json.loads(line))

        f.close()
        return Customers

    def greatCircleDistanceFormula(self, a_lat, a_lon, b_lat, b_lon):
        """
        This function calculates the distance between 2 points on earth
        using the formula of the Great Circle distance.
        """
        lonDiff = abs(a_lon - b_lon)
        dSig = acos(sin(a_lat)*sin(b_lat) + cos(a_lat)*cos(b_lat)*cos(lonDiff))
        d = 6371 * dSig         #6371 is the radius of Earth in km
        return d

    def keepCustomersWhithinRange(self, Customers, rge):
        """
        This function returns the customers within range around the office
        """
        invitedCustomers = []
        for customer in Customers:
            curr_lat = radians(float(customer['latitude']))
            curr_lon = radians(float(customer['longitude']))
            distance = self.greatCircleDistanceFormula(self.off_lat, self.off_lon, curr_lat, curr_lon)
            if distance <= rge:
                invitedCustomers.append(customer)
        
        return invitedCustomers

    def displayInvitedCustomersSorted(self, invitedCustomers):
        """
        This function display the customers sorted by their ID (ascending)
        """
        invitedCustomers_sorted = sorted(invitedCustomers, key=lambda x: x['user_id'])

        for customer in invitedCustomers_sorted:
            print ('ID :',customer['user_id'], ' \tName : ', customer['name'])

#------------------------------------------------------------------------------

#=================================== MAIN =====================================
if __name__ == '__main__': 

    intercom = IntercomCustomerInvitation()
    invitedCustomers = []
    
    Customers = intercom.parseJsonFile('gistfile1.txt')
    invitedCustomers = intercom.keepCustomersWhithinRange(Customers, 100)
    intercom.displayInvitedCustomersSorted(invitedCustomers)

#==============================================================================