class rectangle :
    def __init__(self,w,l):
        self.w =w
        self.l = l
    def area(self):
            return(self.w*self.l)
    def per(self):
            return(self.w+self.l)*2
        
rec=rectangle(2,3)
print(rec.area())
print(rec.per())