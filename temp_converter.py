print("Temperature Converter")
print("1.Celsius to Fahrenheit")
print("2. Fahrenheit tp Celsius")

choice = input("Choose(1/2):")

if choice =="1":
  c = float(input("Enter Celsius:"))
  f = (c*9/5) + 32
  print("Fahrenheit:", round(f,2))

elif choice =="2":
  f = float(input("Enter Fahrenheit:"))
  c = (f - 32)*5/9
  print("Celsius:", round(c,2))

else:
  print("Invalid option")
