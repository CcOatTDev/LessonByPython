from firebase import firebase

url ='https://pythonwithfirebase-19615.firebaseio.com/'
messenger = firebase.FirebaseApplication(url)

result = messenger.get('/users', None)
print(result)

result = messenger.get('/users', '1')
print(result)

result = messenger.get('/users/2', None)
print(result)