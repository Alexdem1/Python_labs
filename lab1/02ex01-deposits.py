#!/usr/bin/env python3

"""Calculate deposit percent yield based on time period.

Imagine your friend wants to put money on a deposit.
He has got many offers from different banks:
- First bank declares +A% each day;
- Second bank promises +B% each month;
- Third bank offers +C% by the end of the year;
- The 4th bank promotes +D% in a 10-year term;
- ... and so on ...

Your friend gets a terrible headache calculating all this stuff,
and asks you to help checking everything. You quickly realize
it is a common task and having a simple script is a great idea.

Let's implement this.

A simplified task:
Given the SUM amount of money, and PERCENT yield promised in a
FIXED_PERIOD of time, calculate the TOTAL equivalent of money
in a SET_PERIOD of time.

Math formula:
p = PERCENT / 100
TOTAL = SUM * ((1 + p) ** (SET_PERIOD / FIXED_PERIOD))
"""


# TODO: add lines to calculate yields for some common periods
#       of time (e.g. 1 month, 1 year, 5 years, 10 years)
# TODO: change the script to output the 1-year percent yield
#       as well
# TODO: (extra) Output only percents if the initial SUM is
#       not known at the moment the script is run

import time 

USAGE = """USAGE: {script} initial_sum percent fixed_period set_period

\tCalculate deposit yield. See script source for more details.
"""
USAGE = USAGE.strip()


def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    per = percent / 100
    growth = (1 + per) ** (set_period / fixed_period)
    return initial_sum * growth
   
def main(args):
            
    def basic (args):
        print("-------Selected basic mode-------\n")
        initial_sum, percent, fixed_period, set_period = map(float, args)
        res = deposit(initial_sum, percent, fixed_period, set_period)
        print(res)

        print("1 Year:")
        res = deposit(initial_sum, percent, fixed_period, 365)
        print(res)

    def common_period (args):
        print("-------Selected common period mode-------\n")
        initial_sum, percent, fixed_period = map(float, args)

        print("1 Month:")
        res = deposit(initial_sum, percent, fixed_period, 31)
        print(res)

        print("1 Year:")
        res = deposit(initial_sum, percent, fixed_period, 365)
        print(res)

        print("5 Year:")
        res = deposit(initial_sum, percent, fixed_period, 1825)
        print(res)

        print("10 Year:")
        res = deposit(initial_sum, percent, fixed_period, 3650)
        print(res)

    def unknown_init_sum (args):
        print("-------Selected uknown initial sum mode-------\n")
        percent, fixed_period, set_period = map(float, args)
        res = deposit(-1, percent, fixed_period, set_period)
        print(res)  
    
    def error (args):
        exit(USAGE.format(script=args[0]))
    
    if len(args) == 4 + 1:
        basic(args)
    elif len(args) == 4 + 1 and args[4] == "-cnpd":
        # Common periods of time
        # USAGE: {script} initial_sum percent
        common_period (args)
    elif len(args) == 3 + 1:
        # unknown initial sum
        # USAGE: {script} percent fixed_period set_period
        unknown_init_sum (args)
    elif len(args) != 4 + 1:
        error(args)

    args = args[1:4]

    

if __name__ == '__main__':
    import sys

    
    main(sys.argv)
