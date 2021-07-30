#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy

months  = float(input("请输入总人月数:"))

junior_price = float(input("请输入初级人员的单价:"))
intermediate_price = float(input("请输入中级人员的单价:"))
senior_price = float(input("请输入高级人员的单价:"))
average_unit_cost = float(input("请输入我们的平均成本价格:"))

junior_staff = float(months * 0.3)
#print("%10.2f" %(junior_staff))
total_junior_price = float(junior_staff * junior_price)

intermediate_staff = float(months * 0.5)
total_intermediate_price = float(intermediate_price * intermediate_staff)

senior_staff = float(months * 0.2)
total_senior_price = float(senior_price * senior_staff )

total_average_cost_price = float(average_unit_cost * months)

print("总人月数: %3.2f " %(months))
print("初级人月数为: %3.2f 人月,不含税初级人员总价为: %10.2f "
      %(junior_staff , total_junior_price))

print("中级人月数为: %3.2f 人月,不含税中级人员总价为: %10.2f "
      %(intermediate_staff , total_intermediate_price ))

print("高级人月数为s: %3.2f 人月,不含税高级人员总价为: %10.2f "
      %(senior_staff , total_senior_price))

total_price = total_junior_price + total_intermediate_price + total_senior_price

print("不含税总价为:%10.2f" %(total_price))
print("含税总价为:%10.2f " %(total_price * 1.06))

print("按平均成本单价 %10.2f 计算，我们的不含税成本约为:%10.2f" %(average_unit_cost,
                                                                       total_average_cost_price ))



