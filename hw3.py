from data import CountyDemographics
from build_data import get_data

# finding 2014 population for all counties
def population_total(counties:list[CountyDemographics]):
    return sum(county.population.get('2014 Population') for county in counties)     # totals the population for each county in all counties

# finding number of counties in state
def filter_by_state(counties:list[CountyDemographics],state:str):
    return [county for county in counties if county.state == state]        # creates new list that only has counties in specified state

# next three are similar: finding percentage of specified demographic and then multiplying by total population, then repeating and summing all results for whole list of given counties
def population_by_education(counties:list[CountyDemographics],edu:str):
    total = 0
    for county in counties:
        edu_percent = float(county.education.get(edu)/100)        #converting to decimal for usage as percent
        pop = county.population.get('2014 Population')            # getting total population
        total += edu_percent*pop                                  # adding population of interest by multiplying by demographic percentage
    return total

def population_by_ethnicity(counties:list[CountyDemographics],eth:str):
    total = 0
    for county in counties:
        eth_percent = float(county.ethnicities.get(eth)/100)
        pop = county.population.get('2014 Population')
        total += eth_percent*pop
    return total

def population_below_poverty_level(counties:list[CountyDemographics]):
    total = 0
    for county in counties:
        poverty_percent = float(county.income.get('Persons Below Poverty Level')/100)
        pop = county.population.get('2014 Population')
        total += poverty_percent*pop
    return total

# next three are similar: using last three function and dividing by total population to then find percentage of desired demographic given list of counties
def percent_by_education(counties:list[CountyDemographics],edu:str):
    return population_by_education(counties,edu)/population_total(counties)

def percent_by_ethnicity(counties:list[CountyDemographics],eth:str):
    return population_by_ethnicity(counties,eth)/population_total(counties)

def percent_below_poverty_level(counties:list[CountyDemographics]):
    return population_below_poverty_level(counties)/population_total(counties)

# last six are similar: returning list of counties if they match certain threshold - using three above functions to determine whether they match desired threshold
def education_greater_than(counties:list[CountyDemographics],edu:str,percent:float):
    return [county for county in counties if percent_by_education([county],edu) >= percent]

def education_less_than(counties:list[CountyDemographics],edu:str,percent:float):
    return [county for county in counties if percent_by_education([county],edu) <= percent]

def ethnicity_greater_than(counties:list[CountyDemographics],eth:str,percent:float):
    return [county for county in counties if percent_by_ethnicity([county],eth) >= percent]

def ethnicity_less_than(counties:list[CountyDemographics],eth:str,percent:float):
    return [county for county in counties if percent_by_ethnicity([county],eth) <= percent]

def below_poverty_level_greater_than(counties:list[CountyDemographics],percent:float):
    return [county for county in counties if percent_below_poverty_level([county]) >= percent]

def below_poverty_level_less_than(counties:list[CountyDemographics],percent:float):
    return [county for county in counties if percent_below_poverty_level([county]) <= percent]
