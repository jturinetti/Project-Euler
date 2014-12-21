from functools import reduce

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
        

# MAIN
print(largest_product_in_series())
