dna = 'ATGATTTTTCCATCTTTAAGTGCGATACTGTTTTGT'
dna_bases = ['A', 'C', 'G', 'T']
rna_bases = ['A', 'C', 'G', 'U']
basecomplement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}

def is_dna(dna):
	output = True
	for i in dna:
		if i == 'A' or i == 'T' or i == "G" or i == 'C':
			output = True
		else:
			output = False
			break
    
	return output


def is_rna(rna):
	output = True
	for i in rna:
		if i == 'A' or i == 'U' or i == "G" or i == 'C':
			output = True
		else:
			output = False
			break
	print rna
	return output

def transcribe(dna):
	output = ''
	for i in dna:
		if i == 'A' or i == "G" or i == 'C':
			output += i
		elif i == 'T':
			output += 'U'
		else:
			break
    
	return output

def reverse(dna):
	output = ''
	for i in dna:
		if i == 'A' or i == "G" or i == 'C' or i == 'T':
			output = i + output
    
	return output

def complement(dna):
	output = ''
	for i in dna:
		output += basecomplement[i]
	return output

def is_complement(strand1, strand2):
	output = True
	testStrand = complement(strand1)
	if strand2 == testStrand:
		output = True
	else:
		output = False
	return output

def reversecomplement(dna):
	flip = reverse(dna)
	return complement(flip)

def gc_content(dna):
	counter = 0
	for i in dna:
		if i == 'C' or i == 'G':
			counter += 1
	output = counter/float(len(dna))
	return output

def get_codons(dna):
	output = []
	if len(dna)%3 != 0:
		print "Error: the string is not a multiple of 3"
	else:
		for i in range(len(dna)/3):
			output.append(dna[(3*i):3*(i+1)])
	return output
