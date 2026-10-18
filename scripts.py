# =========================
# Problem 1.
# =========================

# --- Say "Hello, World!" ---
if __name__ == '__main__':
    print("Hello, World!")

#--- Python If-Else ---
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n %2 !=0:
        print("Weird")
    elif n in range(1,6):
            print("Not Weird")
    elif n in range(5,21):
            print("Weird")
    elif n>=20:
            print("Not Weird")
        

# --- Arithmetic Operators ---
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum_ = a+b
    dif = a-b
    prod = a*b
    print(sum_)
    print(dif)
    print(prod)

# --- Python: Division ---
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum_ = a+b
    dif = a-b
    prod = a*b
    print(sum_)
    print(dif)
    print(prod)

# --- Loops ---
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**2)

# --- Write a function ---
def is_leap(year):
    leap = False
    if year %4 ==0:
        if year %100==0:
            if year%400==0:
                leap= True
        else:
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))

# --- Print Function ---
if __name__ == '__main__':
    n = int(input())
    print(*range(1,n+1),sep ="")


# --- List Comprehensions ---
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    coordinates = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
    
    print(coordinates)

# --- Find the Runner-Up Score! ---
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    first = second = float('-inf')
    
    for i in arr:
        if i>first:
            second = first
            first = i
        elif i>second and i != first:
            second = i
            
    if second !=float('-inf'):
        print(second)
    else:
        print("No runner up")

# --- Nested Lists ---
if __name__ == '__main__':
    
    records =[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append(
            [name,score]
        )
    
    scores = [r[1] for r in records]
    min = scores[0]
    second = float('inf')
    for i in scores:
        if i<min:
            second = min
            min = i
        elif i<second and i !=min:
            second = i 
        
    names = [r[0] for r in records if r[1]== second]
    names = sorted(names)
    for _ in names:
        print(_)

# --- Finding the percentage ---
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    score = student_marks[query_name]
    sum_ = 0
    for _ in range(len(scores)):
        sum_ += score[_]
        
    aver = sum_/len(scores) 
    
    #print(aver) 
    #how i originally had it, but the output gave me "wrong answer", due to decimals, so i used an LLM to explain why i got the wrong answer and how to correct it.
    
    print(f"{aver:.2f}")

# --- Lists ---
if __name__ == '__main__':
    N = int(input())
    arr=[]
    
    for _ in range(N):
        line = input().split()
        if line[0] == "insert":
            arr.insert(int(line[1]),int(line[2]))
        elif line[0] == "print":
            print(arr)
        elif line[0] == "remove":
            arr.remove(int(line[1]))
        elif line[0] == "append":
            arr.append(int(line[1]))
        elif line[0] =="sort":
            arr.sort()
        elif line[0] == "pop":
            arr.pop()
        elif line[0] == "reverse":
            arr.reverse()

# --- Tuples ---
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t))

# --- sWAP cASE ---
def swap_case(s):
    swap = []
    
    for i in s:
        if i.isupper():
            swap.append(i.lower())
        elif i.islower():
            swap.append(i.upper())
        else:
            swap.append(i)
    return "".join(swap)
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# --- String Split and Join ---
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# --- What's Your Name? ---
def print_full_name(first, last):
    text= f"Hello {first} {last}! You just delved into python."
    print(text)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# --- Mutations ---
def mutate_string(string, position, character):
    l = list(string)
    l[position]=character
    string = "".join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# --- Find a string ---
def count_substring(string, sub_string):
    num =0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            num += 1

    return num

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# --- String Validators ---
if __name__ == '__main__':
    s = input()
    for i in s:
        if i.isalnum():
            print("True")
            break
    else :
        print("False")

    for i in s:
        if i.isalpha():
            print("True")
            break
    else :
        print("False")
    
    for i in s:
        if i.isdigit():
            print("True")
            break
    else :
        print("False")
        
    for i in s:
        if i.islower():
            print("True")
            break
    else :
        print("False")
    
    for i in s:
        if i.isupper():
            print("True")
            break
    else :
        print("False")
        
        
# --- Text Alignment ---
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# --- Text Wrap ---
import textwrap

def wrap(string, max_width):
    split = textwrap.wrap(string,max_width)
    split ="\n".join(split)
    return split

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# --- Designer Door Mat ---
# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())
l = "-"

for i in range((N - 1) // 2):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(M, "-"))

pattern2 = "WELCOME"
print(pattern2.center(M,"-"))

for j in range((N-1)//2 -1,-1,-1):
    pattern3 = ".|." * (2 * j + 1)
    print(pattern3.center(M,"-"))
    
# --- String Formatting ---
def print_formatted(number):
   for i in range(1,number+1):
    width = len(f"{number:b}") 
    print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# --- Alphabet Rangoli ---
def print_rangoli(size):
    rows = list(range(size)) + list(range(size-2, -1, -1))
    for i in rows:
        letters_up = []

        for j in range(size-1,size-1-i-1,-1):
            char = chr(ord("a")+j)
            letters_up.append(char)
        letters_up += letters_up[-2::-1]
        pattern = "-".join(letters_up)
        print(pattern.center(4*(size-1)+1,"-"))
        


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# --- Capitalize! ---
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    full_name = []
    for word in s.split(" "):
        if word: 
            word = word[0].upper() + word[1:]
        full_name.append(word)
    return " ".join(full_name)
        

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# --- The Minion Game ---
def minion_game(string):
    kevin = 0
    stuart = 0 
    vowels = "AEIOU"
    
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
            
    if kevin>stuart:
        print(f"Kevin {kevin}")
    elif stuart>kevin:
        print(f"Stuart {stuart}")
    else:
        print("Draw")
    

        

if __name__ == '__main__':
    s = input()
    minion_game(s)

# --- Merge the Tools ---
def merge_the_tools(string, k):
    #n = len(string)/k
    for i in range(0,len(string),k):
        t= string[i:k+i]
        u=[]
        for j in t:
            if j not in u:
                u.append(j)
        print("".join(u)) 

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# --- collections.Counter() ---
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X=int(input()) #number of shoes
shoes = list(map(int, input().split())) 
N =int(input()) #number of costumers

stock = Counter(shoes)
money = 0

for _ in range(N):
    size, price = map(int, input().split())
    
    if stock[size]>0:
        money += price
        stock[size] -= 1
        
print(money)

# --- DefaultDict Tutorial ---
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())

A = []
for _ in range(n):
    A.append(input())

B = []
for _ in range(m):
    B.append(input())


for i in range(m):
    positions =[]
    for j in range(n):
        if B[i] == A[j]:
            positions.append(j+1)
            
    if positions:
        print(" ".join(map(str, positions)))
    else:
        print(-1)

# --- Introduction to Sets ---
def average(array):
    sm = 0
    for i in set(array):
        sm += i
    avr = sm/len(set(array))
    return avr
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# --- Symmetric Difference ---
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set_a = set(map(int, input().split()))
m = int(input())
set_b = set(map(int, input().split()))

inter = set_a.intersection(set_b)
un = set_a.union(set_b)

dif = un.difference(inter)

print(*sorted(dif),sep='\n')

# --- No Idea! ---
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happy = 0

for i in arr:
    if i in a:
        happy+=1
    elif i in b:
        happy-= 1
        
print(happy)
    
# --- Set .add() ---
N = int(input())
stamps = [input() for _ in range(N)]

dist = set()
for i in range(N):
    dist.add(stamps[i])
    
print(len(dist))

# --- Set .discard(), .remove() & .pop() ---
n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())
for _ in range(num_commands):
    command = input().split()
    if command[0] == "pop":
        s.pop()
    elif command[0] == "discard":
        s.discard(int(command[1]))
    elif command[0] == "remove":
        s.remove(int(command[1]))
        
sum = 0

for i in s:
    sum += i
    
print(sum)

# --- Set .union() Operation ---
n = int(input()) #english newspaper
english = set(map(int, input().split()))
b = int(input()) #french newspaper
french = set(map(int,input().split()))

count = english.union(french)
#print(count)
            
print(len(count))

# --- Set .intersection() Operation ---
n = int(input())
english = set(map(int,input().split()))
b = int(input())
french = set(map(int,input().split()))

count = english.intersection(french)
print(len(count))

# --- Set .difference() Operation ---
n = int(input())
english = set(map(int, input().split()))
m = int(input())
french = set(map(int, input().split()))

dif = english.difference(french)

print(len(dif))

# --- Set .symmetric_difference() Operation ---
n = int(input())
english = set(map(int, input().split()))
m = int(input())
french = set(map(int, input().split()))

dif = english.difference(french)

print(len(dif))

# --- Set Mutations ---
# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input()) #number of elements in A
A = set(map(int, input().split())) #set A
N =int(input()) #number of other sets
for _ in range(N):
    op, length = input().split() #operation and length of other set
    other = set(map(int, input().split())) #elements of other set
    if op == "update":
        A.update(other)
    elif op == "intersection_update":
        A.intersection_update(other)
    elif op == "difference_update":
        A.difference_update(other)  
    elif op == "symmetric_difference_update":
        A.symmetric_difference_update(other)
        
sum = 0
for i in A:
    sum += i
    
print(sum)

# --- The Captain's Room ---
# Enter your code here. Read input from STDIN. Print output to STDOUT

K = int(input()) #size of each group
rooms = list(map(int,input().split()))

st = set(rooms)

dif = K*sum(st)-sum(rooms)

captain = dif // (K-1)

print(captain)


# --- Check Subset ---
# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
for _ in range(T):
    n = int(input()) #number of elements in A
    A = set(map(int, input().split())) #elements of A
    m = int(input()) # number of elements in B
    B = set(map(int, input().split()))
    
    inter = A.intersection(B)
    
    if inter == A:
        print("True")
    else:
        print("False")
    
    
# --- Check Strict Superset ---

A = set(map(int,input().split()))
n = int(input())

result = True

for _ in range(n):
    other = set(map(int,input().split()))
    if not A> other:
        result = False
        break

print(result)

# --- Collections.namedtuple()---
from collections import namedtuple

N = int(input()) #number of students
columns = input().split()    
Student = namedtuple("Student", columns)
total = 0
for _ in range(N):
    s = Student(*input().split())
    mark = float(s.MARKS)
    total +=mark
aver = total/N 
print(aver)

# --- Collections.OrderedDict() ---
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

N=int(input())
groceries = OrderedDict()
for _ in range(N):
    name, price = input().rsplit(' ', 1)
    price = int(price)
    
    if name in groceries:
        groceries[name] += price
    else:
        groceries[name] = price
    
total = 0

for n,p in groceries.items():
    print(n,p)
    
# --- Word Order ---
from collections import OrderedDict

n = int(input())

distinct = OrderedDict()
for _ in range(n):
    words = input()
    if words in distinct:
        distinct[words]+=1
    else:
        distinct[words]=1

print(len(distinct))
print(*distinct.values())
    
# --- Collections.deque() ---
from collections import deque

N = int(input())
d = deque()
for _ in range(N):
    command = input().split()
    
    if command[0]== "append":
        d.append(command[1])
        
    if command[0]== "pop":
        d.pop()
        
    if command[0]== "popleft":
        d.popleft()
        
    if command[0]== "appendleft":
        d.appendleft(command[1])
        
print(*d)

# --- Company Logo ---
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()


d= {}
for i in s:
    if i in d:
        d[i] +=1
    else:
        d[i]=1
        
sorted_d = sorted(d.items(), key=lambda x: (-x[1], x[0]))

for c,n in sorted_d[:3]:
    print(c,n)
        

# --- Piling Up! ---

T = int(input()) #number of test cases
for _ in range(T):
    n = int(input())
    cube= list(map(int,input().split()))
    
    left = 0
    right = n - 1
    top = float('inf')
    result = "Yes"
    while left <= right:
        l = cube[left]
        r = cube[right]
        
        if l<= top and r <= top:
            if l<r:
                top = r
                right-=1
            else: 
                top = l
                left+=1
        elif l<= top:
            top = l 
            left+=1
        elif r<= top:
            top = r 
            right-=1
        else:
            result = "No"
            break   
            
            
    print(result)

# --- Calendar Module ---
import calendar 

month, day, year = map(int,input().split())
day = calendar.weekday(year,month,day)
print(calendar.day_name[day].upper())

# --- Time Delta ---
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    d1 = datetime.strptime(t1, fmt)
    d2 = datetime.strptime(t2, fmt)
    return str(int(abs((d1 - d2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
    
    
    from datetime import datetime

# --- Exceptions ---
T = int(input())
for _ in range(T):
    a, b = input().split()

    try:
        print( int(a)//int(b) )
    except ZeroDivisionError as e:
        print ("Error Code:",e)
    except ValueError as v:
        print ("Error Code:",v)

# --- Incorrect Regex ---
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(raw_input())
for _ in range(T):
    s = raw_input()
    try:
        re.compile(s)
        print("True")
    except re.error:
        print("False")

# --- Zipped! ---

N,X =map(int,input().split())

marks = []
for _ in range(X):
    grade = list(map(float,input().split()))
    marks.append(grade)
    
for student in zip(*marks):
    sm = 0
    for i in student:
        sm+=i
    aver = sm/X
    print(f"{aver:.1f}")

# --- Athlete Sort ---
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    k = int(input().strip())
    
    
    result = sorted(arr, key=lambda row: row[k])
    for i in result:
        print(*i)

# --- ginortS ---
# Enter your code here. Read input from STDIN. Print output to STDOUT

S = input()

lowers = sorted([s for s in S if s.islower()])
uppers = sorted([s for s in S if s.isupper()])
odd = sorted([s for s in S if s.isdigit() and int(s)%2!=0])
even = sorted([s for s in S if s.isdigit() and int(s)%2==0])



print("".join(lowers + uppers + odd + even))

# --- Map and Lambda Function ---

cube = lambda x: x**3

F0=0
F1=1
def fibonacci(n):
    if n>=2:
        F = [F0,F1]
        for i in range(2,n):
            Fi = F[i-1]+F[i-2]
            F.append(Fi)
    elif n ==1:
        F=[F0]
    else:
        F=[]
    return F
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# --- XML 1 - Find the Score ---
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    atr = 0
    for i in node.iter():
        atr +=len(i.attrib)
    return  atr    

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

# --- XML2 - Find the Maximum Depth ---
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level +=1
    if level>maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level )
        
    return maxdepth
    
    
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

# --- Standardize Mobile Number Using Decorators ---
def wrapper(f):
    def fun(l):
        mobiles = []
        for i in l:
            phone = i[-10:]
            formatted = f"+91 {phone[:5]} {phone[5:]}"
            mobiles.append(formatted)
        for j in sorted(mobiles):
            print(j)       
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

# --- Decorators 2 - Name Directory ---
import operator

def person_lister(f):
    def inner(people):
        people = sorted(people, key = lambda x: int(x[2]))
        return [f(person) for person in people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

# --- Detect Floating Point Number ---
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r'^[-+]?\d*\.\d+$'

for _ in range(int(input())):
    print(bool(re.match(pattern, input())))

# --- Re.split() ---

regex_pattern = r"[,.]"# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

# --- Group(), Groups() & Groupdict() ---
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

m = re.search(r'([A-Za-z0-9])\1', input())
print(m.group(1) if m else -1)

# --- Re.findall() & Re.finditer() ---
import re

v = "AEIOUaeiou"
c = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"

m = re.findall(r'(?<=[' + c + r'])([' + v + r']{2,})(?=[' + c + r'])', input())
print('\n'.join(m or ['-1']))

# --- Re.start() & Re.end() ---
import re
s = input()
k = input()

matches = list(re.finditer(r'(?=(' + re.escape(k) + r'))', s))

if matches:
    for m in matches:
        print((m.start(1), m.start(1) + len(k) - 1))
else:
    print((-1, -1))

# --- Regex Substitution ---
import re

n = int(input())
for _ in range(n):
    line = input()
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
    print(line)

# --- Validating Roman Numerals ---
regex_pattern = r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))

# --- Validating phone numbers ---
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    print("YES" if re.match(r'^[789]\d{9}$', input()) else "NO")

# --- Validating and Parsing Email Addresses ---
import re
import email.utils

pattern = r'^[A-Za-z][A-Za-z0-9._-]+@[A-Za-z]+\.[A-Za-z]{1,3}$'

for _ in range(int(input())):
    line = input()
    name, addr = email.utils.parseaddr(line)
    if re.match(pattern, addr):
        print(email.utils.formataddr((name, addr)))

# --- Hex Color Code ---

import re

n = int(input())
inside = False

for _ in range(n):
    line = input()
    if '{' in line:
        inside = True
    elif '}' in line:
        inside = False
    elif inside:
        for code in re.findall(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?', line):
            print(code)

# --- HTML Parser - Part 1 ---
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for name, value in attrs:
            print("->", name, ">", value)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for name, value in attrs:
            print("->", name, ">", value)

parser = MyHTMLParser()
parser.feed("".join(input() for _ in range(int(input()))))

# --- HTML Parser - Part 2 ---

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)

parser = MyHTMLParser()
parser.feed("".join(input() + "\n" for _ in range(int(input()))))

# --- Detect HTML Tags, Attributes and Attribute Values ---
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print("->", name, ">", value)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print("->", name, ">", value)

parser = MyHTMLParser()
parser.feed("".join(input() + "\n" for _ in range(int(input()))))

# --- Validating UID ---
import re

for _ in range(int(input())):
    uid = input().strip()
    valid = (
        len(uid) == 10
        and uid.isalnum()
        and len(set(uid)) == 10
        and len(re.findall(r'[A-Z]', uid)) >= 2
        and len(re.findall(r'\d', uid)) >= 3
    )
    print("Valid" if valid else "Invalid")

# --- Validating Credit Card Numbers ---
import re

pattern = r'^[456]\d{3}(-?\d{4}){3}$'

for _ in range(int(input())):
    card = input().strip()
    if re.match(pattern, card) and not re.search(r'(\d)(-?\1){3}', card):
        print("Valid")
    else:
        print("Invalid")

# --- Validating Postal Codes ---
regex_integer_in_range = r"^[1-9]\d{5}$"    # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"    # Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# --- Matrix Script ---
#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
    
decoded = "".join("".join(column) for column in zip(*matrix))
print(re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', decoded))

# --- Arrays ---
import numpy

def arrays(arr):
    return numpy.array(arr[::-1], float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# --- Shape and Reshape ---
import numpy
print(numpy.array(input().split(), int).reshape(3, 3))

# --- Transpose and Flatten ---
import numpy
n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
print(a.transpose())
print(a.flatten())

# --- Concatenate ---

import numpy
n, m, p = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(m)], int)
print(numpy.concatenate((a, b), axis=0))


# --- Zeros and Ones ---
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
dims = tuple(map(int, input().split()))
print(numpy.zeros(dims, dtype=int))
print(numpy.ones(dims, dtype=int))

# --- Eye and Identity ---
import numpy
numpy.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
print(numpy.eye(n, m))

# --- Array Mathematics ---
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(a + b, a - b, a * b, a // b, a % b, a ** b, sep='\n')

# --- Floor, Ceil and Rint ---

import numpy
numpy.set_printoptions(legacy='1.13')
a = numpy.array(input().split(), float)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


# --- Sum and Prod ---
import numpy
n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
print(numpy.prod(numpy.sum(a, axis=0)))

# --- Min and Max ---
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
print(numpy.max(numpy.min(a, axis=1)))

# --- Mean, Var, and Std ---
import numpy

n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)

print(numpy.mean(a, axis=1))
print(numpy.var(a, axis=0))
print(round(numpy.std(a, axis=None), 11))

# --- Dot and Cross ---
import numpy
n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))

# --- Inner and Outer ---
import numpy
a = numpy.array(input().split(), int)
b = numpy.array(input().split(), int)
print(numpy.inner(a, b))
print(numpy.outer(a, b))


# --- Polynomials ---
import numpy
p = list(map(float, input().split()))
x = float(input())
print(numpy.polyval(p, x))

# --- Linear Algebra ---
import numpy
n = int(input())
a = numpy.array([input().split() for _ in range(n)], float)
print(round(numpy.linalg.det(a), 2))



# =========================
# Problem 2.
# =========================

# --- Birthday Cake Candles ---
#!/bin/python3

import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):
    tallest = max(candles)
    return candles.count(tallest)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

# --- Number Line Jumps ---
#!/bin/python3

import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return "YES" if x1 == x2 else "NO"
    return "YES" if (x2 - x1) % (v1 - v2) == 0 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# --- Viral Advertising ---
#!/bin/python3

import math
import os
import random
import re
import sys



def viralAdvertising(n):
    shared, cumulative = 5, 0
    for _ in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# --- Recursive Digit Sum ---
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    total = sum(int(d) for d in n) * k
    while total > 9:
        total = sum(int(d) for d in str(total))
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

# --- Insertion Sort - Part 1 ---
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    value = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = value
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# --- Insertion Sort - Part 2 ---
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1, n):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)



    
