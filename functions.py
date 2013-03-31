import random

def targetPeep(users):
  target = random.choice(users)
  textPeeps([target], "You are the target")
  f = open('target', 'w')
  f.write(target)
  f.close()
  return target

def textPeeps(number, string):
  account  = "ACebee71a1ea0c79fd0f8b2f3eedb4e816"
  token = "3e0adb5bc52d10c6984b6aa96fa95182"
  client = TwilioRestClient(account, token)
  for each txtNum in number:
    message = client.sms.messages.create(to=txtNum, from_="+14845884913", body=string)

def namefile2array(filename):
	a = []
	with open(filename) as f:
		for line in f:
			newline = line.split('\t')
			a.append(newline[0])
	f.close()
	return a

def numberfile2array(filename):
	b = []
	with open(filename) as f:
		for line in f:
			newline = line.split('\t')
			b.append(newline[1])
	f.close()
	return b

