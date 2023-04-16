# Script by Nephew Jonathan for *Works in Progress*, May 2023.  

# DO NOT SET ANY OF THESE VARIABLES TO A NEGATIVE NUMBER (except for 'decrease in emissions' if you want to simulate continued growth in emissions).

excess_CO2 = 2700 # how much excess CO2 needs to be gotten out of the atmosphere, in gigatonnes. For reference, 1 ppm of atmospheric CO2 is about 2.08 gigatonnes, though this doesn't count CO2 dissolved in ocean water (this script does not model gas exchange between atmosphere and ocean, but that exchange occurs reasonably quickly, particularly if it's dissolved CO2 being sequestered by underwater rock, which is quickly replenished by CO2 dissolved in rainwater).

yearly_emissions = 60 # worldwide yearly emissions, in gigatonnes

decrease_in_emissions = 0.5 # how much, year on year, are world emissions decreasing? (in gigatonnes)

necessary_emissions = 10 # yearly emissions from processes that can't be decarbonized that we'll just have to live with, in gigatonnes

amount_sequestered = 0.5 # amount *sequestered* by rock weathering (or other mechanisms) the first year, in gigatonnes

upper_limit = 100 # upper limit of sequestration, yearly, in gigatonnes. Only relevant if upper_limit_exists is set to True.

upper_limit_exists =  False # if set to True, then sequestration has an upper yearly limit. Otherwise, the above variable (upper_limit) is not used

doubling_time = 4 # doubling time, in years, for amount sequestered yearly. For example, if amount_sequestered is initialized to 0.5, and the doubling time is set to 5, then the fifth year of sequestration will see 1 gigatonne of carbon removed, the tenth year 2 gigatonnes...

year = 0 # initializing year count

while (excess_CO2 > 0):
    year += 1

    excess_CO2 += yearly_emissions
    
    if (yearly_emissions >= (necessary_emissions + decrease_in_emissions)):
        yearly_emissions -= decrease_in_emissions

    else:
        yearly_emissions = necessary_emissions

    if (upper_limit_exists == True):
        excess_CO2 -= (min(amount_sequestered, upper_limit))
    else:
        excess_CO2 -= amount_sequestered
    
    # The following line of code multiplies the amount sequestered that year by the [doubling time]th root of 2, which gives the year-on-year *increase* in sequestration, as a coefficient. For example, if the doubling time is 3 years, then the coefficient is the third root of 2 (1.2599...), or about a 26% year-on-year increase.

    amount_sequestered *= (2 ** (1/doubling_time))
       
if (year == 1): # never been a fan of "1 years"
    print("It will take one year to return to preindustrial levels (are you sure this is a realistic model?)")

else: 
    print("It will take " + str(year) + " years to return to preindustrial levels.")
