user_text = list(input('Enter here: '))
upper_letters = lower_letters = 0


for i in user_text:
    if i.isupper():
        upper_letters += 1
        
    elif i.islower():
        lower_letters += 1
    else:
        continue

print('Upper case percentage: ' + str((100 * upper_letters / len(user_text))))

print('Lower case percentage: ' + str((100 * lower_letters / len(user_text))))