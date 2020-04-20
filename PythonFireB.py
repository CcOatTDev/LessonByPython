from firebase import firebase

url ='https://pythonwithfirebase-19615.firebaseio.com/'
messenger = firebase.FirebaseApplication(url)

engineer = {'id':1003,'name':'Amarilo_11'}
engineer2={'id':1004,'name':'Ruby_11'}

result = messenger.put('/users','1',engineer)
result2 = messenger.put('/users','2',engineer2)
messenger.put('/users','3',engineer2)

print("Engineer 1", result)
print("Engineer 2", result2)