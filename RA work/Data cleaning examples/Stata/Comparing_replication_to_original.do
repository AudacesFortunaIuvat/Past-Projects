


/*
By owen

This was a little project to compare the outputs of a replication package with an original dataset. The do file brings in datasets, purges them of variables that arent in each, and compares outputs along the way. It then makes some visualizations of the differences for easy comparison. 

comparing the current replication output, i.e. principals merged with schools for both may and july to see their differences 
note: uses the "compare files 2" function
ssc install cf2
*/

cd "C:\Users\grega\Documents\GitHub\ParentalInvolvementRA\Owen's works in progress\comparing replication to original"

*importing, and sorting for comparison 
use temp_replication, clear
sort emailaddress 
save, replace
use temp_original, clear
sort emailaddress
save, replace
*comparing
*cf _all using temp_replication

/*several variables don't match, will use cf2 to see if it has only to do with ordering
checking to make sure differences arent an artifact of sorting

cf2 _all using temp_replication
the cf2 command output the same variables as containing differences.

Need to grab the list of all vars that don't exist in the replication dataset, this is easiest in python. this grabs the varlist from each dataset and generates a list of any vars in the original dataset that dont also exist in the replciation. This should be the same list as the cf command output, which regretably does not produce a return value that can be copied easily.
*/

python

import pandas as pd
temp_original = pd.read_stata('temp_original.dta')
temp_replication = pd.read_stata('temp_replication.dta')
original_vars = list(temp_original.columns)
replication_vars = list(temp_replication.columns)
missing_vars = [var for var in original_vars if var not in replication_vars]
for var in missing_vars:
	print(var)
end

*copy that varlist and put them into a drop command
use temp_original, clear
drop treatmentOld LocationState NumObsRunning OLD_a_weight OLD_p_weight OLD_f_weight GEO_ID Area_Name malemedianwage femalemedianwage census_wagegap GEO_ID1 fips fips_long FILEID STUSAB SUMLEV GEOCOMP LOGRECNO STATE COUNTY GEOID NAME QName AREALAND AREAWATR laborforcemale laborforcemale_perc laborforcefem laborforcefem_perc lemail_2 county_state State CountyName FIPSState FIPSCounty state_abbr manual_fips year state_po county_name office candidate party candidatevotes totalvotes republican_voteshare_16 fipsstat sexism_index population_2010 rural geo_id county pop2010 totalreligiousadherence outcome Baseline MaleHigh MaleLow FemaleHigh FemaleLow DMFem Main Pay Exp FT voicemail voicemail0

save dropped_original, replace
*cf _all using temp_replication

*again checking to make sure the differences arent an artifact of sorting, and they are not.
*cf2 _all using temp_replication

describe
*209 vars, 80071 obs
use temp_replication, clear
describe
*211 vars, 80071 obs

*there's still 2 vars this guy has that arent in the original, dropping using same process
python 
other_missing_vars= [var for var in replication_vars if var not in original_vars]
for var in other_missing_vars:
	print(var)
end

*take that list and drop them
drop treatment locationstate
save dropped_replication, replace

*checking again, still same output.
*cf _all using dropped_original

*Now it's time to determine how far off the replication is from the original_vars
*grab a sample of 50 from the origial dataset. Using the same seed, the vars will correspond since theyre sorted the same.
use dropped_original, clear
set seed 420
*sample 50, count
save sampled_original, replace

*to prep the visualizations we merge the two datasets together, but first we need to destring the var "duration" so they can merge

use dropped_replication,clear
replace duration = "." if duration == " NA"
destring duration, replace
keep emailaddress WhoCalled FemaleNum0 MaleNum0 Treatment lemail tonumber fromnumber
save sampled_replication, replace

*When I tried merging these two datasets, I got a perfect merge. This meant that the differences noted by the cf command disappeared. So, I generated new vars to show the difference between the original and the replication.

use sampled_original, clear
keep emailaddress WhoCalled FemaleNum0 MaleNum0 Treatment lemail tonumber fromnumber
foreach var of varlist WhoCalled FemaleNum0 MaleNum0 Treatment lemail tonumber fromnumber {
    rename `var' `var'_orig
}

*now I merge and make the difference var
merge 1:1 emailaddress using sampled_replication
keep if _merge==3

foreach var of varlist WhoCalled FemaleNum0 MaleNum0 Treatment lemail tonumber fromnumber {
    gen aresame_`var'= `var'==`var'_orig
}

foreach var of varlist WhoCalled FemaleNum0 MaleNum0 Treatment lemail tonumber fromnumber {
	tab aresame_`var'
}

sort aresame_WhoCalled

save compared_outputs_keyvariables, replace

*now we prep some visualizations
gen observation=_n
foreach var in WhoCalled FemaleNum0 MaleNum0 Treatment lemail tonumber fromnumber {
    twoway (scatter `var' observation, mcolor(blue)) ///
           (scatter `var'_orig observation, mcolor(red)), ///
           title("Comparison of `var': Original vs Replication") ///
           legend(order(1 "Replication" 2 "Original")) ///
           xlabel(, nogrid) ylabel(, nogrid)
	graph export sidebyside_`var'.png, replace
}


foreach var in WhoCalled FemaleNum0 MaleNum0 Treatment lemail tonumber fromnumber {
    twoway (scatter diff_`var' observation), ///
        yline(0) title("Differences in `var'") ///
        ytitle("Difference (Original - Replication)") xtitle("observation")
    graph export diff_`var'_scatter.png, replace
}






