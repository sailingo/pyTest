#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy

months  = float(input("please input your total person months:"))

junior_price = float(input("Please input your junior staff prices:"))
intermediate_price = float(input("please input intermediate staff pries:"))
senior_price = float(input("Please input the senior staff prices:"))

junior_staff = float(months * 0.3)
print("%10.2f" %(junior_staff))
total_junior_price = float(junior_staff * junior_price)

intermediate_staff = float(months * 0.5)
total_intermediate_price = float(intermediate_price * intermediate_staff)

senior_staff = float(months * 0.2)
total_senior_price = float(senior_price * senior_staff )

print("Total months is: %10.2f " %(months))
print("The junior taff number is: %3.2f ,and junior price is(Exclu): %10.2f "
      %(junior_staff , total_junior_price))

print("The intermediate staff number is: %3.2f ,and intermediate price is(Exclu): %10.2f "
      %(intermediate_staff , total_intermediate_price ))

print("The senior staff number is: %3.2f ,and senior price is(Exclu): %10.2f "
      %(senior_staff , total_senior_price))

total_price = total_junior_price + total_intermediate_price + total_senior_price

print("The total price excluded tax:%10.2f" %(total_price))
print("The total price included tax is:%10.2f " %(total_price * 1.06))
