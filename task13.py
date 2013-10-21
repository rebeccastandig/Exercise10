import math 
def rounding(inp):
    base = int(inp)
    if inp - base >= 0.5:
        print base+1
        # rounds up
    else:
        print base
        # rounds down
    
def count_by_line_break(inp):
    if not inp:
        print 0
    num = 1
    for c in inp:
        if c == "\n":
           num  += 1    
    print num

def pythagorean_theorem(a, b):
    c = a * a + b * b
    print math.sqrt(c)
    

def reverse_list(inp):
    size = len(inp)
    for i in range(len(inp)/2):
        temp = inp[i]
        inp[i] = inp[size-i-1]
        inp[size-i-1] = temp
        
    print inp
    
def word_count():
    inp = open("sample_input.txt")
    read = inp.read()
    ws = read.split()
    h = {}
    for w in ws:
        num = h.get(w, 0)
        num += 1
        h[w] = num
    
    for k, v in h.iteritems():
        print "%s:\t%d"%(k, v)

def bubblesort(inp):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(inp)-1):
            if inp[i] > inp[i+1]:
                temp = inp[i]
                inp[i] = inp[i+1]
                inp[i+1] = temp
                swapped = True

bubblesort([1,4,7,3,2])