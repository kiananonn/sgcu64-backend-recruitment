pl=['Mahamakut Building','Sara Phra Kaew','CU Sport Complex','Sanum Juub','Samyan Mitr Town']
print('''Welcome to Chula Chanal!!!
Available commands:
        1. Check in user
        2. Check out user
        3. Print people count''')
command = input('Please input any number: ')
if(command=='1'):
  print('-----------------------------------------------------------------')
  print('Check in')
  phone = input('Enter phone number: ')
  print('''  1. Mahamakut Building
  2. Sara Phra Kaew
  3. CU Sport Complex
  4. Sanum Juub
  5. Samyan Mitr Town''')
  place = int(input('Select the place: '))
  print('Checking in ' + phone + ' into ' +pl[place-1])
if(command=='2'):
  print('-----------------------------------------------------------------')
  print('Check out')
if(command=='3'):
  print('-----------------------------------------------------------------')
  print('Current Population: ')
  print('1. Mahamakut Building: ')
  print('2. Sara Phra Kaew: ')
  print('3. CU Sport Complex: ')
  print('4. Sanum Juub: ')
  print('5. Samyan Mitr Town: ')
