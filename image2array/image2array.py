#need to turn 90 degrees 
#need to reverse odd rows

from PIL import Image
import numpy as np
openfile = raw_input('Enter a filename: ') or 'default_file.asm'

i = Image.open(openfile)

#passes name of file to n
n = open(openfile)

# cutting the everything after the . off
text = n.name
filename, sep, tail = text.partition('.')
# get the w/h of the image
width, height = i.size

iar = np.asarray(i)
print(iar)

print('fliped')

iar = iar[::-1,:,:]
print(iar)

width_string=str(width)
height_string=str(height)
print('image width  '+width_string)
print('image height  '+height_string)

re_orrder_array = np.zeros((width,height,3))


### this counts up 
array_lenght2 = 0
while array_lenght2 < len(iar):
  array_lenght = 0
  #print b
  print(' ')
  print(' ')
  while array_lenght < len(iar):
    print(iar[array_lenght][array_lenght2])
    #iar[array_lenght][array_lenght2] = re_orrder_array

    re_orrder_array[array_lenght2][array_lenght][0] = iar[array_lenght][array_lenght2][0]
    re_orrder_array[array_lenght2][array_lenght][1] = iar[array_lenght][array_lenght2][1]
    re_orrder_array[array_lenght2][array_lenght][2] = iar[array_lenght][array_lenght2][2]
    
    array_lenght += 1
  array_lenght2 += 1

### this counts down
#array_lenght2 = 1
#while array_lenght2 < len(iar):
 # array_lenght = len(iar)
  #print b
 # print(' ')
 # print(' ')
 # while array_lenght > 0:
 #   print(iar[array_lenght-1][array_lenght2])
 #   re_orrder_array[array_lenght2][array_lenght-1][0] = iar[array_lenght-1][array_lenght2][0]
 #   re_orrder_array[array_lenght2][array_lenght-1][1] = iar[array_lenght-1][array_lenght2][1]
 #   re_orrder_array[array_lenght2][array_lenght-1][2] = iar[array_lenght-1][array_lenght2][2]
 #   array_lenght -= 1
 # array_lenght2 += 2
		

print(re_orrder_array)





with open(filename + "_.c", 'w') as outfile:

    # Writing out a break to indicate different slices...
    outfile.write('int LED_'+ filename+'[]['+width_string+'][3] = {\n') # 3d array width/hight + rgb values
    for data_slice in re_orrder_array: 
    	outfile.write('\n') 
        outfile.write('{\n')
        
        np.savetxt(outfile, data_slice,fmt='{%1.0f, %1.0f, %1.0f},') #fmt='{%1.0f %1.0f %1.0f},)'
        outfile.write('},')
        outfile.write('\n')
    outfile.write('};\n')
