import os
import sys
import time

# Grab command line parameter
ScriptName = sys.argv[0]
ac = len(ScriptName)
if len(sys.argv)<2:
  print("Usage: "+ScriptName+" <BFI Data File>")
  exit(1)
file2process = sys.argv[1]

# Start the time counter
t1 = time.time()
timeStamp = time.strftime(" %H %M %S %d-%m-%Y")

#################
# Sort the data
#################

input_file = file2process
out_f = "Sorted-"+input_file

of = open(out_f,'w', encoding='utf-8', errors='ignore')

print("Sorting "+input_file+" into "+out_f)

with open(input_file, encoding='utf-8', errors='ignore') as f:  # Converting to Python3 with Unicode
   lines = f.readlines()
   lines.sort()        
   f.seek(0)
   for n in lines:
      of.write(n)
f.close()
of.close()

#################
# Count the data
#################

in_file = "Sorted-"+input_file
out_f = "Counted-"+in_file

of = open(out_f, 'w', errors='ignore')

print("Counting "+in_file+" into "+out_f)

f = open(in_file, errors='ignore') 
counter = 0 

for line in f:
   line = line.strip()
   if len(line) == 0:
      continue
   if counter == 0:
      prevLine = line
   if line == prevLine: 
      counter = counter + 1
   else:
      out_line = prevLine+"\t"+str(counter)+"\n"
#      print(out_line.strip())
      of.writelines(out_line)
      counter = 1
   prevLine = line
f.close()
of.close()

#################
# Done
#################

t2 = time.time()
t3 = t2 - t1
t4 = t3/60
t5 = t3%60
print('All products sorted and counted in %d minutes and %d seconds\a\n' % (t4,t5))
# Make a bell tone so you don't have to watch the screen the whole time.
print("\a")