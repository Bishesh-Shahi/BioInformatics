# DNA Nucleodite files 

Nucleotides = ["A","U", "G", "U", "T"]

# Check the sequence to make sure it is in DNA String 
def validateSeq(dna_seq):
    tmpSeq = dna_seq.upper()
    for nuc in tmpSeq:
        if nuc not in Nucleotides:
            return False
        return tmpSeq
    
def countNucFrequency(seq):
    tmpFreqDict = {"A":0, "C":0, "G":0, "T":0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict