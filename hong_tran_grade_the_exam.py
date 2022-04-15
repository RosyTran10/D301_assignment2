import pandas as pd
class1 = pd.read_csv('https://drive.google.com/uc?export=download&id=1As-p6PnJFY6gvvyRMqH5lLEv1DzUR47R', sep = " ", header=None)
class2 = pd.read_csv('https://drive.google.com/uc?export=download&id=18TDdhQvkMvECCbdBbaCYAQHknHCw9Srw', sep = " ", header=None)
class3 = pd.read_csv('https://drive.google.com/uc?export=download&id=1uaULHWPUHJCIqjMI3_8V2mFqwmcAFe8g', sep = " ", header=None)
class4 = pd.read_csv('https://drive.google.com/uc?export=download&id=1AzA8OGQQQD6rBnDW97xF5F_50Hl1-9ze', sep = " ", header=None)
class5 = pd.read_csv('https://drive.google.com/uc?export=download&id=192lcfvbwdCLeyKUMFSebFIN_F8q45LGx', sep = " ", header=None)
class6 = pd.read_csv('https://drive.google.com/uc?export=download&id=1NdR4432-NPcdkQJ4kq5_HBS8JJQH7sGW', sep = " ", header=None)
class7 = pd.read_csv('https://drive.google.com/uc?export=download&id=1hQVk49A8Xv_60SKk1-2YD7JOTSkXskjY', sep = " ", header=None)
class8 = pd.read_csv('https://drive.google.com/uc?export=download&id=1TfCgkYvnSkJg12ixOiei_f8QJ9rqLCvP', sep = " ", header=None)


# In[41]:


# open the requested file (Sử dụng exception)
fileset = [class1, class2, class3, class4, class5, class6, class7, class8]
try:
    filename = int(input('Enter the class number (i.e.1,2,3,...): class'))
    if 1 <= filename <= 8:
        print('Successfully opened class',filename,'.txt')
        yourfile = fileset[filename-1]
    else:
        print('Your class number is exceed the data.') # in case of over 8
except:
    print('It is not a class number.') # in case of not integers


# In[42]:


# TASK 2
# create numpy of your file
import numpy as np
A = np.array(yourfile)
row, column = A.shape

# create pandas of your file
f = []
i = 0
while i < row:
    a = A[i,0].split(',') # split items in a list
    i = i + 1
    f.append(a)
df = pd.DataFrame(f, dtype=object) # pandas 1


# In[43]:


# check data format (Tiêu chí 2)
import re
Nid = re.compile('N\d\d\d\d\d\d\d\d') # use regex to check invalid student ID

print('**** ANALYZING ****')
check = []
i = 0
while i < row:
    a = A[i,0].split(',')
    n = df.iloc[i,0] # extract student ID
    i = i + 1
    if len(a) != 26: # more or less than 25 answers
        check.append('wrong')
        print('Invalid line of data: does not contain exactly 26 values:', A[i-1,0])        
    if not Nid.match(n): # invalid student ID
        check.append('wrong') 
        print('Invalid line of data: N# is invalid', A[i-1,0])  
if len(check) == 0: # in case of no invalid data
    print('No errors found!')

print('**** REPORT ****')
print('Total valid lines of data: ', row - len(check))
print('Total invalid lines of data: ', len(check))


# In[44]:


# TASK 3
# count point of whole class, except for invalid lines
answer_key = ['B','A','D','D','C','B','D','A','C','C','D','B','A',
              'B','A','C','B','D','A','C','A','A','B','D','D']
point = []
detail = []
i = 0
while i < row:
    a = A[i,0].split(',')
    n = df.iloc[i,0]
    j = 0
    B = []
    if (len(a) == 26 and Nid.match(n)):
        while j < len(answer_key):
            if answer_key[j] != a[j+1]:
                if a[j+1] == '':
                    B.append(0) # skip answer 0 point
                else:
                    B.append(-1) # wrong anser -1 point
            else:
                B.append(4) # correct answer +4 point
            j = j + 1
            b = sum(B)
    else:
        b = np.nan # return invalid lines as NaN value
    point.append(b) # list of total point per student
    detail.append(B) # list of point per answer
    i = i + 1


# In[45]:


# print report (Tiêu chí 3)
df1 = pd.DataFrame(point, dtype=int) # pandas 2
df1.columns = ['Point']
print('Total student of high scores: ', sum(df1.Point > 80))
print('Mean (average) score: ', round(df1['Point'].mean(),3))
print('Highest score: ', df1['Point'].max())
print('Lowest score: ',df1['Point'].min())
print('Range of scores: ', df1['Point'].max() - df1['Point'].min())
print('Median score: ', df1['Point'].median())

# count skipped answers
df2 = pd.DataFrame(detail, dtype=int) # pandas 3
skip = [0]
i = 0
while i < 25:
    skip.append(sum(df2[i] == 0))
    i = i + 1
# count incorrect answers
incorrect = [0]
i = 0
while i < 25:
    incorrect.append(sum(df2[i] == -1))
    i = i + 1
# print report
indices = [i for i, x in enumerate(skip) if x == max(skip)] # extract repeat skip question
print('Question that most people skip (Question No. - People No. - % skip): ',
      indices, ' - ', max(skip), ' - ', round(max(skip)/row,3))
indices = [i for i, x in enumerate(incorrect) if x == max(incorrect)] # extract repeat incorrect question
print('Question that most people answer incorrectly (Question No. - People No. - % incorrect): ',
      indices, ' - ', max(incorrect), ' - ', round(max(incorrect)/row,3))


# In[46]:


# TASK 4
# create report files
class1_grades = 'class1_grades.txt'
class2_grades = 'class2_grades.txt'
class3_grades = 'class3_grades.txt'
class4_grades = 'class4_grades.txt'
class5_grades = 'class5_grades.txt'
class6_grades = 'class6_grades.txt'
class7_grades = 'class7_grades.txt'
class8_grades = 'class8_grades.txt'
reportset = [class1_grades,class2_grades,class3_grades,class4_grades,
             class5_grades,class6_grades,class7_grades,class8_grades]
yourreport = reportset[filename-1]


# In[47]:


# extract the list of grade (Tiêu chí 4)
i = 0
result = []
while i < row:
    a = A[i,0].split(',')
    n = df.iloc[i,0]
    i = i + 1
    if (len(a) == 26 and Nid.match(n)):    
            c = ''.join([n, ',', str(point[i-1]),'\n'])
            result.append(c)

# write the list to report file
with open(yourreport, 'w') as report:
    for line in result:
        print(line)
        report.write(line)

