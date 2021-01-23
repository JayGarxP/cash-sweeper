# Cash Sweeper given compound interest arguments will determine the breakpoints of interest when to sweep cash
#   to higher yield accounts
# total compound interest (I) formula
# I = (P * (1 + r/n)^(nt)) – P
# (P) Principal amount or start value
# (r) Rate of interest; like nominal APR
# (n) Compounding frequency
# (t) time units interest is applied over, must be same unit as r if APR use t * years
import argparse
from decimal import *

# create parser
parser = argparse.ArgumentParser(description='Print Interest Breakpoints',
                                 epilog='Dont forget about inflation!')

# Set parser arguments
parser.add_argument('principal', type=float)
parser.add_argument('interestRate', type=float)
parser.add_argument('compoundFrequency', type = float)
parser.add_argument('time', type=float)
# only show the minimum contribution to next whole cent interest
parser.add_argument('-n', '--next')

args = parser.parse_args()
print(args)
P = args.principal
r = args.interestRate / 100.0 #percent
n = args.compoundFrequency
t = args.time

Balance = P * pow(1 + r/n, n * t)

print("New Balance: $%.2f USD" % Balance)

Interest = Balance - P
print("Interest Generated: $%.2f USD" % Interest)
