from grab import Grab
g = Grab()
g.go('https://home.openweathermap.org/users/sign_in')
g.doc.set_input('user[email]', 'popov.anatoly@gmail.com')
g.doc.set_input('user[password]', '20111982')
g.doc.submit()
# g.go('https://home.openweathermap.org/api_keys')