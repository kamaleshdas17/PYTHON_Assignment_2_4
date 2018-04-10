"""
Write a Python Program to print the given string in the format specified in the sample
output.
WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
its citizens
Sample Output:
WE, THE PEOPLE OF INDIA,
	having solemnly resolved to constitute India into a SOVEREIGN, !
		SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
			and to secure to all its citizens:

"""
str="WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens"

lst=str.split(',')

##['WE', ' THE PEOPLE OF INDIA', ' having solemnly resolved to constitute India into a SOVEREIGN', ' SOCIALIST', ' SECULAR', ' DEMOCRATIC REPUBLIC and to secure to all its citizens']

j=1
line1=[]
line2=[]
line3=[]
for i in range(len(lst)):
	
	if i < 2:
		line1.append(lst[i] + ',')
		str1=''.join(line1)
	elif i==2:
		line2.append(lst[i] +', !')
		str2=''.join(line2)
	elif i>2:
		line3.append(lst[i] + ',')
		str3=''.join(line3)

str3_sublist=str3.split('and')

print('Sample Output: \n----------------------------------------------------------------')
print (str1)
print ("\t"+str2)
print ("\t\t"+str3_sublist[0])
print ("\t\t\t and"+str3_sublist[1].replace(',',':'))




		
