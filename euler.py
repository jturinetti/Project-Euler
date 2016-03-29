from functools import reduce
from math import sqrt

#helpers
def factorial(num):
    if (num > 1):
        return num * factorial(num - 1)
    else:
        return num

def find_prime_factors(num):
    arr = []
    counter = 2
    while (counter <= num):
        if (num % counter == 0):
            arr.append(counter)
            num = num / counter
            counter = 1
        counter = counter + 1    
    return arr

def prime_numbers(num_to_find):
    prime_numbers = [2]
    done = False
    counter = 3
    while (not done):
        isPrime = True
        for pn in prime_numbers:
            if (counter % pn == 0):
                isPrime = False

        if (isPrime):
            prime_numbers.append(counter)
        
        if (len(prime_numbers) >= num_to_find):
            done = True
            
        counter = counter + 2
    return prime_numbers

def prime_numbers_below(num):
    prime_numbers = [2]    
    done = False
    counter = 3
    while (not done):        
        isPrime = True
        for pn in prime_numbers:
            if (counter % pn == 0):
                isPrime = False

        if (isPrime):
            prime_numbers.append(counter)
            print("prime numbers found: ", len(prime_numbers))
            print("last prime number found: ", counter)
        
        if (counter > num):
            done = True
            
        counter = counter + 2
    return prime_numbers

#euler problem 5
def lowest_common_multiple(num):
    num_prime_factors = []
    for counter in range(2, num + 1):
        prime_factors = find_prime_factors(counter)
        distinct_factors = set(prime_factors)
        for factor in distinct_factors:
            difference = prime_factors.count(factor) - num_prime_factors.count(factor)
            if (difference > 0):
                factors_to_add = 0
                while (factors_to_add < difference):
                    num_prime_factors.append(factor)
                    factors_to_add = factors_to_add + 1
    num_prime_factors.sort()
    print(num_prime_factors)
    return reduce(lambda x,y: x*y, num_prime_factors)

#euler problem 6
def sum_square_difference(num):
    summed_squares = sum([i ** 2 for i in range(1, num + 1)])
    squared_sum = (sum(range(1, num + 1))) ** 2
    print (summed_squares)
    print (squared_sum)
    return squared_sum - summed_squares


#euler problem 7
def prime_factor_10001():
    return prime_numbers(10001)[10000]

#euler problem 8
def largest_product_in_series():
    large_number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    largest_product = 0
    starting_index = 0
    while (starting_index < len(large_number) - 13):                
        sub_array = large_number[starting_index:starting_index + 13]        
        
        if ("0" in sub_array):
            #product is 0, move index and continue loop
            starting_index = starting_index + sub_array.find("0") + 1
        else:
            product = reduce(lambda x,y: int(x)*int(y), sub_array)
            if (product > largest_product):
                largest_product = product            
            
            starting_index = starting_index + 1
            
    return largest_product

#euler problem 9
def pythag_triplet():
    actual_a = 0
    actual_b = 0
    done = False
    for a in range(1, 1000):
        for b in range(1, 1000):            
            output = (a + b + sqrt(a**2 + b**2))
            if (output == 1000):
                actual_a = a
                actual_b = b
                done = True
            if (done):
                break
        if (done):
            break
    c = sqrt(actual_a ** 2 + actual_b ** 2)
    print(actual_a)
    print(actual_b)
    print(c)
    return actual_a * actual_b * c

#euler problem 10
def summation_of_primes():
    #THIS TAKES A LONG TIME, NEED TO OPTIMIZE
    primes_list = prime_numbers_below(2000000)
    return sum(primes_list)

#euler problem 11
def largest_product_in_grid():
    grid = []
    grid_string =  '''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
'''.strip()
    for line in grid_string.splitlines():
        grid.append([int(number) for number in line.split()])

    largest_product = 0
    x = 0
    y = 0
    while (x < (len(grid))):
        while (y < (len(grid[x]))):            
            #horizontal
            if (y < len(grid[x]) - 3):
                #print ("horizontal mult: {0} * {1} * {2} * {3}".format(grid[x][y], grid[x][y+1], grid[x][y+2], grid[x][y+3]))
                product = grid[x][y] * grid[x][y+1] * grid[x][y+2] * grid[x][y+3]
                if (product > largest_product):
                    largest_product = product
            if (x < (len(grid) - 3)):
                #vertical
                #print ("vert mult: {0} * {1} * {2} * {3}".format(grid[x][y], grid[x+1][y], grid[x+2][y], grid[x+3][y]))
                product = grid[x][y] * grid[x+1][y] * grid[x+2][y] * grid[x+3][y]                
                if (product > largest_product):
                    largest_product = product
            if (x < (len(grid) - 3) and y < len(grid[x]) - 3):
                #diagonal to the right
                #print ("diag mult: {0} * {1} * {2} * {3}".format(grid[x][y], grid[x+1][y+1], grid[x+2][y+2], grid[x+3][y+3]))
                product = grid[x][y] * grid[x+1][y+1] * grid[x+2][y+2] * grid[x+3][y+3]                
                if (product > largest_product):
                    largest_product = product
            if (x < (len(grid) - 3) and (y - 3) > 0):
                #diagonal to the left
                #print ("diag mult: {0} * {1} * {2} * {3}".format(grid[x][y], grid[x+1][y-1], grid[x+2][y-2], grid[x+3][y-3]))
                product = grid[x][y] * grid[x+1][y-1] * grid[x+2][y-2] * grid[x+3][y-3]
                if (product > largest_product):
                    largest_product = product
            y = y + 1
        y = 0        
        x = x + 1
    return largest_product
        
# MAIN
print(largest_product_in_grid())
