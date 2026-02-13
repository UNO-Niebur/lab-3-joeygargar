#TempConvert.py
#Name:Mia Garcia
#Date:2/12/26
#Assignment:Lab 3 


def main():
  #Prompt the user for a Fahrenheit temperature
  fah = int(input("provide a temperature in Fahrenheit:"))
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
 
  
  cel = (fah - 32) * 5/9

  roundedcel = round(cel,1)
  
  print(fah, "is ", cel, "degrees celsius.")
if __name__ == '__main__':
  main()
