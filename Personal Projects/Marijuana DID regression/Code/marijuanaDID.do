capture log close
log using logtest.txt, replace text
clear

*code we've run
cd "C:\Users\gobenner\Box\Econ 398 Research\Tables_Graphs_Datasets Final Draft"

*prepping square mileage data for merge
import excel "state sq mileage.xlsx", firstrow
rename State state

*some observations were on territories that did not have sq mileage measurements
drop if SqMileage==. 
save "state_pop_density", replace

*wrangling unemployment data and prepping it for merge
import excel "state_unemployment.xlsx", firstrow clear

*getting the names of the vars to appear as their respective labels
foreach var of varlist C-AO {
    local label : variable label `var'
    rename `var' year`label'
}
drop Fips

*reshaping for merge
drop if state == "United States"
encode state, gen(state_identifier)
duplicates drop
reshape long year, i(state_identifier) j(placeholder)
rename year unemploymentrate
rename placeholder year
drop if state==""
save "state_unemployment",replace

*wrangling GDP data and prepping it for merge
import excel "GDP per state 1971-2020.xlsx", firstrow clear
keep state I-AF
foreach var of varlist I-AF {
    local label : variable label `var'
    rename `var' year`label'
}
encode state, gen(state_identifier)
reshape long year, i(state_identifier) j(placeholder)
rename year GDPmillions
rename placeholder year
duplicates drop
save "state_GDP", replace

*executing the merge of square mileage data with population and crime dataset
import delimited "state_crime.csv", clear
merge m:1 state using state_pop_density, force nogen
drop if SqMileage==.
drop if year==.

*merging the unemployment data with our master dataset
merge 1:1 state year using state_unemployment, keep(1 3) nogen
merge 1:1 state year using state_GDP, keep(1 3) nogen

/*getting rid of obs on territories that were missing data. these were
usually U.S. territories that were missing data on either sq mileage or year obs.
Also, getting rid of pre 1980 data where we did not have unemployment rate data,
which also falls outside of a neccessary range for us to identify causality. Also, 
dropping DC, Alaska, and Hawaii because DC is a statistical outlier and Alaska and 
Hawaii are not part of the coniguous United States*/

drop if SqMileage==. | year==. | unemployment==.| state == "District of Columbia" | state == "Alaska" | state == "Hawaii"

*prepping population density variable
gen popdensity=datapopulation/SqMileage
gen GDPtotal=GDPmillions*1000000
gen GDPpercapita= GDPtotal/datapopulation

*prepping indicator for treatment for each state
gen legal =0
replace legal =1 if (state=="California" & year>2017)
replace legal =1 if (state=="Colorado" & year>2013)
replace legal =1 if (state=="Maine" & year>2016)
replace legal =1 if (state=="Massachusetts" & year>2016)
replace legal =1 if (state=="Nevada" & year>2016)
replace legal =1 if (state=="Oregon" & year>2015)
replace legal =1 if (state=="Washington" & year>2012)

*testing the first stage significance of our controls on legality (all are significant)
reg legal unemploymentrate popdensity GDPpercapita
test unemploymentrate popdensity GDPpercapita
scalar F_stat = r(F)
scalar F_p_value = r(p)


*regression with population density control, year and state fe, and clustered se
gen logvc =ln(dataratesviolentall)
gen logpc =ln(dataratespropertyall)

*dropping the year observations that dont have GDP per captita
drop if year <1997
ssc install outreg2
reg logvc legal i.year i.state_identifier logpc popdensity unemploymentrate GDPpercapita, cluster(state)
outreg2 using results, word

*setting up a local macro to call the treatment and control states as groups,
* we omitted 9, which is DC, because of its dispropotionately high crime rate
local treat_states  5 6 20 22 29 38 48
local control_states 1 3 4 7 8 10 12 13 14 15 16 17 18 19 21 23 24 25 26 27 28 30 31 32 33 34 35 36 37 39 40 41 42 43 44 45 46 47 49 50 51

*Generate averages of violent crime in treatment and control groups
egen mean_violentcrime_treat = mean(dataratesviolentall) if inlist(state, "Colorado", "California", "Maine", "Massachusetts", "Nevada", "Oregon", "Washington"),by(year)
egen mean_violentcrime_control = mean(dataratesviolentall) if !inlist(state, "Colorado", "California", "Maine", "Massachusetts", "Nevada", "Oregon", "Washington"),by(year)

*prepping graphical representation of data
local lp
foreach var in `control_states'  {
    local lp `lp' line mean_violentcrime_control year if state_identifier==`var', lcolor(blue) ||
}
foreach var in `treat_states'  {
    local lp `lp' line mean_violentcrime_treat year if state_identifier==`var', lcolor(orange) ||
}

twoway `lp', legend(off) xline(2015)
graph export "Parallel Trends Graph.png", replace
save "398dataproject.dta", replace

*prepping some summary stats
sort legal
by legal: summarize dataratesviolentall popdensity GDPpercapita dataratespropertyall unemploymentrate

*performing robustness checks by systematically removing controls to see how our coefficient changes
*removing property crime control
reg logvc legal i.year i.state_identifier popdensity unemploymentrate GDPpercapita, cluster(state)

*removing density control
reg logvc legal i.year i.state_identifier unemploymentrate GDPpercapita, cluster(state)

*removing financial controls
reg logvc legal i.year i.state_identifier, cluster(state)

log close
