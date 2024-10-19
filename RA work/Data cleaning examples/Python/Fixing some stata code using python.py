#This was an ugly set of commands written by a former RA that I chose to convert into a for loop.
#The first step in this process was taking this massive command and making some changes to its
#syntax, which was accomplished by this python code.


# Multi-line string input
lines = """
use in	1/66	using	..\data\derived\temporary\PRIVmaleblack3treatments	, clear
save	..\data\derived\temporary\PRIVmaleblack3treatments_subset		,replace
use in	1/73	using	..\data\derived\temporary\PRIVmaleblack4treatments	, clear
save	..\data\derived\temporary\PRIVmaleblack4treatments_subset		,replace
use in	1/155	using	..\data\derived\temporary\PRIVmaleblack5treatments	, clear
save	..\data\derived\temporary\PRIVmaleblack5treatments_subset		,replace
use in	1/82	using	..\data\derived\temporary\PRIVmaleblack6treatments	, clear
save	..\data\derived\temporary\PRIVmaleblack6treatments_subset		,replace
use in	1/224	using	..\data\derived\temporary\PRIVmaleblack7treatments	, clear
save	..\data\derived\temporary\PRIVmaleblack7treatments_subset		,replace
use in	1/82	using	..\data\derived\temporary\PRIVmaleblack8treatments	, clear
save	..\data\derived\temporary\PRIVmaleblack8treatments_subset		,replace
use in	1/53	using	..\data\derived\temporary\PRIVmaleblack9treatments	, clear
save	..\data\derived\temporary\PRIVmaleblack9treatments_subset		,replace
use ..\data\derived\temporary\PRIVmalehispanic1treatments	, clear	// ***will be using all observations in PRIVmalehispanic1treatments
save	..\data\derived\temporary\PRIVmalehispanic1treatments_subset	,replace
use in	1/13	using	..\data\derived\temporary\PRIVmalehispanic2treatments	, clear
save	..\data\derived\temporary\PRIVmalehispanic2treatments_subset	,replace
use in	1/9	using	..\data\derived\temporary\PRIVmalehispanic3treatments	, clear
save	..\data\derived\temporary\PRIVmalehispanic3treatments_subset	,replace
use in	1/23	using	..\data\derived\temporary\PRIVmalehispanic4treatments	, clear
save	..\data\derived\temporary\PRIVmalehispanic4treatments_subset	,replace
use in	1/21	using	..\data\derived\temporary\PRIVmalehispanic5treatments	, clear
save	..\data\derived\temporary\PRIVmalehispanic5treatments_subset	,replace
use in	1/5	using	..\data\derived\temporary\PRIVmalehispanic6treatments	, clear
save	..\data\derived\temporary\PRIVmalehispanic6treatments_subset	,replace
use in	1/36	using	..\data\derived\temporary\PRIVmalehispanic7treatments	, clear
save	..\data\derived\temporary\PRIVmalehispanic7treatments_subset	,replace
use in	1/38	using	..\data\derived\temporary\PRIVmalehispanic8treatments	, clear
save	..\data\derived\temporary\PRIVmalehispanic8treatments_subset	,replace
use in	1/15	using	..\data\derived\temporary\PRIVmalehispanic9treatments	, clear
save	..\data\derived\temporary\PRIVmalehispanic9treatments_subset	,replace
use in	1/409	using	..\data\derived\temporary\PRIVmalewhite1treatments	, clear
save	..\data\derived\temporary\PRIVmalewhite1treatments_subset		,replace
use in	1/158	using	..\data\derived\temporary\PRIVmalewhite2treatments	, clear
save	..\data\derived\temporary\PRIVmalewhite2treatments_subset		,replace
use in	1/287	using	..\data\derived\temporary\PRIVmalewhite3treatments	, clear
save	..\data\derived\temporary\PRIVmalewhite3treatments_subset		,replace
use in	1/204	using	..\data\derived\temporary\PRIVmalewhite4treatments	, clear
save	..\data\derived\temporary\PRIVmalewhite4treatments_subset		,replace
use in	1/619	using	..\data\derived\temporary\PRIVmalewhite5treatments	, clear
save	..\data\derived\temporary\PRIVmalewhite5treatments_subset		,replace
use in	1/163	using	..\data\derived\temporary\PRIVmalewhite6treatments	, clear
save	..\data\derived\temporary\PRIVmalewhite6treatments_subset		,replace
use in	1/538	using	..\data\derived\temporary\PRIVmalewhite7treatments	, clear
save	..\data\derived\temporary\PRIVmalewhite7treatments_subset		,replace
use in	1/442	using	..\data\derived\temporary\PRIVmalewhite8treatments	, clear
save	..\data\derived\temporary\PRIVmalewhite8treatments_subset		,replace
use in	1/206	using	..\data\derived\temporary\PRIVmalewhite9treatments	, clear
save	..\data\derived\temporary\PRIVmalewhite9treatments_subset		,replace
use in	1/520	using	..\data\derived\temporary\PUBLfemaleasian1treatments	, clear
save	..\data\derived\temporary\PUBLfemaleasian1treatments_subset	,replace
use in	1/166	using	..\data\derived\temporary\PUBLfemaleasian2treatments	, clear
save	..\data\derived\temporary\PUBLfemaleasian2treatments_subset	,replace
use in	1/104	using	..\data\derived\temporary\PUBLfemaleasian3treatments	, clear
save	..\data\derived\temporary\PUBLfemaleasian3treatments_subset	,replace
use in	1/193	using	..\data\derived\temporary\PUBLfemaleasian4treatments	, clear
save	..\data\derived\temporary\PUBLfemaleasian4treatments_subset	,replace
use in	1/238	using	..\data\derived\temporary\PUBLfemaleasian5treatments	, clear
save	..\data\derived\temporary\PUBLfemaleasian5treatments_subset	,replace
use in	1/60	using	..\data\derived\temporary\PUBLfemaleasian6treatments	, clear
save	..\data\derived\temporary\PUBLfemaleasian6treatments_subset	,replace
use in	1/206	using	..\data\derived\temporary\PUBLfemaleasian7treatments	, clear
save	..\data\derived\temporary\PUBLfemaleasian7treatments_subset	,replace
use in	1/233	using	..\data\derived\temporary\PUBLfemaleasian8treatments	, clear
save	..\data\derived\temporary\PUBLfemaleasian8treatments_subset	,replace
use in	1/94	using	..\data\derived\temporary\PUBLfemaleasian9treatments	, clear
save	..\data\derived\temporary\PUBLfemaleasian9treatments_subset	,replace
use in	1/1088	using	..\data\derived\temporary\PUBLfemaleblack1treatments	, clear
save	..\data\derived\temporary\PUBLfemaleblack1treatments_subset	,replace
use in	1/606	using	..\data\derived\temporary\PUBLfemaleblack2treatments	, clear
save	..\data\derived\temporary\PUBLfemaleblack2treatments_subset	,replace
use in	1/555	using	..\data\derived\temporary\PUBLfemaleblack3treatments	, clear
save	..\data\derived\temporary\PUBLfemaleblack3treatments_subset	,replace
use in	1/1568	using	..\data\derived\temporary\PUBLfemaleblack4treatments	, clear
save	..\data\derived\temporary\PUBLfemaleblack4treatments_subset	,replace
use in	1/1161	using	..\data\derived\temporary\PUBLfemaleblack5treatments	, clear
save	..\data\derived\temporary\PUBLfemaleblack5treatments_subset	,replace
use in	1/880	using	..\data\derived\temporary\PUBLfemaleblack6treatments	, clear
save	..\data\derived\temporary\PUBLfemaleblack6treatments_subset	,replace
use in	1/2281	using	..\data\derived\temporary\PUBLfemaleblack7treatments	, clear
save	..\data\derived\temporary\PUBLfemaleblack7treatments_subset	,replace
use in	1/657	using	..\data\derived\temporary\PUBLfemaleblack8treatments	, clear
save	..\data\derived\temporary\PUBLfemaleblack8treatments_subset	,replace
use in	1/258	using	..\data\derived\temporary\PUBLfemaleblack9treatments	, clear
save	..\data\derived\temporary\PUBLfemaleblack9treatments_subset	,replace
use in	1/1054	using	..\data\derived\temporary\PUBLfemalehispanic1treatments	, clear
save	..\data\derived\temporary\PUBLfemalehispanic1treatments_subset	,replace
use in	1/348	using	..\data\derived\temporary\PUBLfemalehispanic2treatments	, clear
save	..\data\derived\temporary\PUBLfemalehispanic2treatments_subset	,replace
use in	1/93	using	..\data\derived\temporary\PUBLfemalehispanic3treatments	, clear
save	..\data\derived\temporary\PUBLfemalehispanic3treatments_subset	,replace
use in	1/907	using	..\data\derived\temporary\PUBLfemalehispanic4treatments	, clear
save	..\data\derived\temporary\PUBLfemalehispanic4treatments_subset	,replace
use in	1/297	using	..\data\derived\temporary\PUBLfemalehispanic5treatments	, clear
save	..\data\derived\temporary\PUBLfemalehispanic5treatments_subset	,replace
use in	1/29	using	..\data\derived\temporary\PUBLfemalehispanic6treatments	, clear
save	..\data\derived\temporary\PUBLfemalehispanic6treatments_subset	,replace
use in	1/355	using	..\data\derived\temporary\PUBLfemalehispanic7treatments	, clear
save	..\data\derived\temporary\PUBLfemalehispanic7treatments_subset	,replace
use in	1/399	using	..\data\derived\temporary\PUBLfemalehispanic8treatments	, clear
save	..\data\derived\temporary\PUBLfemalehispanic8treatments_subset	,replace
use in	1/146	using	..\data\derived\temporary\PUBLfemalehispanic9treatments	, clear
save	..\data\derived\temporary\PUBLfemalehispanic9treatments_subset	,replace
use in	1/2866	using	..\data\derived\temporary\PUBLfemalewhite1treatments	, clear
save	..\data\derived\temporary\PUBLfemalewhite1treatments_subset		,replace
use in	1/1696	using	..\data\derived\temporary\PUBLfemalewhite2treatments	, clear
save	..\data\derived\temporary\PUBLfemalewhite2treatments_subset		,replace
use in	1/1775	using	..\data\derived\temporary\PUBLfemalewhite3treatments	, clear
save	..\data\derived\temporary\PUBLfemalewhite3treatments_subset		,replace
use in	1/2461	using	..\data\derived\temporary\PUBLfemalewhite4treatments	, clear
save	..\data\derived\temporary\PUBLfemalewhite4treatments_subset		,replace
use in	1/3174	using	..\data\derived\temporary\PUBLfemalewhite5treatments	, clear
save	..\data\derived\temporary\PUBLfemalewhite5treatments_subset		,replace
use in	1/1104	using	..\data\derived\temporary\PUBLfemalewhite6treatments	, clear
save	..\data\derived\temporary\PUBLfemalewhite6treatments_subset		,replace
use in	1/3271	using	..\data\derived\temporary\PUBLfemalewhite7treatments	, clear
save	..\data\derived\temporary\PUBLfemalewhite7treatments_subset		,replace
use in	1/1806	using	..\data\derived\temporary\PUBLfemalewhite8treatments	, clear
save	..\data\derived\temporary\PUBLfemalewhite8treatments_subset		,replace
use in	1/1203	using	..\data\derived\temporary\PUBLfemalewhite9treatments	, clear
save	..\data\derived\temporary\PUBLfemalewhite9treatments_subset		,replace
use in	1/344	using	..\data\derived\temporary\PUBLmaleasian1treatments	, clear
save	..\data\derived\temporary\PUBLmaleasian1treatments_subset		,replace
use in	1/118	using	..\data\derived\temporary\PUBLmaleasian2treatments	, clear
save	..\data\derived\temporary\PUBLmaleasian2treatments_subset		,replace
use in	1/124	using	..\data\derived\temporary\PUBLmaleasian3treatments	, clear
save	..\data\derived\temporary\PUBLmaleasian3treatments_subset		,replace
use in	1/106	using	..\data\derived\temporary\PUBLmaleasian4treatments	, clear
save	..\data\derived\temporary\PUBLmaleasian4treatments_subset		,replace
use in	1/249	using	..\data\derived\temporary\PUBLmaleasian5treatments	, clear
save	..\data\derived\temporary\PUBLmaleasian5treatments_subset		,replace
use in	1/55	using	..\data\derived\temporary\PUBLmaleasian6treatments	, clear
save	..\data\derived\temporary\PUBLmaleasian6treatments_subset		,replace
use in	1/136	using	..\data\derived\temporary\PUBLmaleasian7treatments	, clear
save	..\data\derived\temporary\PUBLmaleasian7treatments_subset		,replace
use in	1/189	using	..\data\derived\temporary\PUBLmaleasian8treatments	, clear
save	..\data\derived\temporary\PUBLmaleasian8treatments_subset		,replace
use in	1/67	using	..\data\derived\temporary\PUBLmaleasian9treatments	, clear
save	..\data\derived\temporary\PUBLmaleasian9treatments_subset		,replace
use in	1/749	using	..\data\derived\temporary\PUBLmaleblack1treatments	, clear
save	..\data\derived\temporary\PUBLmaleblack1treatments_subset		,replace
use in	1/465	using	..\data\derived\temporary\PUBLmaleblack2treatments	, clear
save	..\data\derived\temporary\PUBLmaleblack2treatments_subset		,replace
use in	1/520	using	..\data\derived\temporary\PUBLmaleblack3treatments	, clear
save	..\data\derived\temporary\PUBLmaleblack3treatments_subset		,replace
use in	1/788	using	..\data\derived\temporary\PUBLmaleblack4treatments	, clear
save	..\data\derived\temporary\PUBLmaleblack4treatments_subset		,replace
use in	1/957	using	..\data\derived\temporary\PUBLmaleblack5treatments	, clear
save	..\data\derived\temporary\PUBLmaleblack5treatments_subset		,replace
use in	1/712	using	..\data\derived\temporary\PUBLmaleblack6treatments	, clear
save	..\data\derived\temporary\PUBLmaleblack6treatments_subset		,replace
use in	1/1285	using	..\data\derived\temporary\PUBLmaleblack7treatments	, clear
save	..\data\derived\temporary\PUBLmaleblack7treatments_subset		,replace
use in	1/485	using	..\data\derived\temporary\PUBLmaleblack8treatments	, clear
save	..\data\derived\temporary\PUBLmaleblack8treatments_subset		,replace
use in	1/219	using	..\data\derived\temporary\PUBLmaleblack9treatments	, clear
save	..\data\derived\temporary\PUBLmaleblack9treatments_subset		,replace
use in	1/684	using	..\data\derived\temporary\PUBLmalehispanic1treatments	, clear
save	..\data\derived\temporary\PUBLmalehispanic1treatments_subset	,replace
use in	1/164	using	..\data\derived\temporary\PUBLmalehispanic2treatments	, clear
save	..\data\derived\temporary\PUBLmalehispanic2treatments_subset	,replace
use in	1/60	using	..\data\derived\temporary\PUBLmalehispanic3treatments	, clear
save	..\data\derived\temporary\PUBLmalehispanic3treatments_subset	,replace
use in	1/446	using	..\data\derived\temporary\PUBLmalehispanic4treatments	, clear
save	..\data\derived\temporary\PUBLmalehispanic4treatments_subset	,replace
use in	1/158	using	..\data\derived\temporary\PUBLmalehispanic5treatments	, clear
save	..\data\derived\temporary\PUBLmalehispanic5treatments_subset	,replace
use in	1/17	using	..\data\derived\temporary\PUBLmalehispanic6treatments	, clear
save	..\data\derived\temporary\PUBLmalehispanic6treatments_subset	,replace
use in	1/161	using	..\data\derived\temporary\PUBLmalehispanic7treatments	, clear
save	..\data\derived\temporary\PUBLmalehispanic7treatments_subset	,replace
use in	1/265	using	..\data\derived\temporary\PUBLmalehispanic8treatments	, clear
save	..\data\derived\temporary\PUBLmalehispanic8treatments_subset	,replace
use in	1/80	using	..\data\derived\temporary\PUBLmalehispanic9treatments	, clear
save	..\data\derived\temporary\PUBLmalehispanic9treatments_subset	,replace
use in	1/2103	using	..\data\derived\temporary\PUBLmalewhite1treatments	, clear
save	..\data\derived\temporary\PUBLmalewhite1treatments_subset		,replace
use in	1/1463	using	..\data\derived\temporary\PUBLmalewhite2treatments	, clear
save	..\data\derived\temporary\PUBLmalewhite2treatments_subset		,replace
use in	1/2113	using	..\data\derived\temporary\PUBLmalewhite3treatments	, clear
save	..\data\derived\temporary\PUBLmalewhite3treatments_subset		,replace
use in	1/1519	using	..\data\derived\temporary\PUBLmalewhite4treatments	, clear
save	..\data\derived\temporary\PUBLmalewhite4treatments_subset		,replace
use in	1/3400	using	..\data\derived\temporary\PUBLmalewhite5treatments	, clear
save	..\data\derived\temporary\PUBLmalewhite5treatments_subset		,replace
use in	1/1091	using	..\data\derived\temporary\PUBLmalewhite6treatments	, clear
save	..\data\derived\temporary\PUBLmalewhite6treatments_subset		,replace
use in	1/2234	using	..\data\derived\temporary\PUBLmalewhite7treatments	, clear
save	..\data\derived\temporary\PUBLmalewhite7treatments_subset		,replace
use in	1/2286	using	..\data\derived\temporary\PUBLmalewhite8treatments	, clear
save	..\data\derived\temporary\PUBLmalewhite8treatments_subset		,replace
use in	1/1074	using	..\data\derived\temporary\PUBLmalewhite9treatments	, clear
save	..\data\derived\temporary\PUBLmalewhite9treatments_subset		,replace
"""

# Convert multi-line string to list of lines
lines = lines.strip().split('\n')

# Function to remove the specified path
def remove_path(lines, path):
    updated_lines = []
    for line in lines:
        updated_line = line.replace(path, "")
        updated_lines.append(updated_line)
    return updated_lines

# Path to remove (raw string to avoid escaping backslashes)
path_to_remove = "..\data\derived\temporary\\"

# Removing the path from the lines
updated_lines = remove_path(lines, path_to_remove)

# Print the updated lines
for line in updated_lines:
    print(line)
