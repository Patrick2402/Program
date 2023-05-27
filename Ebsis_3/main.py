import argparse
from functions import one_sinus, second_stage, two_sinus

########################################################################
# Poniszy kod pozwala wywolac odpowiednie etapy zadania za pomoca flag #
########################################################################

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-onesin', '--one',  action="store_true",  help='One signal in part 1')
parser.add_argument('-sumsin', '--onetwo',  action="store_true",  help='Two signals in part 1')
parser.add_argument('-stagetwo', '--two',      action="store_true",  help='One signal in part 2')
args = parser.parse_args()

if args.one:
    one_sinus()
elif args.onetwo:
    two_sinus()
elif args.two:
    second_stage()

###############################################################################
# PRAWA AUTORSKIE: PATRYK ZAWIEJA 259428 - student politechniki wrocławskiej  #
###############################################################################