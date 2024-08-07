# Module 5 Lab-5
# The main function
def main(): 
 getSales() #call to get sales
   
 
# This function gets the monthly sales
def getSales():
    monthlySales = float(input('Enter the monthly sales $'))
    return monthlySales

# This function gets the percent of increase in sales
def getIncrease():

     salesIncrease = getIncrease() #call to get sales increase

     salesIncrease = float(input('Enter percent of sales increase: '))
     salesIncrease = float(salesIncrease)
     salesIncrease = salesIncrease / 100
     return salesIncrease


# This function determines the storeAmount bonus
def storeBonus(MonthlySales):
  if MonthlySales >=110000:
        storeAmount = 6000
  elif MonthlySales >=100000:
        storeAmount = 5000
  elif MonthlySales >=90000:
        storeAmount = 4000
  elif MonthlySales >=80000:
        storeAmount = 3000
  else:
        storeAmount = 0
        return storeAmount
  #This function determines the empAmount bonus
def empBonus(salesIncrease):
 if salesIncrease >=.05:
   empAmount =75
 elif salesIncrease >=.04:
   empAmount = 50
 elif salesIncrease >=.03:
  empAmount =40
 else:
  empAmount =0
 return empAmount

 #call to get the store bonus
 storeAmount = storeBonus(monthlySales)
# This function prints the bonus information
def printBonus(storeAmount, empBonus):
    print (f'The store bonus amount is ${storeAmount}')
    print (f'The employee bonus amount is ${empBonus}')
    if storeAmount == 6000 and empBonus == 75:
     print(f'Congrats! You have reached the highest bonus amounts possible!')
 
# calls main

main()
 


MonthlySales = float(input('Enter the monthly sales $'))

def Increase():

     salesIncrease = getIncrease() #call to get sales increase

     salesIncrease = float(input('Enter percent of sales increase: '))
     salesIncrease = float(salesIncrease)
     salesIncrease = salesIncrease / 100
     return salesIncrease