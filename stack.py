import requests
import sys
import time

f = open(sys.argv[1],"r")
for l in f:
	if l.find("stackover") != -1:
		time.sleep(1)
		try:
			r = requests.get(l.rstrip())
			source = r.text
			i_anwser = source.find('<div id="answers">')
		except HTTPError as http_err:
        		print(f'HTTP error occurred: {http_err}')  # Python 3.6
		except Exception as err:
        		print(f'Other error occurred: {err}')  # Python 3.6	
		else:
			if i_anwser == -1 and r.status_code not in [429,404]:
				print (str(i_anwser)+": "+l+" status: "+str(r.status_code))
			if r.status_code == 429:
				print (r.headers)
				print (r.text)
				sys.exit()

