import re
par = open('JuanEnriquez_2016T-480p.txt').read()
q = re.split("[0-9]+:[0-9]+\n", par)
q.pop(0)
#print(len(q))

