"""
import re
par = open('JuanEnriquez_2016T-480p.txt').read()
q = re.split("[0-9]+:[0-9]+\n", par)
q.pop(0)
print q
"""


import re
import string
import hunspell


def para_to_cloud(paragraph):
	para = paragraph.translate(None, string.punctuation) # Cleans the paragraph of all punctuation
	para = para.split(' ') # Extracts all the words from the paragraph
	hobj = hunspell.HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')
	inception = para.pop(0)

	# Creates the very first stem set (including the original word)
	stem_cloud = set([inception]) | set(hobj.stem(inception)) 
	
	for word in para:
		#print word
		cloud = set(hobj.suggest(word))
		stem_cloud |= set([word]) | cloud   # Creates a union of the new set and inception cloud

	return list(stem_cloud)  


def file_to_transcript(filename):
	with open(filename) as f:
	    content = f.readlines()

	# Gets all the lines from the txt file and stores them in the list
	content = [x.strip() for x in content] 

	timestamps = []
	paragraphs = []

	for line in content:
		if re.search('[0-9]+:[0-9]+', line): 
			timestamps.append(line)
		else:
			line = line.translate(None, string.punctuation)
			line = line.lower()
			paragraphs.append(line)

	# Transcript is a dictionary consisting of {timestamp: pragraph}
	transcript = dict(zip(timestamps,paragraphs))

	return transcript
	"""
	stem_transcript = {}

	for key, value in transcript.iteritems():
		stem_transcript[key] = para_to_cloud(value)

	return stem_transcript
	"""

def most_relevant_snippets(question, filename):
	stem_transcript = file_to_transcript(filename)
	#query_cloud = para_to_cloud(question)
	query_cloud = question.lower()
	snippets = []
	
	for key, value in stem_transcript.iteritems():
		weight = len(set.intersection(set(query_cloud), set(value)))
		print value
		snippets.append((weight, key))

	snippets = sorted(snippets, key = lambda x: (-x[0],x[1]))
	print snippets 



# filename = raw_input("Enter the name of the transcript file as [data/*.txt]: ")
# question = raw_input("Enter your question: ")
#filename = 'data/Juan_Enriquez.txt'


filename = 'data/Sugata_Mitra.txt'
question = 'What is a granny cloud?'

most_relevant_snippets(question, filename)
#print para_to_cloud(question)

"""
The next stage is to take a question and find the relevant paragraphs

"""

