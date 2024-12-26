def fun(s,l,r): # We are Definning three elements
    if l < r:  # if l < r then this work as a base condition to terminate the condition
        s[l],s[r] = s[r],s[l] # Here we Are Swaping the elements from the last ( like the index 0 , 5 )
        fun(s,l+1,r-1) # used to continue to the next element from  front and back 
s =["h","e","l","l","o"]        # Input string
fun(s,0,len(s)-1) 
print(s)
