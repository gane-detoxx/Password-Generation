# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:56:16 2020
@author: ganesh
"""
import random as r
class gen_pass:
    def __init__(self,name):
        self.c="" #password variable
        self.n=name
    def genlen(self):
        return r.randint(8,15)
    def assignNUL(self,x,y):
        return chr(r.randint(x, y))
    def assignspl(self):
        s=list("!@#$^&*()_-/\\:<>.")
        return r.choice(s)
    def assign(self,x):
        if x==0:
            return self.assignNUL(ord("A"),ord("Z"))
        elif x==1:
            return self.assignNUL(ord("a"),ord("z"))
        elif x==2:
            return self.assignNUL(ord("0"),ord("9"))
        else:
            return self.assignspl() 
    def genstr(self):
        x=self.genlen()
        for i in range(x):
            if i<4:
                self.c+=self.assign(i)
            else:
                self.c+=self.assign(r.randint(0, 3))
        l=r.sample(self.c,len(self.c))
        self.c="".join(i for i in l)
#the below code is for testing purpose
a=gen_pass(input("ENTER YOUR USERNAME: "))
a.genstr()
print("USERNAME:",a.n)
print("PASSWORD:",a.c)
            
        
            
            
            
            
            

