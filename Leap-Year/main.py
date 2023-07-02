# leap year
# on every year that is evenly distributed by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400
# solution 1
year = int(input("Which year you want to check? "))
count = 0
count2 = 1
if year%4 == 0:
   count+=1
   if year % 100 == 0:
      count2 = 0
   if year % 400 == 0:
      count +=1
   if count == 2 and count2 == 0 or count == 2 and count2==1:
      print("This year is leap year.")
   else:
      print("This year is not the leap year")
else:
  print("This year is not the leap year")

#solution 2:
if year%4==0:
  if year%100 ==0:
     if year%400 == 0:
        print("Leap Year")
     else:
        print("Not Leap Year")
  else:
    print("Not Leap Year.")
else:
  print("Not Leap Year.")
    