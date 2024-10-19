capture log close
log using log.txt, replace text
clear

*prepping death data by county
cd C:\Users\gobenner.BYU.000\Desktop\dp3
import delimited "us-counties-2020.csv",clear
collapse (max) deaths, by (county fips state)
save countydeaths, replace

*prepping data for county population
import delimited "co-est2022-alldata.csv", clear
gen fips = state*1000 + county
save countypopulation, replace

*merging death and population data by county
use countydeaths, clear
merge m:1 fips using countypopulation.dta, force nogen keep(3)
drop stname ctyname
gen pcdeaths = deaths/popestimate2020
gen pcdeathpct = pcdeaths*100
save mergedpcdataset, replace

*prepping hpi data
import excel using "HPI_AT_BDL_county.xlsx", clear cellrange("A7:H97668") firstrow
destring FIPScode Year AnnualChange HPI, replace
drop HPIwith1990base HPIwith2000base
keep if Year==2021
rename FIPScode fips
save preppedhpi, replace

*merging hpi and county data
merge 1:m fips using "mergedpcdataset.dta", force nogen keep(3)
drop county state
save dp3data, replace

*adding controls for urbanicity and population density
import excel "2020_UA_COUNTY.xlsx", clear firstrow
destring STATE COUNTY POP_COU, replace
drop if STATE==.
gen fips = STATE*1000 + COUNTY
save populationdensity.dta, replace

*bringing it all together
use dp3data, clear
merge m:1 fips using populationdensity.dta

*Data Analysis using Fixed Effects
encode State, generate(state_number)
gen lChangeHPI = ln(AnnualChange)
reg lChangeHPI pcdeathpct i.state_number ALAND_PCT_URB POPDEN_COU
summarize lChangeHPI pcdeathpct state_number ALAND_PCT_URB POPDEN_COU
twoway (scatter lChangeHPI pcdeathpct) (lfit lChangeHPI pcdeathpct), ytitle("log Annual Change HPI") xtitle("COVID-19 Deaths Per-Capita, County Level")

*This line should always be at the end
log close
