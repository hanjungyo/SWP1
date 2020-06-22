from cgi import parse_qs
from template2 import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])

	a = d.get('a', [''])[0]
	b = d.get('b', [''])[0]

	if '' not in [a,b]:
		a, b = int(a), int(b)
		x = a + b
 		y = a * b
 	
	else:
		x = "Please enter both values." 
		y = "Please enter both values." 




	response_body = html % {
		'x': x,
		'y': y,	
	}

	status = '200 OK'
	response_headers = [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	]

	start_response(status, response_headers)
	return [response_body]
