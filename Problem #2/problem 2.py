pl=['Mahamakut Building','Sara Phra Kaew','CU Sport Complex','Sanum Juub','Samyan Mitr Town']
def checkin(phone,place):
  a=pl[int(place)-1]
  f = open(a+".txt", "r")
  lines = f.readline()
  if(phone+'\n' in lines or phone==lines[-1] or phone==lines[0]):
    print('this phone number already checkin')
    f.close()
  else:
    f.close()
    for i in range(5):
      a=pl[i]
      f = open(a+".txt", "r")
      lines = f.readlines()
      f.close()
      f = open(a+".txt", "w")
      for line in lines:
        print(line)
        if line.strip("\n") != phone:
          f.write(line)
      f.close()
    f = open(pl[int(place)-1]+".txt", "a")
    f.write(phone+'\n')
    print('Checking in ' + phone + ' into ' +pl[place-1])
    f.close()
def checkout(phone):
  check=0
  for i in range(5):
    a=pl[i]
    f = open(a+".txt", "r")
    lines = f.readlines()
    if(phone+'\n' in lines or phone==lines[-1] or phone==lines[0]):
      f.close()
      f = open(a+".txt", "w")
      for line in lines:
        print(line)
        if line.strip("\n") != phone:
            f.write(line)
      f.close()
      check=1
  if(check==0):
    print('this phone is not checkin')
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
  checkin(phone,place)
if(command=='2'):
  print('-----------------------------------------------------------------')
  print('Check out')
  phone = input('Enter phone number: ')
if(command=='3'):
  print('-----------------------------------------------------------------')
  
