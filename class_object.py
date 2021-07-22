"""class student:
    pass

x=student()
y=student()

x.name="ankit"
y.name="akash"
y.subject=["civil","autocad"]
print(x.name,y.name)
print("akash readd ",y.subject,"subject")
"""
"""class student:
    no_of_leaves=10

x=student()
y=student()

x.name="ankit"
y.name="akash"
y.subject=["civil","autocad"]
print(x.name,y.name)
print("akash readd ",y.subject,"subject")
print(x.no_of_leaves)
print(x.__dict__)      # DICT FUNCTION RETURNS THE DICTIONARY ONLY
print(student.__dict__) # DICT FUNCTION RETURNS THE DICTIONARY ONLY
"""
# INSTANCE VARIABLE(X AND Y) CAN NOT  CHANGE THE CLASS VARIABLE VALUE(NO_OF_VALUES)------------------------
# IF I WANT TO CHANGE CLASS VARIABLE(no_of_LEAVES) THEN I CAN CHANGE IT BY (STUDENT.no_of_leaves)-------
# IF I USE(X.NO_OF_LEAVES) THEN ONLY VALUE OF(X.NO_OF_LEAVES) WILL CHANGE------------------

# SELF_AND_INIT() FUNCTION------------------------------------------------------------------------

"""class student:
    no_of_leaves=10
    def printdetails(self):
        return f"Name is {self.name},subject is {self.subject} and course is {self.course}"
x=student()
y=student()

x.name="ankit"
y.name="akash"
y.subject=["civil","autocad"]
y.course="b.tech"
print(x.name,y.name)
print("akash read ",y.subject,"subject")
print(y.printdetails())
"""

# INIT FUNCTION IS CONSTRUCTOR--------------------------------------------------------------

"""
class student:
    def __init__(self,aname,acourse,Aage):
        self.name=aname
        self.course=acourse
        self.age=Aage
x=student("ankit","BCA",20)
y=student("akash","b.tech",24)
print("name is",x.name,"age is",x.age,"course is",x.course)
print("name is",y.name,"age is",y.age,"course is",y.course)
"""




