# Numeric expressions
2019
2000 + 19
0 * 1 * 2 + 3 + 4 * ((5 // 6) + 7 * 8 * 9)

# Call expressions
max(3, 4.5)
pow(100, 2)
pow(2, 100)
max(1, -2, 3, -4)
max(pow(10, 2), pow(2, 10), 1010)

# Importing and arithmetic with call expressions
from operator import add, mul#wooww....hai yao input first
add(1, 2)
mul(4, 6)
mul(add(4, mul(4, 6)), add(3, 5))
add(2, mul(9, mul(add(4, mul(4, 6)), add(3, 5))))#2018

# Objects
# Note: Download from http://composingprograms.com/shakespeare.txt
shakes = open('shakespeare.txt')
text = shakes.read().split()#read and split into individual word
len(text)# how many of the words
text[:25]#first 25 of the words
text.count('the')
text.count('thou')
text.count('you')
text.count('forsooth')
text.count(',')
text.count(',')/len(text)

# Sets
words = set(text)
len(words)#how many unique words, interpretation
max(words)
max(words, key=len)

# Reversals
'draw'[::-1]#prints "ward"
{w for w in words if w == w[::-1] and len(w)>4}#redder, minim,level,refer,madam...
{w for w in words if w[::-1] in words and len(w) == 4}#teem, meet, meed,deem, 
                                                      #of course, "star","leer"
                                                      #it does not shows in this sequence, it si more random display
{w for w in words if w[::-1] in words and len(w) > 6}#drawer, diaper
