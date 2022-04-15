# How to extract the grades of your class

The following are all the steps you need to follow:

* Make sure all the applications needed
* Run the file name as "tran_hong_grade_the_exam.py"
* Check the report
  

## Application

Python is the must application to run the program. You can download install application [here](https://www.python.org/downloads/).

In the program, we use Pandas and Numpy Dictionary. To check that they are available or not:
1. Go to C:\Users\"your account"\AppData\Local\Microsoft\WindowsApps which contain the file "python.exe".
2. Replace the path with "cmd" to call Command prompt.
3. Type "pip install pandas" to install pandas. Type "pip install numpy" to install numpy.


## Run the program

1. Go to the folder you download the file "tran_hong_grade_the_exam.py".
2. Replace the path with "cmd" to call Command prompt.
3. Type "dir" to open the file.
4. Type "python tran_hong_grade_the_exam.py" to run the program.
5. The program will print "Enter the class number (i.e.1,2,3,...): class". You input the class number you want to grade, for example: 2.
6. There will be a summary in terms of the grade of your class including:
    Total valid lines of data
    Total invalid lines of data
    Total student of high scores
    Mean (average) score
    Highest score
    Lowest score
    Range of scores
    Median score
    Question that most people skip
    Question that most people answer incorrectly

## Check the report

Program will automatically extract a report of the grade of your class with student ID and grade. The report will be stored in the same folder which you download the file "tran_hong_grade_the_exam.py".


If you want to research the program in detail, please take a look at [here](https://github.com/RosyTran10/D301_assignment2/blob/main/tran_hong_grade_the_exam.ipynb).