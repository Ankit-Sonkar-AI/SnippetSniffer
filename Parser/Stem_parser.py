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
	stem_cloud = set([inception]) | set(hobj.suggest(inception)) 
	
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
			paragraphs.append(line)

	# Transcript is a dictionary consisting of {timestamp: pragraph}
	transcript = dict(zip(timestamps,paragraphs))
	stem_transcript = {}

	for key, value in transcript.iteritems():
		stem_transcript[key] = para_to_cloud(value)

	return stem_transcript

# filename = raw_input("Enter the name of the transcript file as [data/*.txt]: ")
# question = raw_input("Enter your question: ")



filename = 'data/Juan_Enriquez.txt'
filename = 'data/Sugata_Mitra.txt'


"""
mystring = "Hello world! (How) are you (now) sister?"

for m in mystring.split(' '):
	print m


start = mystring.find( '(' )
end = mystring.find( ')' )
if start != -1 and end != -1:
  result = mystring[start+1:end]

print result
"""