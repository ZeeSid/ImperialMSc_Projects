#Object oriented programming exercises
#MSc Bioinformatics 2021/2022

#Exercise 1:


#Exercise 31:
#Modify the code to include the following functionality:
#Returns a fasta sequence with a specified ID. Returns the description lines of all the sequences as a list. Returns the IDs of all the sequences as a list. Returns the length of a sequence with a specified ID.
#To incorporate this functionality separate methods should be added to the FastaRecord class. Write a script that tests the modified class.


class FastaRecord(object):
    # Class representing a FASTA record

	def __init__(self, description_line):
		# Initialise an instance of the FastaRecord class
		self.sequence = description_line
		# Remove > and whitespace on ends
		self.description = description_line[1:]
		self.description = self.description.strip()
		self.seqid = (self.description.split())[0]
		self.seq_length = 0

	def add_sequence_line(self, sequence_line):
        
		# Add a sequence line to the FastaRecord instance.
		# This function can be called more than once.
        
		self.seq_length += len(sequence_line.strip())
		self.sequence += sequence_line

	def matchesID(self, searchid):
		# Return description line by ID
		if self.seqid == searchid:
			return True

	def getDescription(self):
		# Return description line
		return self.description 

	def getSeqLength(self):
		# Return seq_length
		return self.seq_length
    
	def __repr__(self):
		# Representation of the FastaRecord instance
		return self.sequence


class FastaParser(object):
   	# Class for parsing FASTA files
	def __init__(self, fpath):
	# Initialise an instance of the FastaParser
		self.fpath = fpath
		self.record_list = []

		fasta_record = None
		with open(self.fpath, 'r') as fh:
			for line in fh:
				if line.startswith('>'):
					if fasta_record:
						self.record_list.append(fasta_record)
					fasta_record = FastaRecord(line)
				else:
					fasta_record.add_sequence_line(line)
			self.record_list.append(fasta_record)

	
	def __repr__(self):
		seqs = ""
		for record in self.record_list:
			seqs += str(record) + "\n"
		return seqs

	def getRecords(self):
		return self.record_list

	def getRecordByID(self, seqid):
		for record in self.record_list:
			if record.matchesID(seqid):
				return record

	def getSeqLength(self, seqid):
		for record in self.record_list:
			if record.matchesID(seqid):
				return record.getSeqLength()

	def getIDs(self):
		ids = []
		for record in self.record_list:
			ids.append(record.seqid)
		return ids

	def getDescriptions(self):
		descriptions = []
		for record in self.record_list:
			descriptions.append(record.description)
		return descriptions


##########################################################################################################################

#Exercise 2:


#The classes so far are designed to handle multiple fasta sequences but sometimes a requirement is just to manipulate a single sequence. 
#Below is a simple class to store a nucleotide sequence, which can be modified to provide additional functionality. This class will just store the sequence itself and not the description line.

########################################################
#class DNA: 										   #
#    def __init__(self, s): 						   #
#        # Create DNA instance initialized to string s #
#        self.seq = s 								   #
########################################################


#Reverse the sequence. Complement the sequence. Reverse complement the sequence. Provide the %GC content of the sequence. 
#Provide a list of codons in the sequence. You could also additionally add a method to translate the sequence. You should have the code for this from a previous exercise.
#Write a script that tests the DNA class. You can use the sequence.fasta file available from the the exercise anwsers page to test the class. 
#You will need to extract just the sequence from this file and use that to create an object instance of the DNA class.



class DNA: 
 
	def __init__(self, s): 
		# Create DNA instance initialized to by the sequence s
		self.seq = s 
		self.comp = {'a':'t', 't':'a', 'g':'c', 'c':'g'}
	
	def reverse(self): 
        	# Return the reversed sequence
		self.revseq = self.seq[::-1]
		return self.revseq 

	def complement(self): 
		# Return the complementary sequence
		compseq = ""
		for nuc in self.seq:
			compseq += self.comp[nuc] 
		return compseq 
     
	def reversecomplement(self): 
		# Return the reverse complement of the sequence
		compseq = ""
		for nuc in self.seq:
			compseq += self.comp[nuc]
		return compseq[::-1] 
     
	def gc(self): 
		# Return the percentage of sequence composed of G and C
		# Note the limitation of these next two methods are that they are case sensitive
		# They need to be modified to work with a sequence in upper case
		gc = self.seq.count('g') + self.seq.count('c') 
		return gc * 100.0 / len(self.seq) 
 
	def codons(self): 
		# Return a list of codons for the sequence
		codons = []
		for count in range(0, len(self.seq), 3):  
			codons.append(self.seq[count:count+3])
		 
		return codons 

	# Return the printable representation of the object, the sequence
	def __repr__(self):
		return self.seq
  

