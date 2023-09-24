import interest as i
pri=float(input("enter principal : "))
rat=float(input("enter rate of interest : "))
tim=float(input("enter time : "))
print("Default Values :")
print("Simple Intrest :",i.simp_intr(pri,tim))
print("Compound Intrest :",i.comp_intr(pri,tim))
print("User given Values : ")
print("Simple Intrest :",i.simp_intr(pri,tim,rat))
print("Compound Intrest :",i.comp_intr(pri,tim,rat))

