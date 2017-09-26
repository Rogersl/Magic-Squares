'''
Logan Rogers

Magic squares problem

Tested and made on python 2.7.6

Be sure when running this program in terminal to remove the column limitation
for output, otherwise line-wrap messes up table printing.

row/column/diagonal sum = (n * (n**2 + 1) / 2)

Input value n must be of value > 2
'''

#This function creates a magic-square for doubly-even n. (n divisible by 4)
#Uses the 3rd method described here: http://www.1728.org/magicsq2.htm
def doubly_even_magic_square(n):

	matrix = [[0 for x in range(n)] for y in range(n)]

	partition = n/4	#bound marker for rectangular segments

	count = 1 		#starting value for initial fill

	#fill spots in select rectangular segments
	for i in range(n):
		for j in range(n):
			#left segment
			if i >= partition and i < 3*partition and j < partition:
				matrix[i][j] = count

			#top segment
			if i < partition and j >= partition and j < 3*partition:
				matrix[i][j] = count
			
			#bottom segment
			if i >= 3*partition and j >= partition and j < 3*partition:
				matrix[i][j] = count

			#right segment
			if i >= partition and i < 3*partition and j >= 3*partition:
				matrix[i][j] = count

			count += 1

	count = n**2 		#starting value for backfill

	#backfill empty spots
	for i in range(n):
		for j in range(n):
			if matrix[i][j] == 0:
				matrix[i][j] = count
			count -= 1

	return matrix

#This function creates an odd n magic-square.
def odd_magic_square(n):
	matrix = [[0 for x in range(n)] for y in range(n)]

	#initial starting point (top middle)
	row, col, square = 0, n//2, n**2

	#loop through, adding values and ensuring we stay within bounds.
	#(up-right diagonal move w/ wrap-around, moving down when encountering
	# an occupied spot)
	for i in range(1,square+1):
		matrix[row][col] = i
		if i % n == 0:
			row += 1
		else:
			if row == 0:
				row = n - 1
			else:
				row -= 1
			if col == n - 1:
				col = 0
			else:
				col += 1

	return matrix

#This function creates a magic-square for singly-even n (even n not divisible by 4)
#Uses the method described here: http://www.1728.org/magicsq3.htm
def singly_even_magic_square(n):

	matrix = [[0 for x in range(n)] for y in range(n)]

	partition = n // 4					#width of column swapping left edge

	swap_edge_width = partition - 1 	#width of rightmost swap edge

	half_size = n/2 					#n/2, used for solving sub-matrix

	base_addition = half_size**2 		#base addition amount for copying solved sub-matrix

	#Solve matrix of size n/2xn/2 (odd magic square) for basis
	#of the full magic sqaure
	sub_matrix = odd_magic_square(half_size)

	#copy values of solved sub-sqaure to full matrix, adding values based on quadrant
	#
	for i in range(n):
		for j in range(n):
			#top left corner of full matrix
			if i < half_size and j < half_size:
				matrix[i][j] = sub_matrix[i][j]

			#top right corner of full matrix
			if i < half_size and j >= half_size:
				matrix[i][j] = sub_matrix[i][j-half_size] + 2*base_addition

			#bottom left corner of full matrix
			if i >= half_size and j < half_size:
				matrix[i][j] = sub_matrix[i-half_size][j] + 3*base_addition

			#bottom right corner of full matrix
			if i >= half_size and j >= half_size:
				matrix[i][j] = sub_matrix[i-half_size][j-half_size] + base_addition

	#debug
	#print_matrix(matrix,n)

	#Swap select elements from upper-left and lower-left quadrants
	for j in range(partition):
		for i in range(half_size):
			if i != partition:
				temp = matrix[i][j]
				matrix[i][j] = matrix[i+half_size][j]
				matrix[i+half_size][j] = temp
			if i == partition:
				temp = matrix[i][j+1]
				matrix[i][j+1] = matrix[i+half_size][j+1]
				matrix[i+half_size][j+1] = temp

	#Swap select elements from upper-right and lower-right quadrants
	if swap_edge_width >= 1:
		for j in range(n-swap_edge_width, n):
			for i in range(half_size):
				temp = matrix[i][j]
				matrix[i][j] = matrix[i+half_size][j]
				matrix[i+half_size][j] = temp

	return matrix

#Function to print the matrix, using tab spacing
def print_matrix(magic_square,n):
	for i in range(n):
		for j in range(n):
			if j == n-1:
				print magic_square[i][j]
			else:
				print '%s \t' %(magic_square[i][j]),

def main():
	
	#Get input size n
	n = raw_input('Input integer size of magic square (n > 2): ')
	n = int(n)
	while (n < 3):
		n = raw_input('Please input integer n > 2: ')
	n = int(n)

	#output sum formula
	print 'Sum of rows/columns/diagonals = (n * (n^2 + 1)) / 2\n'

	#Check if n in singly/doubly even or odd, and run
	#magic square algorithm based on that.
	if n%4 == 0:
		magic_square = doubly_even_magic_square(n)
	else if n%2 == 0:
		magic_square = singly_even_magic_square(n)
	else:
		odd_magic_square(n)

	print '%s x %s Magic Square: ' %(n,n)
	print_matrix(magic_square,n)

	#Formula to calculate sum.
	sum = (n * (n**2 + 1)) / 2

	print '\nSum of rows/columns/diagonals: %s' %(sum)
	print '\n\n'

if __name__ == '__main__':
	main()