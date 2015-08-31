# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 20:24:34 2015

@author: jp
"""

#Part 1
import csv

#Opening the chipotle.tsv file using a context manager and storing the data into a list
with open('chipotle.tsv', mode='rU') as f:
    file_nested_list = [row for row in csv.reader(f,delimiter='\t')]

#Part 2
#Storing the header info
header = file_nested_list[0]

#Storing the data (without the header)
data = file_nested_list[1:]

#Part 3
#Since item_price already adds up the quantity of the item, we do not
#have to multiple the quantity with the price.
#This avg calculation assumes the final line in the data is the last order.
#It also assumes each order increments by 1.
avg = round(sum([float(line[4][1:]) for line in data])/int(data[-1][0]),2)
print 'Average price of an order: $' + str(avg)

#Part 4
#Used if statement to check if the order item was a drink.
#Then converted the list of drinks into a set to remove duplicates from the list
unique_drinks_set = set([line[3] for line in data if 'Canned Soda' in line or 'Canned Soft Drink' in line])
    
#Part 5
#First grab list of burritos
burritos = [line for line in data if 'Burrito' in line[2]]

#Then convert the toppings into a list and add them up. Assumes the salsa is not a topping.
sum_total_toppings = sum([len(burrito[3].split('[')[-1][:-2].split(',')) for burrito in burritos])

#Calculate avg
avg_number_toppings = round(float(sum_total_toppings)/len(burritos),1)
print 'Average number of toppings per burrito: ' + str(avg_number_toppings)

#Part 6
#Import collections to use defaultdict
from collections import defaultdict
d = defaultdict(int)

#First grab list of chips orders
chips = [line for line in data if 'Chips' in line[2]]

#Use defaultdict to count occurrences of chips order type
for line in chips:
    d[line[2]] += int(line[1]) 

chips_dictionary = dict(d.items())
print chips_dictionary