from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
accountSID = "AC7a9b9c46e51c9c4ac6d218a3300d4c60"
authToken = "5bd5db0d26521201026660b0138d22eb"
myNumber = "9178431278"
twilioNumber = "+15163500538"

def textmyself(message):
	twilioCli = Client(accountSID,authToken)
	twilioCli.messages.create(body=message,from_=twilioNumber, to=myNumber)
	    


textmyself("Good Afternoon, Man!!")
