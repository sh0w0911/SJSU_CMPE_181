def send_simple_message():
	return requests.post(
		"https://https://api.mailgun.net/v3/sandbox7fb0153697a44970b7a430530ca48afc.mailgun.org/messages",
		auth=("api", "82c4b9fd1cbae184e3defe7c686a5cbd-a09d6718-76d4880f"),
		data={"from": 'hello@example.com',
			"to": ["suyeob.kim@sjsu.edu"],
			"subject": "Set up email notification",
			"text": "Your Rasberry Pi set up successfully!"})

request = send_simple_message()
print ('status: ' + format(request.status_code))
print ('Body: ' + format(request.text))
