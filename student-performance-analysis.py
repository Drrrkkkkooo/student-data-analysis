# W3schools - Round(), break, plt.close()

import matplotlib.pyplot as plt

# Opening the Data
with open ("student_habits.csv") as fileData: 
  studentData = fileData.readlines()[1:]

# Variables
AllExam = []
AllAttendance = []
AllStudy = []
AllRating = []
AllMedia = []
maleCount = 0
femaleCount = 0
yesCount = 0
noCount = 0
jobPercentage = 0
femaleStudyHours = 0
maleStudyHours = 0
maleAverage = 0
femaleAverage = 0
jobAttendance = 0
noJobAttendance = 0
jobAtnRate = 0
noJobAtnRate = 0


# Cleaning and Sorting the Data
for line in studentData: 
  pieces = line.split(",")
  attendanceRate = float(pieces[5])
  mHealthRating = float(pieces[7])
  studyHours = float(pieces[2])
  examScore = float(pieces[8])
  part_time_job = str(pieces[4]).strip()
  mediaHours = float(pieces[3])
  gender = pieces[1]
  
  AllExam.append(examScore)
  AllAttendance.append(attendanceRate)
  AllStudy.append(studyHours)
  AllRating.append(mHealthRating)
  AllMedia.append(mediaHours)
  
  if part_time_job == "Yes":
    yesCount += 1
    jobAttendance += attendanceRate
    
  elif part_time_job == "No":
    noCount += 1
    noJobAttendance += attendanceRate
  
  if gender == "Female":
    femaleCount += 1
    femaleStudyHours += studyHours
  
  elif gender == "Male": 
    maleCount += 1
    maleStudyHours += studyHours
  
  
# Input/Output System
while True: 
  choice = input("Please select which piece of information you would like to see: \n [S]catter Plot - Attendance vs Class Score \n [B]ar Chart - Mental Health Rating vs Social Media Hours \n Statistic - Does having a [J]ob impact attendence? \n Statistic - Does [G]ender affect study hours? \n Or, type in 'Q' to quit \n " ).upper()
  
  if choice == "Q": 
    print("Ending the Program. Goodbye!")
    break
 
  elif choice == "S": 
    plt.figure()
    plt.scatter(AllExam, AllAttendance)
    plt.title("Comparing attendance rates with exam scores")
    plt.xlabel("Exam Scores")
    plt.ylabel("Attendence Rate (%)")
    plt.show()
    plt.close()

  elif choice == "J":
    jobPercentage = (yesCount / (yesCount + noCount)) * 100
    
    print("Only " + str(jobPercentage) + "% of students have a job. \n")

    # Calculating Average Attendance 
    jobAtnRate = round(jobAttendance/yesCount, 3)
    noJobAtnRate = round(noJobAttendance/noCount, 3)
    
    print("Students with a job have an attendance rate of " + str(jobAtnRate) + "%. ")
    print("Students without a job have an attendance rate of " + str(noJobAtnRate) + "%. \n")
    
    if jobAtnRate > noJobAtnRate: 
      print("Students with a job attend their classes at a higher rate than students without a job. Jobs do not seem to have a correlation with student attendence. \n")
    
    elif noJobAtnRate > jobAtnRate: 
      print("Students without a job attend their classes at a higher rate than students with a job. Jobs seem to have a correlation with student attendance. \n")
    
    else: 
      print("Jobs do not seem to have a correlation with student attendance. ")
    
  elif choice == "B":
    plt.figure()
    plt.bar(AllRating, AllMedia)
    plt.title("Comparing social media hours with mental health ratings")
    plt.xlabel("Mental Health Rating")
    plt.ylabel("Social Media Hours per Day")
    plt.show()
    plt.close()
  
  elif choice == "G":
    print("There are " + str(femaleCount) + " female students, who study a total of around " + str(int(femaleStudyHours)) + " hours. ")
    
    print("There are " + str(maleCount) + " male students, who study a total of around " + str(int(maleStudyHours)) + " hours. \n \n")
    
    # Averaging 
    maleAverage = maleStudyHours/maleCount
    femaleAverage = femaleStudyHours/femaleCount
    
    # Accounting for Varying Datasets
    print("Female students average about " + str(round(femaleAverage, 2)) + " hours per student. ")
    
    print("Male students average about " + str(round(maleAverage, 2)) + " hours per student. \n")
    
    if femaleAverage > maleAverage: 
      print("Female students study more by around " + str(round(float(femaleAverage - maleAverage), 2)) + "hours per student. Gender does seem to have some correlation with the amount of studying a student participates in.  \n")
      
    elif maleAverage > femaleAverage:
      print("Male students study more by around " + str(round(float(maleAverage - femaleAverage), 2)) + " hours per student. Gender does seem to have some correlation with the amount of studying a student participates in. \n")
      
    else: 
      print("Gender does not seem to have an affect on hours studied. ")
    
    

  else: 
    print("Invalid choice, please selecct S, B, J, G, or Q")
  