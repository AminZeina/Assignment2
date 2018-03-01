# Created By: Amin Zeina
# Created On: Feb 2018

radius = int(input("Please Enter the Radius: "))

circumferenceOrArea = input('''
Type "Area" to calculate area
Type "Circumference" to calculate circumference
''')

if circumferenceOrArea == 'Area':
	print( 3.14 * ( radius * radius ))

elif circumferenceOrArea == 'Circumference' :
    print( 2 * radius * 3.14 )

else:
	print('Invalid operation, please restart the program using "Area" or "Circumference"')

input('End of Program')
