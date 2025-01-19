#Question 1
#This code is used for printing the binary and hex value of variable "x"
from operator import invert

x = 31
print(x, bin(x), hex(x))

#Question 2

#I got an error saying that 'float' object cannot be interpreted as an integer
#This is because python cannot use floaters as an integer, and you also cannot have python read "x" as an integer using the "int()" command

x = 18
print (x, bin(x), hex(x))

#Question 3
#This code is for assigning a binary or hex value to a variable
y= 0b1011
z= 0xA3
print(y,z)

#Question 4
#This code is for showing you can add numbers in any representation
w= x + y + z
print('the sum is',w)


#Compression Questions

#Part 1
#This program is used for calculating compression percentage
original_size= 240
dictionary_size= 25
compressed_text_size= 148

percent_of_compression= 1-((compressed_text_size + dictionary_size) / original_size)
compression_percent_conversion= percent_of_compression * 100
rounded_compression_percent= round(compression_percent_conversion,2)

#Part 2
print(f'{rounded_compression_percent}%')

#Part 3-4
#This is the same code but using my own variable values for testing compression percentage
original_size= 465
dictionary_size= 42
compressed_text_size= 288
total= compressed_text_size + dictionary_size

#All of this is for converting compression decimal to percentage amount and rounding to 2 decimals
percent_of_compression= 1-((compressed_text_size + dictionary_size) / original_size)
compression_percent_conversion= percent_of_compression * 100
rounded_compression_percent= round(compression_percent_conversion,2)

print('Compressed Text Size:   ', compressed_text_size, 'characters')
print('Dictionary Size:        ', dictionary_size, 'characters')
print('Total:                  ', total, 'characters')
print('Original Text Size:     ', original_size, 'characters')
print(f'Compression Percentage:  {rounded_compression_percent}%')

#Extra Credit

first_number= input('Enter a number: ')
bin_second=(bin(int(first_number)))
#These two lines are for getting rid of the "b" when printing and getting all  8 digits to show in binary

bin2_no_b= bin_second[2:]
full_bin2= ((bin2_no_b).zfill(8))
print(full_bin2)

#This is as far as I could get without having to look up the code online for two's complement

