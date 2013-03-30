import sendgrid

s = sendgrid.Sendgrid('ace6598','aiser12',Secure=True)

message = sendgrid.Message("ace6598@gmail.com", "SUBJECT", "HERRO", "nothing?")

message.add_to("wlangfor@gmail.com", "William Langford")

s.web.send(message)
