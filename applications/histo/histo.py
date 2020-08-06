
# Your code here
def histo(s):
    words = s.split
    count = {}

    for i in words():
        if i.lower() in count:
            count[i.lower()] += "#"
        else:
            count[i.lower()] = "#"
    
    for key, value in sorted(count.items()):
        print(f"{key}        {value}")
    # return count
    

    
f = open("applications\histo\Robin.txt", "r")
print(histo(f.read()))