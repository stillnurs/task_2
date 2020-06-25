print('Enter first time: ')
a_hours = int(input('Hours: '))
a_minutes = int(input('Minutes: '))
a_seconds = int(input('Seconds: '))

print('Enter second time: ')
b_hours = int(input('Hours: '))
b_minutes = int(input('Minutes: '))
b_seconds = int(input('Seconds: '))

a_converted_to_seconds = (a_hours * 60 + a_minutes) * 60 + a_seconds
b_converted_to_seconds = (b_hours * 60 + b_minutes) * 60 + b_seconds

a_b_difference = a_converted_to_seconds - b_converted_to_seconds

print('Difference: ' + str(abs(a_b_difference)))

