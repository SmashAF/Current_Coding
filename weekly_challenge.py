    
'''
March 15th, 2021
'''

'''
Finish the cels_to_fahr and fahr_to_cels functions below. These functions should convert from celsius to 
fahrenheit and vice versa. Their parameters will be temperature in one system, and it should return the 
temperature converted to the other system.

Conversion equations:
To convert from celsius to fahrenheit:
F=C⋅95+32
To convert from fahrenheit to celsius:
C=(F−32)⋅59
'''

def cels_to_fahr(temp_c):
    return round((temp_c * 1.8) + 32)

# print (cels_to_fahr(10))      #50
# print (cels_to_fahr(38))     #100
# print (cels_to_fahr(-40))     #-40 

def fahr_to_cels(temp_f):
    return round((temp_f - 32) * .5556)
   
# print (fahr_to_cels(50))      #10
# print (fahr_to_cels(100))     #38
# print (fahr_to_cels(-40))     #-40
'''
Write a function called fast_fib which takes one parameter, n, which is the n-th term of the Fibonacci
sequence. This is a classic problem to do recursively (learn more about recursion here  ), but the naive
recursive approach is incredibly slow. This fast Fibonacci program should use a for loop to calculate 
the n-th term of the Fibonacci sequence.

The Fibonacci seqence is calculated by summing the two previous terms in the sequence, with 
the first two terms of the sequence being 0 and 1. For example, the third Fibonacci number is
f1+f2=0+1=1, and the fourteenth Fiboncci term is f12+f13=89+144=233.
The Fibonacci sequence is typically written

fn=fn−1+fn−2
For Example
fast_fib(1) # returns 0
fast_fib(2) # returns 1
fast_fib(3) # returns 1
fast_fib(4) # returns 2
fast_fib(10) # returns 34

'''

def fast_fib(n):
    # write code below
    pass


'''
Pascal's Triangle is one of the most amazing objects in mathematics. Learn more about it here
. Essentially each term in a given row is calculated by summing the two terms in the row 
directly above it (for numbers on the edge of the triangle, there is an implicit 0).

Here are the first five rows of Pascal's Triangle:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
For example, the third row is calculated by doing 0 + 1 = 1, 1 + 1 = 2, and 1 + 0 = 1. This triangle can be represented as nested lists like so [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]] and so on.

Write a function called pascals_tri that will create Pascal's Triangle in a nested list like above. It should take in one parameter n, which will always be a value greater than or equal to 1, and represents the number of rows to find. It can be helpful to use combinations to find this triangle, learn more about combinations here  .

Examples
pascals_tri(1) # returns [[1]]
pascals_tri(2) # returns [[1], [1, 1]]

'''





'''
The next challenge builds upon the singly-linked-list challenge from last week,  so if you haven't already, go complete that challenge first!

For this week, add a shift method to the SLL class. The shift method should take in a single value and add it to the front of the singly-linked list.
'''




'''
March 22nd, 2021
'''


'''
Complete the compounding interest function below. This function takes in parameters prin, t, rate, and n. 
prin is the initial principle (or amount), t is the overall length of time the interest is applied, 
rate is the interest rate, and n is the frequency. The new principle is calculated by doing 
prin×(1+raten)n×t

This function should return the new principle given the parameters. 
Learn more about compounding interest here. 
'''

def comp_interest(P, t, rate, n):
    return P *(1 + (rate/n))**(n*t)

# print(comp_interest(1500, 6, .043, 4))  # 1938.8368221341054

'''
Assume you are programming a video game. A character needs to move around a board 
(that is filled with obstacles ) and return to the the same starting spot in exactly 10 moves.
It can be helpful to see if they entered a valid path that takes them from the start back 
around to the start. Complete the is_valid_walk function below. It takes in one parameter 
walk that is a list of directions ('n', 's', 'e', and 'w'). 
It will return True if it is a valid path, and False if it is not a valid path. 
A valid path is exactly 10 moves long, and they start and end in the same place on the board.
'''

def is_valid_walk(walk):
    dir = {'n': 1, 's': -1, 'e': 2, 'w': -2}

    count = []
    
    for el in walk:
        for x, y in dir.items():
            if el in x:
                count.append(y)
            
    return sum(count) == 0
    

# print(is_valid_walk(['n', 'n', 'e', 's', 'w', 's', 'w', 'n'])) # returns False

# print(is_valid_walk([ 's', 's', 'w', 's', 'n', 's', 'n', 'e', 'n', 's']) )# returns False

# print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])) # returns True




'''
Write a function called is_solved that takes in a a tic-tac-toe board as an input. 
The tic-tac-toe will be a list of three sub lists, where 
the first list is the first row, 
the second list is the second row, and 
the third list is the third row. 
It will look like this:
[[0, 0, 1],
 [2, 1, 2],
 [2, 2, 1]]
is_solved will check to see if "X"(represented by the 2) has won , 
"O"(represented by 1) has won, if there are moves left to be played 
(represented by 0's still being available on the board), or if its a
stale mate (neither "X" or "O" won and no more available spaces left). 
This function should return 2 if "X" won, return 1 if "O" won, 
return 0 if the board still has places to play, and -1 if the board is at a stale mate.
'''








'''
The next challenge builds upon the singly-linked-list challenge from the previous two weeks,  so if you haven't already, go complete that challenge first!
For this week, add a pop method to the SLL class. The pop method should remove the last node from the list and return the value of that node. Be careful, to fully remove the node from the list the nxt value in the previous node will need to be set back to None.
'''




'''
March 29th, 2021
'''

'''
The cartesian product of two sets A,B is the set of tuples containing every element from 
A paired with every element in B. For example, let A={a,b,c}, and B={1,2,3}. 
Then the cartesian product, denoted A×B, is the set of tuples

(a, 1)
(a, 2)
(a, 3)
(b, 1)
(b, 2)
(b, 3)
(c, 1)
(c, 2)
(c, 3)
Implement your own cartesian_product() function, which should take two lists and compute the
cartesian product. Your function should return a list of tuple pairs. If you are unfamiliar 
with Python's tuple type, you can read about it in this  unit.

Note: you may not import any packages!

'''



'''
The function ex can be approximated by the partial sum

ex≈∑k=0n−1xkk!
Where n is the number of terms to include in the partial sum. The higher the value n, the 
better the approximation.

Write a function which will calculate the value of ex given two parameters, x and n, where n 
is the number of terms to include in your summation.

Note: you may not import any packages!
'''
    
# def exp_approx(x, n):
#     e = 1.0
#     fact = 1.0
#     # stop condition
#     if (n == 0):
#         return 1
#     # recursion
#     r = exp_approx(x, n-1)
    
    
#     e = e * x
#     fact = fact * n
#     return (r + e / fact)   
    

    # for num in range(1, x + 1 ):
    #     fact *= num
    #     e +=  1/fact
    

# print(exp_approx(-1, 1)) # 1.0
# print(exp_approx(5, 1)) # 2.283333
# print(exp_approx(-1, 10))
# AssertionError: 1.0 != 0.36787944117144233 within 6 places



'''
Implement the function convert_time_format() which will convert an amount of time given in seconds to one given in years, days, hours, minutes, and seconds. The input type will be int and the output type should be str.
Notice that singular values are not pluralized!
'''
# def format_time(interval_name, interval):
#     if   interval % 60 == 0:
#         return ""
#     elif interval % 60 == 1:
#         return f"{interval % 60} {interval_name} " 
#     else:
#         return f"{interval % 60} {interval_name+'s'} "
# def convert_time_format(scnds):
#     minutes     = (scnds   // 60)
#     hours       = (minutes // 60)
#     days        = (hours // 24)
#     years       = (days    // 365)
#     scnds_str   = format_time("second", scnds)
#     minutes_str = format_time("minute", minutes)
#     hours_str   = format_time("hour"  , hours)
#     days_str    = format_time("day"   , days)
#     years_str   = format_time("year"  , years)
#     return (years_str + days_str + hours_str + minutes_str + scnds_str).strip()
# print( [convert_time_format(600)]        ) # 10 minutes
# print( [convert_time_format(51_234)]     ) # 14 hours, 13 minutes, 54 seconds
# print( [convert_time_format(3_661)]      ) # 1 hour, 1 minute, 1 second
# print( [convert_time_format(87_239_051)] ) # 2 years, 279 days, 17 hours, 4 minutes, 11 seconds

# def convert_time_format(seconds):
#     seconds = seconds % (31536000 * seconds)
#     years = seconds // (86400 * 365)
#     seconds = seconds % (86400 * 365)
#     days = seconds // (24 * 3600)
#     seconds = seconds % (24 * 3600) # 61451
#     hour = seconds // 3600 # 17
#     seconds %= 3600 # 251
#     minutes = seconds // 60 # 4
#     seconds %= 60 # 11
      
#     lst = [years, days, hour, minutes, seconds]
#     lst2 = ['year', 'day' , 'hour', 'minute', 'second']
#     acc = ''
#     for idx, ele in enumerate(lst):
#         if ele == 0:
#             acc += ''
#         elif ele == 1:
#             acc += f"{lst[idx]} {lst2[idx]}  "
#         else:
#             acc += f"{lst[idx]} {lst2[idx]+'s'}  "
    
#     return (acc.strip()).replace('  ', ', ')


# def convert_time_format(s: int) -> str:
#     result = []
#     remainder = s
#     conversions = {"year":    31536000,
#                    "day":     86400,
#                    "hour":    3600,
#                    "minute":  60,
#                    "second":  1}

#     for span, seconds in conversions.items():
#         num_of_span, remainder = divmod(remainder, seconds)
#         if num_of_span > 0:
#             word = f"{num_of_span} {span}"
#             if num_of_span > 1:
#                 word += "s"
#             result.append(word)

#     return ", ".join(result)

# for span, seconds in conversions.items():
#     num_of_span, remainder = divmod(remainder, seconds)
#     if num_of_span > 0:
#         result.append(f"{num_of_span} {span}" + "s"*bool(num_of_span - 1))

'''
A couple of weeks ago  one of the weekly challenges was to implement a Caesar cipher function.

We're going to take that challenge to the next level by implementing a CaesarCipher class. 
Your CaesarCipher class should support message encoding and message decoding, based on a shift 
value specified at instantiation. For example, a shift value of 13 will give you the classic 
ROT13 cipher: rot13 = CaesarCipher(13).

Feel free to add any other methods you feel may be necessary, but leave encode_message and 
decode_message intact (and be sure to implement them!). Your cipher should properly handle both 
upper- and lower-case alphabetic letters, and leave punctuation and other symbols intact. 
For example, for a cipher with a shift value of 23, the message "Hello, Caesar cipher!" should 
be encoded as "Ebiil, Zxbpxo zfmebo!".

Part of the motivation for creating a class instead of simply a function is that you can calculate
a translation table once and then be able to encode and decode many messages without needing to 
recalculate a translation table each time. (It's being heavily implied that you should use some sort
of mapping for your character translations, instead of the typical indexing technique shown in the 
weekly challenge from a few weeks ago!).

It may be beneficial to browse through the documentation on string methods. 

Note: you may not use the built-in str.encode()!
'''


class CaesarCipher:
    def __init__(self, shift):
        pass

    def encode_message(self, msg):
        pass

    def decode_message(self, msg):
        pass
    

'''
April 13th, 2021
'''
  
'''
  Implement the following formula:
∑ni=11i2
This formula is known as the Basel Problem, which states that the series of summed fraction can be used to
approximate π26. Complete the approximate function below that takes in a single term. The single
term, called n, is the upper inclusive bound for that approximation of π26. This function should return that approximation.
'''  
    
def approximate(n):
    pass



'''
The Fibonacci numbers are a sequence of numbers defined by the following relation:
F(n) = F(n - 1) + F(n - 2)

Or in plain english the current term is the sum of the previous to numbers. So the sequence goes 
like 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. Write the function called product_fib that takes in 
a number as a parameter and returns if that number is the result of multiplying two subsequent 
Fibonacci numbers together. For example, if the number was 40 it would return [5, 8, True] 
because 5 * 8 = 40. Note the style of the return where where it includes the two Fibonacci
numbers and whether they are equal to the product.
'''
def product_fib(number):
    pass
    
    
    
# print(product_fib(4895)) # returns [55, 89, True]
# print(product_fib(5895)) # returns [89, 144, False]    
    
    
'''  
This question builds off the Doubly Linked List(DLL) challenge from last week, if you haven't 
already go do those challenges here.  This week add a shift method that adds a node to the 
beginning of the DLL. The shift method should take in the value and add it the beginning of 
the DLL.  
'''    

def DLL():
    pass




'''
April 13th, 2021
'''

'''
Complete the function called pythag_checker. This function takes in three numbers and it should check if any combination of the three numbers is a correct pythagorean triple. To the Pythagorean Formula is:
a2+b2=h2
This function should return a string of the format "The pythagorean triple in this set is <a>, <b>, and <h>." where <a> is the smaller side, <b> is the larger side, and <h> is the hypothenuse. If there are no Pythagorean values return the string 'There are no pythagorean triples here!'. Learn more about the Pythagorean Theorem here. 
'''

def pythag_checker(num1, num2, num3):
    pass



'''

Some numbers have funny properties, for example:
89→81+92=89=89×1
695→62+93+54=1390=695×2
46288→43+64+25+86+87=46288×51
This is really the implementation of the following formula where a, b, c, d, and so on represent the digits of a number n, with p and k representing a positive integers:
ap+bp+1+cp+2+dp+3+...=n∗k
For this problem implement a function called dig_pow with two parameters n and p. n represents the initial number, p is the power to start raising the individual digits too. This function should return k the value that makes n * k equal to the summing of the digits raised to their powers. If there is no k that makes the formula true, this function should return -1.
Example's:
dig_pow(92, 1) # returns -1, because no k makes the formula True
dig_pow(46288, 3) # returns 51,
'''







'''
Write a function called mode_dict with one parameter that is a list of numbers. This function should create a dictionary with the count of how many times each item occurs in the dictionary.
For Example:
lst = [3, 1, 1, 1, 3, 2, 1]
mode_dict(lst) # should return {3: 2, 1: 4, 2: 1}
'''





'''
April 26th, 2021
'''

'''Complete the find_next_square function. This function takes in a single parameter call pfsq. This function should do the following:
If pfsq is not a perfect square the function should return -1
If pfsq is a perfect square this function should find the next perfect square and return it
Note:
A perfect square has the following property:
\( k = x^{2} \) or \( \sqrt{k} = x \) where x and k are integers.'''


# def find_next_square(pfsq):
#     # write code here


# print(find_next_square(9)) # should return 16
# print(find_next_square(121)) # should return 144
# print(find_next_square(8)) # should return -1
# print(find_next_square(13)) # should return -1


'''
If you have gone though all of our material you have seen the fibonacci sequence. This problem covers the lesser known tribonacci sequence. The tribonacci sequence is the sum of the three proceeding terms. Write a function called tribonacci that takes in two terms signature and n. signature will be a list of length three and represents the first three digits on the sequence, and n will be the total number of terms in the sequence that need to be returned. It should return the sequence calculated out to n.
'''



# tribonacci([0, 0, 1], 10) # should return [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
# tribonacci([1, 1, 1], 10) # should return [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
# tribonacci([1, 2, 3], 7) # should return [1, 2, 3, 6, 11, 20, 37]
# tribonacci([1, 2, 3], 1) # should return [1]
# tribonacci([1, 2, 3], 0) # should return []


'''Write a function called cakes. cakes will take in two dictionaries as parameters. The first one will be called recipe and its keys will be the ingredient and the value will be the amount of that ingredient required (for example it will look something like this {"eggs" : 2}). The second parameter available will be a dictionary of all available ingredients. This function should check the recipe against available and return the number of cakes that those available ingredients can make.'''






# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# cakes(recipe, available) # returns 2

# recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
# available = {"sugar": 500, "flour": 2000, "milk": 2000}
# cakes(recipe, available) # should return 0



'''
4 May
'''

'''
Write a function called mult_total that will take in two numbers as parameters. This function should 
return the result of multiplying all the numbers between the smaller number and the larger number 
together including the larger number. If the numbers are equal, it should return just that number.
'''
def mult_total(num1, num2):
    prod = 1
    
    if num1 == num2:
        return num1
    if num1 < num2:
        for i in range(num1, num2 + 1):
            prod *= i
        return prod
    else:
        for i in range(num2, num1 + 1):
            prod *= i
        return prod

# print(mult_total(1, 4)) # 24
# print(mult_total(4, 1)) # 24

def mult_total2(num1, num2):
    
    if num1 == num2:return num1
    prod =1
    for num in range((min(num1, num2), max(num1,num2)+1)):
        prod *= num
    return prod


# print(mult_total(1, 4)) # 24
# print(mult_total(4, 1)) # 24        


'''
Write a function called generate_hashtag. This function will take in a single string, called s, and 
will generate the hashtag version of that string. These hashtags have a few rules that they need to 
follow. 
First they must all begin with the '#' symbol. 
Second all the individual words must be capitalized. 
Third, if the generated hashtag contains just the '#' symbol or is more than 140 characters 
long it is not a valid hashtag and the function should return False, otherwise this function should return 
the generated hashtag.'''


from string import capwords

def generate_hashtag(s):
    hashtag = '#' + (capwords(s)).replace(' ', '')
    if len(hashtag) > 140 or s == '':
        return False
    return hashtag

    

# print( generate_hashtag("Codeing is fun") ) # returns '#CodingIsFun'
# print( generate_hashtag("Math is hard") ) # returns '#MathIsHard'
# print( generate_hashtag("") ) # returns False



'''
Write a function called spiral_unpack which will take in a single parameter called stacked. 
This function should flatten everything in stacked in a spiral pattern. T
his function should return a list of all the items in stacked returned in the correct spiral pattern. 
Note, you can assume all the sublists will have the same length.
'''
def spiral_unpack(stacked):
    pass

# def spiral_unpack(stacked):
#     i = 0
#     j = 0
#     lst = []
#     shift = (0, 1)
#     shifts_switch = {
#         (0, 1):  (1, 0),
#         (1, 0):  (0, -1),
#         (0, -1): (-1, 0),
#         (-1, 0): (0, 1)
#     }
#     for _ in range(len(stacked) * len(stacked[0])):
#         lst.append(stacked[i][j])
#         stacked[i][j] = None

#         if i + shift[0] == len(stacked) or j + shift[1] == len(stacked):
#             shift = shifts_switch[shift]
#         elif stacked[i + shift[0]][j + shift[1]] == None:
#             shift = shifts_switch[shift]
#         i += shift[0]
#         j += shift[1]
#     return lst

# lst = [[1, 2],
#        [4, 3]]
# print( spiral_unpack(lst) ) # returns [1, 2, 3, 4]

# lst = [[1, 2],
#        [3, 4]]
# print( spiral_unpack(lst) ) # returns [1, 2, 4, 3]

# lst = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]
# print( spiral_unpack(lst) ) # returns [1, 2, 3, 6, 9, 8, 7, 4, 5]



def fibonacci(n):
    """Returns the nth Fibonacci number, assuming the
    sequence starts at 0, 1.

    Parameters
    ----------
    n : int
        The index of the Fibonacci number to be calculated.

    Returns
    -------
    int
        The nth Fibonacci number.
    """
    if not n:
        return 0

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b

    return b



'''
10 May
'''

'''
Complete the one_odd_one_even function below. This function takes in two numbers and should return 
True if one number is odd and one number is even. This function should return False otherwise. 
Note that the numbers can be in any order, so the first number could be odd or even, and the 
second number could be odd or even.
'''

def one_odd_one_even(num1, num2):
    return (num1 + num2)%2 != 0

# print(one_odd_one_even(1,3))
# print(one_odd_one_even(2,6))
# print(one_odd_one_even(4,3))

'''
Write a function named fisrt_non_repeating_letter that takes a string input, 
and returns the first character that is not repeated in the string. 
Note that upper and lower case letters are considered the same character, 
but the function should return the proper case for the letter. 
For example the word "sTreSS" should return "T", which is the proper case for the first non repeated letter. 
If there are no non-repeated letter, this function should return "", an empty string.
'''
def first_non_repeating_letter(meow):
    comp = []
    for i in meow:
        comp.append(i.lower())
    for i in meow:
        if comp.count(i.lower()) == 1:
            return i
    return " "

# print(first_non_repeating_letter('sTreSS'))
# print(first_non_repeating_letter('sSttoo'))    

'''
Write a function called cut_the_ropes which takes in a list of integers representing the length of the ropes. 
At each step the shortest rope must be removed and the other ropes must be reduced by that much. 
This function should return a list that represents the number of ropes before each reduction.

For Example
cut_the_ropes([[3, 3, 2, 9, 7]]) # returns [5, 4, 2, 1]
The steps would be:

Append 5 because there are 5 ropes left, then reduce all by 2, resulting in [1, 1, 0, 7, 5]
Append 4 because there are 4 ropes left, then reduce remaining ropes by 1, resulting in [0, 0, 0, 6, 4]
Append 2 because there are 2 ropes left, then reduce remaining ropes by 4, resulting in [0, 0, 0, 2, 0]
Append 1 because there is 1 rope left, then reduce all remaining ropes by 1, resulting in [0, 0, 0, 0, 0]
Stop and return because there are no more ropes left to reduce
Note: That there are clever solutions if you think about what is going on and exactly what should be returned.
'''

def cut_the_ropes(lst):
    ropes = []
    n = len(lst)

    ropes.append(len(lst))

    lst.sort()
    cuttingLength = lst[0]

    for i in range(1, n):
        if (lst[i] - cuttingLength > 0):
            ropes.append(n - i)
            cuttingLength = lst[i]
            
    return ropes


# print( cut_the_ropes([3, 3, 2, 9, 7]) ) # returns [5, 4, 2, 1])



















