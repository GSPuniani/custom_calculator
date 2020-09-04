Project: rocket_propellant_ratio_calculator

This project uses Python 3.7.4.

My custom calculator uses the Tsiolkovsky rocket equation (also called the "ideal rocket equation") to determine the proportion of the mass of propellant (fuel) relative to the weight of the full rocket (including propellant, tank, engines, payload, etc.). This calculator will require two input values from the user. One is 'delta-v', which is the total change in velocity (final velocity subtracted by the initial velocity, where the initial velocity is zero if the rocket is launching from Earth's surface). For example, a rocket starting from Earth's surface and ending in Low Earth Orbit could have a "delta-v" of 9.7 km/s, which is the final speed of the rocket for this trajectory. The other input value is the effective exhaust velocity, which is the velocity of the material ejected from the bottom of the rocket to produce thrust. Continuing with our previous scenario of a rocket bound for Low Earth Orbit, the effective exhaust velocity might be 4.5 km/s. This would yield a ratio of propellant mass to full rocket mass of 0.8842, which means that 88.4% of the total mass of a full rocket is just the fuel! Clearly, chemical propellant is highly inefficient. But the efficiency of a rocket can be improved by using multiple stages, which has been standard practice for decades now. 

More information about the Tsiolkovsky rocket equation can be found in the resources below. The ideal rocket equation makes many assumptions and shortcuts, but it is a good rule-of-thumb for quick calculations relating to orbital maneuvers. The equation is based on Newtonian mechanics, but it is special compared to the usual interpretation of Newton's Second Law of Motion (F = ma) because a rocket does not have constant mass during the course of its trajectory. As the rocket accelerates, the fuel is combusted to produce thrust. Using Newton's Laws of Motion and the Law of Conservation of Momentum, Tsiolkovsky derived the eponymous equation (although other scientists also did independently) and published his result in 1903. 

Resources: 
https://www.grc.nasa.gov/WWW/K-12/rocket/rktpow.html
https://www.nasa.gov/mission_pages/station/expeditions/expedition30/tryanny.html
https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation
