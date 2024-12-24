friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}


#friends - abroad = rolf
local_friends = friends.difference(abroad)

#abroad - friends = empty
outer_friends = abroad.difference(friends)

#total uniq friends
total_friends = local_friends.union(abroad)

print(local_friends)
print(outer_friends)
print(total_friends)




#intersection for both sets
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both_studies = art.intersection(science)

print(both_studies)
