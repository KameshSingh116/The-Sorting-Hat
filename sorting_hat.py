#Radhe Radhe
#Python code to implement the working of the sorting hat from "Harry Potter!"
#initialize all the group points to 0
g=0
h=0
s=0
r=0
#Question 1
q1=input("Do you like Dawn or Dusk?:")
if(q1=="Dawn"):
    g+=1
    r+=1
elif(q1=="Dusk"):
    h+=1
    s+=1
else:
    print("Wrong Input!")
#Question 2
q2=int(input('''When i am dead i want people to remember me as:  
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold:'''))
print("\n")
if(q2==1):
    h+=1
elif(q2==2):
    s+=1
elif(q2==3):
    r+=1
elif(q2==4):
    g+=1
else:
    print("Wrong Input!")
#Question 3
q3=int(input('''What kind of instrument most pleases your ear:
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum:'''))
print("\n")
#Conditions to diaplay the final house alloted
if (q3==1):
    s+=4
elif(q3==2):
    h+=4
elif(q3==3):
    r+=4
elif(q3==4):
    g+=4
else:
    print("Wrong Input!")

if(r>s and r>h and r>g):
    print("Ravenclaw!!!")
elif(s>r and s>g and s>h):
    print("Slytherine!!!")
elif(h>s and h>r and h>g):
    print("Hufflepuff!!!")
elif(g>h and g>s and g>r):
    print("Gryffindor!!!")

    #Radhe Radhe