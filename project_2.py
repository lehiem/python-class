# This program is used to calculate heat add (Q). The program asks for specific heat, mass, the start tempreature and the end tempreature to calculate heat added. Each is stored in seprate variables. Specific heat = C Mass=m. They are all printed and then you calculate the change in tempreature by subtracting the starting tempreature by the end tempreature and taking it's the absoulte value. Then you mulitple all of the variables together specific heat/C * mass/m * change in tempreature/change_in_tempreature. That is stored in a variable called heat_added. The last part is printing heat added/the answer. 
# Test: Specific heat=1.1, Mass=15, Start Tempreture=30, End Tempreature= 15 Result should equal 247.5
specific_heat = input("What is the specific heat?")
print ("C:"+ specific_heat)
mass = input("What is the mass?")
print ("m:"+mass)
start_tempreature= input("What is the start tempreture?")
end_tempreature= input("What is the end tempreature?")
start_tempreature = float (start_tempreature)
end_tempreature = float(end_tempreature)
change_in_tempreature = abs(start_tempreature - end_tempreature)
# To calculate delta tempreature you have to subtract the starting tempreture and the end tempreture and take the absolute value to make it positve 
change_in_tempreature_str = str(change_in_tempreature)
print ("Change in tempreture is: "+ change_in_tempreature_str)
mass = float(mass)
specific_heat= float(specific_heat)
heat_added = specific_heat*mass*change_in_tempreature
# Finishing the equation by multiplying all the parts of the formula 
heat_added= str(heat_added)
print ("The heat added is "+heat_added)