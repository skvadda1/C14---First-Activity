file = open('the_essay.txt' , 'r')
print(file.read())
file.close()

file = open('the_essay.txt' , 'r')
print("\n Read In Parts \n")
print(file.read(5))
file.close()

file = open('the_essay' , 'a')
file.write("Take Use Of This Advice")
file.close()