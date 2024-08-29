#!/usr/bin/env python
# coding: utf-8

# In[10]:


students={}
student_name=['arun','naman','kajol','lalit']
Class=[9,10,12,10]
ht=[6,5,6,5]
wt=[56,70,50,68]
sport=['cricket','volleyball','tennis','tennis']


# In[12]:


students['name']=student_name
students['class']=Class
students['height']=ht
students['weight']=wt
students['sport']=sport


# In[16]:


students


# In[29]:


calories=[100,50,300,400]


# In[30]:


students['calories']=calories


# In[20]:


len (students['name'])


# In[42]:


def calc_diet(students):
    print("diet chart\n")
    length=len(students['name'])
    for i in range(0,length):
        print(students['name'][i],": ",students['height'][i]," ",students['weight'][i]," ",students['calories'][i])
       
        if students['calories'][i]>=100:
           bmi=students['weight'][i]/students['height'][i]
           print("bmi: ",bmi) 
           if bmi<10:
              print("orange: needs more intake\n")
          
           else:
              print("green: sufficient consumption\n")
        else:
           print("red: underweight\n")

      


# In[43]:


calc_diet(students)


# In[49]:


students={}
student_name=['arun','naman','kajol','lalit']
Class=[9,10,12,10]
ht=[6,5,6,5]
wt=[56,70,50,68]
sport=['cricket','volleyball','tennis','tennis']
calories=[100,50,300,400]
students['name']=student_name
students['class']=Class
students['height']=ht
students['weight']=wt
students['sport']=sport
students['calories']=calories
print(students)
def calc_diet(students):
    print("\ndiet chart\n")
    length=len(students['name'])
    for i in range(0,length):
        print(students['name'][i],": ",students['height'][i]," ",students['weight'][i]," ",students['calories'][i])
       
        
        
        bmi=students['weight'][i]/students['height'][i]
        print("bmi: ",bmi) 
        if bmi<10:
                 print("red: underweight\n")
        else:                
                 if students['calories'][i]<=100:
                   print("orange: needs more intake\n")
          
                 else:
                   print("green: sufficient consumption\n")
       
          

calc_diet(students)


# In[ ]:




