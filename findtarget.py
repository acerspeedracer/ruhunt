import pickle
import random
f=open("/home/ss1925/pickledump","r")
users = pickle.load(f)
f.close()
target = random.choice(users)
print target
