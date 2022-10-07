loop = 1
print("TRAFFIC LIGHT SYSTEM")
print("Input Data Catagorization:")
print(" RED:STOP")
print(" YELLOW:GET READY")
print(" GREEN:GO")
print("----------------------------")
loop=eval(input("press 1 to start : "))
while True:
 print("enter input signal colour to run the program : ")
 signal = input()
 if signal == "red":
 print("STOP THE VEHICLE FOR NEXT 60 SECONDS")
 else:
 if signal =="yellow":
 print("get ready")
 else:
 if signal=="green":
 print("go")
 else:
 if signal=="stop":
 print("you choose to end the program")
 else:
 print("enter only the correct signal")
