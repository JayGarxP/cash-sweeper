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
parser.add_argument('-a', '--APR', default=0.49876, type=float)
# days away from next payment / reinvestment
parser.add_argument('--da', type=float)
# going to assume that previous days of compounding can be ignored
#      this will make the next breakpoint much more conservative
#      will eventually make form for multiple schedules of reinvestment within a compounding period

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

#17 days left till next pay
# 0.49876% APR
# $1071
# daily compound but only reinvested monthly on the 10th
# does not count certain holidays or weekends and seems to not count
# the business day of deposits
# daily interest accrued is 1cent???
# savingsAPR = 0.49876
# savingsDailyRate = (savingsAPR / 100.0) / 365.0
# acctBal = 1115.0 # + 44$ is next breakpoint on interest anything less would be a waste of money

savingsDailyRate = (args.APR / 100) / 365
nextBal = P + (P * savingsDailyRate * args.da)
print("Next monthly balance: $%.2f USD" % nextBal)
print("Actual monthly interest $%.2f USD" % (nextBal - P))

# next steps: ask user for next deposit/invest/payout day, count the days til then
# minus two with optional business days only mode
# calculate minimum interest breakpoint of cent, ten cent, dollar, ten dollar, hundred dollar
#

# effective annual interest rate
#EAR = (1 + i/n)^n -1
ear = pow(1 + args.APR / 365, 365) - 1
print ("Stated Annual Interest Rate Percent %.2f" % args.APR)
print("Effective Annual Interest Rate (Daily Compound) Percent %.2f" % ear)

# find Principal that returns a specific interest equation
# P = i/(((n + r)/n)^(n t) - 1) and ((n + r)/n)^(n t) !=1
i = Interest + 0.01
deltaP = (i / ( pow(((n+r)/n), n * t) - 1)) - P
print("Amount needed for next breakpoint: %.2f USD" % deltaP)

# approximation with EAR does not work so well...
#print( P +  P * ((ear / 100) / 365 * 17))

# approximation with APR works OK
rr = args.APR / 100 / 365
dailyInterestAccr = P * rr
print("Daily Interest Accrued: $%.2f" % dailyInterestAccr)

interestThisPeriod = dailyInterestAccr * args.da
print("Interest this period: $%.2f" % interestThisPeriod)

nextBP = ((interestThisPeriod + 0.01) / (args.da * rr)) - P
print("ACTUAL amount needed for next BP: %.2f USD" % nextBP)