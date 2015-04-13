import csv

manigga = 0
with open('crimes_since_2009.csv', 'rb') as csvfile:
     crimereader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in crimereader:
     	print row
     	print row[1]
     	print row[2]
       	for word in row:
       		print word 
        	manigga = manigga + 1 
     	if manigga > 100:
     		break


#if __name__ == "__main__": 
 #   main()