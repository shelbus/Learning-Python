states_of_America = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_America[49])
#States are in order of when they joined the Union, initially, and later the United States.
#[brackets] are always used for lists as well as the index/offset (aka the number on the list, starting from 0). You can also use [-1] to start from the end of the list.
#You can also alter the item indexed by selecting with [#] =

states_of_America.append("Shelbyland")
print(states_of_America)
#Lots of other functions available for lists using .function
#Examples include append, extend, insert, remove, pop, clear, index. Some will use () and others will use []

print(len(states_of_America))
#IndexError: list index out of range means we tried to select/use something outside the range we have. Ex, trying to print state#50 when there is no state #50 since we start at 0.

num_of_states = len(states_of_America)
print(states_of_America[num_of_states -1])