from pyscript import display

x = "Year" #string
y = 2025 #integer
z = 3.14 #float
a = True #boolean
b = ['Student1', 'Student2', 'Student3'] #list
c = ('1', '2', '3') #tuple
d = {1,2,3} #set with num
e = {'emerald', 'ruby', 'sapphire'} #set with string
f = {
    "name": "Aeris",
    "age": 15,
    "description": "lazy"
} #dictionary

display('The data type of x is ', type(x), targets="div1") # display output in div
display(type(y), targets="div1") 
display(type(z), targets="div1")   
display(type(a), targets="div1")   
display(type(b), targets="div1")
display(type(c), targets="div1")
display(type(d), targets="div1")
display(type(e), targets="div1")
display(type(f["name"]), targets="div1")
display(f["description"], targets="div1")