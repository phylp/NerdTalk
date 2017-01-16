#Strip all text that follows any of a set of comment markers passed in as a second argument. 
#Any whitespace at the end of the line should also be stripped out.

def strip_comments(message, markers):
	new_message = ''
	omitting = False
	markers_u = [unicode(i) for i in markers]
	for i in range(0, len(message)):
		if message[i] == '\n':  
			omitting = False
			new_message += message[i]
		elif unicode(message[i]) in markers_u: 
			omitting = True
		elif message[i] == ' ' and message[i + 1] in markers:
			continue
		elif omitting == True: 
			continue
		else:                 
			new_message += message[i]

	return new_message


			

