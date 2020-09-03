import math

#These two print statements orient the user as to the purpose and proper usage of this calculator
print("Welcome! This calculator uses the Tsiolkovsky rocket equation (also called the 'ideal rocket equation') to determine the proportion",
"of the mass of propellant (fuel) relative to the weight of the full rocket (including propellant, tank, engines, payload, etc.).")
print("This calculator will require two input values. One is 'delta-v', which is the total change in velocity.",
"For example, a rocket starting from Earth's surface and ending in Low Earth Orbit could have a 'delta-v'",
"of 9.7 km/s, which is the final speed of the rocket for this trajectory. The other input value is the effective",
"exhaust velocity, which is the velocity of the material ejected from the bottom of the rocket to produce thrust.",
"Continuing with our previous scenario of a rocket bound for Low Earth Orbit, the effective exhaust velocity",
"might be 4.5 km/s. More information about this rocket equation can be found in the resources below.")

#Here, the user is instructed to enter two input values, with suggested values included
#The values are stored in variables
deltaV = float(input("Please enter a value for delta-v in km/s (try values like 7.8 or 9.7): "))
exhaustV = float(input("Please enter a value for effective exhaust velocity in km/s (try values like 3.4 or 4.5): "))

#If deltaV has a value of 7.8 km/s and exhaustV has a value of 3.4 km/s, then the answer should be around 0.9 or 90%
#If deltaV has a value of 9.7 km/s and exhaustV has a value of 4.5 km/s, then the answer should be 0.884 or 88.4%

#This equation is a reformulation of Tsiolkovsky's rocket equation
#mass_ratio is the ratio of the mass of the full rocket (with propellant) to the mass of the empty rocket (without propellant)
mass_ratio = math.exp(deltaV / exhaustV)
#Inverting the mass ratio and subtracting from 1 yields the ratio of propellant mass to mass of fully loaded rocket
#This fraction is basically (mass of full rocket - mass of empty rocket) / (mass of full rocket), where the numerator is the propellant mass
proportion_of_fuel = 1 - (1 / mass_ratio)

print(f"The ratio of the mass of the propellant to the mass of the full rocket is {round(proportion_of_fuel, 4)},",
f"which means that {round(proportion_of_fuel * 100, 2)}% of the mass of the full rocket is just the propellant!")


print("Clearly, chemical propellant is highly inefficient. But the efficiency of a rocket can be improved by using",
"multiple stages and other technical improvements.")


#References:
#https://www.grc.nasa.gov/WWW/K-12/rocket/rktpow.html
#https://www.nasa.gov/mission_pages/station/expeditions/expedition30/tryanny.html
#https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation