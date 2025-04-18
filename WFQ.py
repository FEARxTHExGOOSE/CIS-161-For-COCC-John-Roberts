from collections import deque
#These are the empty lists for the for loop to fill up via appending with data from reading
#the .txt file.
premium_data=[]
standard_data=[]
economy_data=[]

#This block of code loops through the .txt file and appends to the empty lists above by
#comparing the first letter of each line of text in order to match it with the appropriate
#data set. I looked up the strip command due to the data coming out with a \n added to the end.
with open("C:\WFQ Assignment\input queue-1.txt","r") as packets_list:
	for packets in packets_list:
		packets = packets.strip()
		if packets[0] == "P":
			premium_data.append(packets)
		elif packets[0] == "S":
			standard_data.append(packets)
		elif packets[0] == "E":
			economy_data.append(packets)

print("Premium Queue Data:")
print(premium_data)
print("")

print("Standard Queue Data")
print(standard_data)
print("")

print("Economy Queue Data")
print(economy_data)
print("")

# I did this in two different ways, primarily so I could ask you if you had any ideas for
# how I could have these while loops run within one another, so that I could have the
# number they are comparing to iterate as well. So that one iteration would essentially
# be one while loop and I could eliminate the other while loop blocks.
print("Queue via While Loops:")
print("")
print("Collective Queue:")
collective_queue=[]

premium_queue=0
standard_queue=0
economy_queue=0

#These while loop iterations are looping through and appending the data from the appropriate
#lists in order to add them to the collective_queue list in the proper order.

#First Queue Iteration
while premium_queue <=2:
	collective_queue.append(premium_data[premium_queue])
	premium_queue+=1

while standard_queue <= 1:
	collective_queue.append(standard_data[standard_queue])
	standard_queue+= 1

while economy_queue <= 0:
	collective_queue.append(economy_data[economy_queue])
	economy_queue += 1


#Second Queue Iteration
while premium_queue <=5:
	collective_queue.append(premium_data[premium_queue])
	premium_queue+=1

while standard_queue <= 3:
	collective_queue.append(standard_data[standard_queue])
	standard_queue+= 1

while economy_queue <= 1:
	collective_queue.append(economy_data[economy_queue])
	economy_queue += 1


# Third Queue Iteration
while premium_queue <=7:
	collective_queue.append(premium_data[premium_queue])
	premium_queue+=1

while economy_queue <= 7:
	collective_queue.append(economy_data[economy_queue])
	economy_queue += 1


print(collective_queue)
print("")

# This method with the deque function certainly takes up more space, but it is radically
# simpler in the execution of building the full collective queue by going through each packet
# one by one.

print("Queue via Deque Function:")
q = deque()
q.append(premium_data[0])
q.append(premium_data[1])
q.append(premium_data[2])
print("Premium queue")
print(q)
print("")

q.append(standard_data[0])
q.append(standard_data[1])
print("Standard queue added")
print(q)
print("")

q.append(economy_data[0])
print("Economy queue added")
print(q)
print("")

q.append(premium_data[3])
q.append(premium_data[4])
q.append(premium_data[5])
print("Premium queue added")
print(q)
print("")

q.append(standard_data[2])
q.append(standard_data[3])
print("Standard queue added")
print(q)
print("")

q.append(economy_data[1])
print("Economy queue added")
print(q)
print("")

q.append(premium_data[6])
q.append(premium_data[7])
print("Premium queue added")
print(q)
print("")

q.append(economy_data[2])
q.append(economy_data[3])
q.append(economy_data[4])
q.append(economy_data[5])
q.append(economy_data[6])
q.append(economy_data[7])
print("Economy queue added, queue complete")
print(q)

