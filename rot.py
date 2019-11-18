box = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

input_line = input("want to change sentence : ")
a = input_line
input_line = list(input_line)
#L = input("rot? : ")
#l = int(L)

count = 0
l = 0
box2 = []
while count <= 26:
    for i in range(len(input_line)):
        number = box.index(input_line[i])
        if number + l >=26:
            b = number + l  -26
        else:
            b = number + l
        input_line[i] = box[b]
    box2 = input_line
    box2 = map(str,box2)
    box2 = "".join(box2)
    #print(box2)
    if len(str(count))==2:
        print("rot"+str(count)+" "+box2)
    else:
        print("rot"+"0"+str(count)+" "+box2) 

    #if len(str(count))==2:
       # print("rot"+str(count)+" "+str(input_line))
    #else:
        #print("rot"+"0"+str(count)+" "+str(input_line)) 
    count += 1
    l += 1
    input_line = list(a)

#box2 = map(str,box2)
#box2 = "".join(box2)
#print(box2)

