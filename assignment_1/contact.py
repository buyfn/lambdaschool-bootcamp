import requests

data = {'name': 'Ignat',
        'lastname': 'Petrenko',
        'email': 'buyfng@gmail.com',
        'message': 'Sir, let me convey to you, with this http request, my proufound respect and warmest thanks for blessing us with your divine teachings. Your most humble and obedient servant: I.'}

r = requests.post('https://lambdaschool.com/contact-form', json = data)
