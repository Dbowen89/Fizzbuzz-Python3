# -*- coding: utf-8 -*-
"""
Function for the common interview question 'Fizzbuzz'

The function takes the following arguments:
lower_range 
upper_range
fb_nums - list of factors to print fizz 




"""

def main(lower_range = 1, upper_range = 101, fb_nums = [3,5], fb_names = ['fizz', 'buzz']):

    for i in range(1, 101):
        mod0 = sum([i % num == 0 for num in fb_nums])
        if mod0 == 0:
            print(i)
        elif mod0 == 1:
            print('fizz')
        elif mod0 == len(fb_nums):
            print('fizzbuzz')
    
if __name__ == '__main__':
    main()    