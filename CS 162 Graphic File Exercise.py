
import matplotlib.pyplot as plot
# set up your lists
numlist = [12, 4, 18, 9]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['red', 'green', 'pink', 'yellow' ]
explodelist = [0.08, 0.08, 0.08, 0.08]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.4f%%', colors=colorlist,
    	explode = explodelist, startangle = 270)
plot.axis('equal')
plot.savefig('piechart.png')

