employees = ['Madhavi','kunny','Madha']
defaults = {"designation": 'Developer', "salary": 80000}
##data=dict()
##for i in employees:
##    data[i]=defaults
data=dict.fromkeys(employees,defaults)
print(data)
