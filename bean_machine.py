import sys, getopt, random

DECIMALS = 2;

# random_box return the specific box where a ball fell
def random_box(levels):
	box_result = 0
	for x in range(levels):

		# get a random number between 0.0 and 1.0
		side =  random.random()

		# if random number is bigger than 0.5 it represent that ball go to right
		if side > 0.5:
			box_result = box_result + 1
		# otherwise it represent that ball go to left
	return box_result


def throw_balls(balls,levels,boxes):
	for x in range(balls):
		drop = random_box(levels)
		boxes[drop] = boxes[drop] + 1
	return boxes;


def main(argv):
	levels = 1
	balls = 1
	percent = False
	try:
	  opts, args = getopt.getopt(argv,"hl:b:p",["levels=","balls="])
	except getopt.GetoptError:
	  print '-l <number_of_levels> -b <number_of_balls> -p < result in percent>'
	  sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print '-l <number_of_levels> -b <number_of_balls>'
			sys.exit()
		elif opt in ("-l", "--levels"):
			try:
				levels = int(arg)
				if levels < 1:
					print "Min level: 1"
					sys.exit()
			except ValueError:
				print "Not a number"
				sys.exit()

		elif opt in ("-b", "--balls"):
			try:
				balls = int(arg)
				if balls < 0:
					print "Min of balls: 1"
					sys.exit()

			except ValueError:
				print "Not a number"
				sys.exit()

		elif opt in ("-p", "--percent"):
			percent = True

		


	print 'Number of levels: ', levels
	print 'Total of balls: ', balls



	# number of boxes
	num_boxes = levels + 1 

	# create list and reset it
	boxes = [0 for x in range(num_boxes)]

	result = throw_balls(balls,levels,boxes)

	if percent:
		result = [str(round((x/float(balls))*100,DECIMALS)) + '%' for x in result]

	print result



if __name__ == "__main__":
   main(sys.argv[1:])
