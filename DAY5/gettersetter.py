class student:
    def __init__(self,name,branch,rno):
        self.sname=name
        self.sbranch=branch
        self.rno=rno
    def name(self): #instance method
        print(self.sname)
    @property
    def from_branch(self):
        return self.sbranch
    @from_branch.setter
    def from_branch(self,branch):
        self.sbranch=branch
    @from_branch.deleter    
    def from_branch(self):
        self.branch=None
s1=student("chaitanya","CSM",41)
s3=student("chaitanya","CSM",41)
s2=student("sai","CSM",64)
print(s1.from_branch)
s1.from_branch="CSE"
print(s1.sbranch)
#del s1.from_branch
s1.from_branch=None
print(s1.sbranch)   