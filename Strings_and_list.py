#Strings and List theory and examples

tea_party = ['March Hare', 'Hatter', 'Dormouse', 'Alice']
print tea_party[2]

tea_party[1] = 'Cheshire Cat'
print tea_party

tea_party.append('Jabberwocky') #append() method: Add items to the end of an existing list
print tea_party

print tea_party[0:2] #displays the elements from 0 to 2 not including 2
print tea_party[:2] #display from 0 to 2, without 2
print tea_party[3:] #display from 3 till the end, including 3

a = 'Sheldom'
b = 'Amy'
c = a[:2] + b[0:3]
print c #Use the same comands for list on a string to slice it

# Problem: Given a string s of length at most 200 letters and four integers a, b, c and d. 
# Return: The slice of this string from indices a through b and c through d (wit space in between), inclusively.

a = 76
b = 82
c = 157
d = 166
string = 'sOWilLMqtdwannEj1vRLTvO31ZH6cv2HsIGDFZoSx7ueT30yL47lDyCpRgO1C5PS6FO23mDI1YSFKassinaFPdWziEXDBDCDB7vMgAvjyhsoun5NLmhwCbaw3ZXFWYUWC6Vzqh6J22stqxaXtO7x0NhvKqjZ5hendersonidHREZ.'
print string[a:(b+1)] + ' ' + string[c:(d+1)]

