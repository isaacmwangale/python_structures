# Use the file name mbox-short.txt as the file name
'''Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below''' 


fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
       #print(line.rstrip())
       xx = line.find('0')
       yy = line[xx:]
       num = float(yy)
       #print(num)
       tot = tot + num
       count = count + 1
#print(count, tot)
print('Average spam confidence:',tot/count)


