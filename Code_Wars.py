


def comp(array1, array2):
    pass
	
        # a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        # a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        # test.assert_equals(comp(a1, a2), True)
        # a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        # a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        # test.assert_equals(comp(a1, a2), False)
        # a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        # a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
        # test.assert_equals(comp(a1, a2), False)
        


# def to_float_array(arr):
    
#     return [float(el) if '.' in el else int(el) for el in arr ]    

# print(to_float_array(["1.1", "2.2", "3.3"])) #[1.1, 2.2, 3.3])
# print(to_float_array(["1", "2", "3"]))  #[1, 2, 3]

# def converter(mpg):
#     ltr = 4.54609188 
#     km = 1.609344
#     return round(mpg / (ltr/km), 2)
#     #your code here
    
# print(converter(12))# 4.25)
# print(converter(24))# 8.50)
# print(converter(36))# 12.74)

# def nb_year(p0, percent, aug, p):#needs work 26 May fixed
#     pop = p0
#     count = 0
    
    
#     while pop <= p:
#         pop = (p0 + (p0 * (percent/100)) + aug)
#         count += 1 
#         p0 = pop
    
        
#     return count
    
        
       
 

# print(nb_year(1500, 5, 100, 5000))#15)
# print(nb_year(1500000, 2.5, 10000, 2000000))#10)
# print(nb_year(1500000, 0.25, 1000, 2000000))#94)
        

# At the end of the first year there will be: 
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants

# At the end of the 2nd year there will be: 
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213

# It will need 3 entire years.

# reel1 = ["Wild", "Star", "Bell", "Shell", "Seven", "Cherry", "Bar", "King", "Queen", "Jack"]
# reel2 = ["Bar", "Wild", "Queen", "Bell", "King", "Seven", "Cherry", "Jack", "Star", "Shell"]
# reel3 = ["Bell", "King", "Wild", "Bar", "Seven", "Jack", "Shell", "Cherry", "Queen", "Star"]
# spin = [5, 4, 3]

'''
1. There are always exactly three reels

2. Each reel has 10 different items.

3. The three reel inputs may be different.

4. The spin array represents the index of where the reels finish.

5. The three spin inputs may be different

6. Three of the same is worth more than two of the same

7. Two of the same plus one "Wild" is double the score.

8. No matching items returns 0.


Item
Three of the same
Two of the same
Two of the same plus one Wild
Wild
100
10
N/A
Star
90
9
18
Bell
80
8
16
Shell
70
7
14
Seven
60
6
12
Cherry
50
5
10
Bar
40
4
8
King
30
3
6
Queen
20
2
4
Jack
10
1
2
'''
# def fruit(reels, spin):
#     landed = []
#     for pick in reels:
#         landed.append(reels[0], [(spin[0])])
#         landed.append(reels[1], [(spin[1])])
#         landed.append(reels[2], [(spin[2])])      
        
#     return landed

# print(fruit( [reel1, reel2, reel3], [5,4,3] )) #, 0))
    







    # reel = ["Wild", "Star", "Bell", "Shell", "Seven", "Cherry", "Bar", "King", "Queen", "Jack"]
    # spin = [0, 0, 0]
    # check(([reel, reel, reel], spin), 100)

    # reel1 = ["Wild", "Star", "Bell", "Shell", "Seven", "Cherry", "Bar", "King", "Queen", "Jack"]
    # reel2 = ["Bar", "Wild", "Queen", "Bell", "King", "Seven", "Cherry", "Jack", "Star", "Shell"]
    # reel3 = ["Bell", "King", "Wild", "Bar", "Seven", "Jack", "Shell", "Cherry", "Queen", "Star"]
    # spin = [5, 4, 3]
    # check(([reel1, reel2, reel3], spin), 0)

    # reel1 = ["King", "Cherry", "Bar", "Jack", "Seven", "Queen", "Star", "Shell", "Bell", "Wild"]
    # reel2 = ["Bell", "Seven", "Jack", "Queen", "Bar", "Star", "Shell", "Wild", "Cherry", "King"]
    # reel3 = ["Wild", "King", "Queen", "Seven", "Star", "Bar", "Shell", "Cherry", "Jack", "Bell"]
    # spin = [0, 0, 1]
    # check(([reel1, reel2, reel3], spin), 3)

    # reel1 = ["King", "Jack", "Wild", "Bell", "Star", "Seven", "Queen", "Cherry", "Shell", "Bar"]
    # reel2 = ["Star", "Bar", "Jack", "Seven", "Queen", "Wild", "King", "Bell", "Cherry", "Shell"]
    # reel3 = ["King", "Bell", "Jack", "Shell", "Star", "Cherry", "Queen", "Bar", "Wild", "Seven"]
    # spin = [0, 5, 0]
    # check(([reel1, reel2, reel3], spin), 6)

def over_the_road(address, n):
  return (n * 2) +1 - address

# print(over_the_road(1, 3))   # 6)
# print(over_the_road(3, 3))   # 4)
# print(over_the_road(2, 3))   # 5)
# print(over_the_road(3, 5))   # 8)
# print(over_the_road(7, 11))  # 16)
# print(over_the_road(23633656673, 310027696726)) # 596421736780)


import re 
from string import ascii_lowercase
def alph_score(word): # 26 May should be good
    d = {let: int(index) for index, let in enumerate(ascii_lowercase, start=1)}
    
    score = 0
    for letter in word:
        score += d[letter]
        
    return score

def solve(s):   
    trimmed = re.split('a|e|i|o|u', s)
    scores = [alph_score(word) for word in trimmed]
    
    return max(scores)

# print(solve("zodiac"))           #26)
# print(solve("chruschtschov"))    #80)
# print(solve("khrushchev"))       #38)
# print(solve("strength"))         #57)
# print(solve("catchphrase"))      #73)
# print(solve("twelfthstreet"))    #103)
# print(solve("mischtschenkoana")) #80)



'''
You throw a ball vertically upwards with an initial speed v (in km per hour). 
The height h of the ball at each time t is given by h = v*t - 0.5*g*t*t 
where g is Earth's gravity (g ~ 9.81 m/s**2). 
A device is recording at every tenth of second the height of the ball. 
For example with v = 15 km/h the device gets 
something of the following form: (0, 0.0), (1, 0.367...), (2, 0.637...), 
(3, 0.808...), (4, 0.881..)... where the first 
number is the time in tenth of second and the second number the height in meter.

Task
Write a function max_ball with parameter v (in km per hour) that returns the time 
in tenth of second of the maximum height recorded by the device.

Examples:
max_ball(15) should return 4

max_ball(25) should return 7

Notes
Remember to convert the velocity from km/h to m/s or from m/s in km/h when necessary.
The maximum height recorded by the device is not necessarily the maximum height reached by the ball.
'''


# print(max_ball(37))#  10)
# print(max_ball(45))#  13)
# print(max_ball(99))#  28)
# print(max_ball(85))#  24)


'''
In 1978 the British Medical Journal reported on an outbreak of influenza at a 
British boarding school. There were 1000 students. The outbreak began with one 
infected student.
We want to study the spread of the disease through the population of this school.
The total population may be divided into three: the infected (i), those who have 
recovered (r), and those who are still susceptible (s) to get the disease.

We will study the disease on a period of tm days. One model of propagation 
uses 3 differential equations:

(1) s'(t) = -b * s(t) * i(t)
(2) i'(t) =  b * s(t) * i(t) - a * i(t)
(3) r'(t) =  a * i(t)

where s(t), i(t), r(t) are the susceptible, infected, recovered at time t and s'(t),
i'(t), r'(t) the corresponding derivatives. b and a are constants: b is representing
a number of contacts which can spread the disease and a is a fraction of the 
infected that will recover.





'''






'''    
The function 'fibonacci' should return an array of fibonacci numbers. 
The function takes a number as an argument to decide how many no. of elements 
to produce. If the argument is less than or equal to 0 then return empty array
'''


def fibonacci(n):
    seq = []
    for num in range(n):
   
        if num <= 1: 
            seq.append(num)

        else:
            seq.append(fibonacci(num-1) + fibonacci(num-2))
    return seq
        

# print(fibonacci(4))# [0, 1, 1, 2], 'Should work for 4.')
# print(fibonacci(1))# [0], 'Should work for 1 element.')
# print(fibonacci(0))# [], 'Should have 0 elements for 0.')
# print(fibonacci(-1))# [], 'Should have 0 elements for negative input.')
# print(fibonacci(-14))# [], 'Should have 0 elements for negative input.')
# print(fibonacci(10))# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 'Should work for 10.')

# def fib(n:'upto n number')->int:
#     l=[0,1]
#     if n==0:
#         return l[0]
#     elif n==1:
#         return l
#     a=0
#     b=1
#     for i in range(0,n-1):
#         b=a+b
#         a=b-a
#         l.append(b)
#     return l

'''
Your task is to write a regular expression (regex) that will match a string only 
if it contains at least one valid date, in the format [mm-dd] (that is, a 
two-digit month, followed by a dash, followed by a two-digit date, surrounded by 
square brackets).

You should assume the year in question is not a leap year. Therefore, the number 
of days each month should have are as follows:

1. January - 31 days
2. February - 28 days (leap years are ignored)
3. March - 31 days
4. April - 30 days
5. May - 31 days
6. June - 30 days
7. July - 31 days
8. August - 31 days
9. September - 30 days
10. October - 31 days
11. November - 30 days
12. December - 31 days
All text outside a valid date can be ignored, including other invalid dates.

'''
def valid_date(regex):
    pass

# print(valid_date("[01-23]" )) #January 23rd is a valid date
# print(valid_date("[02-31]" )) #February 31st is an invalid date
# print(valid_date("[02-16]" )) #valid
# print(valid_date("[ 6-03]" )) #invalid format
# print(valid_date("ignored [08-11] ignored")) #valid
# print(valid_date("[3] [12-04] [09-tenth]" )) #December 4th is a valid date
# print(valid_date("[[[08-29]]]")) #"valid")
# print(valid_date("[13-02]"))     #"invalid format")
# print(valid_date("[02-[08-11]04]"))  #"valid")


def validate_pin(pin):
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)






# "_1234567890abcdefghijklmnopqrstuvwxyz":





