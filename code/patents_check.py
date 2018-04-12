input_file = open('claim.tsv','r')
output_file = open('claim500.txt','w')
 
for lines in range(50000):
    line = input_file.readline()
    output_file.write(line)