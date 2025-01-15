from DNAToolkit import *
import random

rndDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(50)])

print(validateSeq(rndDNAStr))
