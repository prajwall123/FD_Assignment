from django.shortcuts import render



def perm3(c):           # function that accepts string length of 3
    c1 = c[0:1]
    c2 = c[1:2]
    c3 = c[2:3]
    list3 = []
    list3.append(c1 + c2 + c3)
    list3.append(c1 + c3 + c2)
    list3.append(c2 + c1 + c3)
    list3.append(c2 + c3 + c1)
    list3.append(c3 + c2 + c1)
    list3.append(c3 + c1 + c2)
    return list3

def perm4(st):                #Function that accepts string length of 4
    results = []
    
    c1 = st[0:1]
    l = perm3(st[1:])
    for i in l:
        results.append(c1 + i)
       
    c2 = st[1:2]
    l = perm3(st[2:] + c1)
    for i in l:
        results.append(c2 + i)
   
    c3 = st[2:3]
    l = perm3(st[3:] + c1 + c2)
    for i in l:
        results.append(c3 + i)
    
    c4 = st[3:4]
    l = perm3(c1 + c2 + c3)
    for i in l:
        results.append(c4 + i)
    
    return results


def perm5(t):          #Function that accepts string length of 5
    results = []
    
    c1 = t[0:1]
    l = perm4(t[1:])
    for i in l:
        results.append(c1 + i)
    
    c2 = t[1:2]
    l = perm4(t[2:] + c1)
    for i in l:
        results.append(c2 + i)
    
    c3 = t[2:3]
    l = perm4(t[3:] + c1 + c2)
    for i in l:
        results.append(c3 + i)
    
    c4 = t[3:4]
    l = perm4(t[4:] + c1 + c2 + c3)
    for i in l:
        results.append(c4 + i)
    
    c5 = t[4:5]
    l = perm4(c1 + c2 + c3 + c4)
    for i in l:
        results.append(c5 + i)
    
    return results

# END OF HARD CODING

def get_possibilities(s):        #a python function for strings length>5
    if len(s) == 1:
        return [s]
    possibilities = []
    for i in range(len(s)):
        char = s[i]
        remaining_str = s[:i] + s[i+1:]
        for p in get_possibilities(remaining_str):
            possibilities.append(char + p)
    return possibilities

def permutation(request):
    if request.method == 'POST':
        input_string = request.POST.get('input_string')
        if(len(input_string)==3):
            perm = perm3(input_string)
        elif(len(input_string)==4):
            perm = perm4(input_string)
        elif(len(input_string)==5):
            perm=perm5(input_string)
        else:
            perm=get_possibilities(input_string)
        return render(request, 'app4/perm.html', {'permutations': perm, 'input_string': input_string})
    return render(request, 'app4/perm.html')


