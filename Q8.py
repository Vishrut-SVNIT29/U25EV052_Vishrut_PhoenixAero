#Q8 Restricted Airspace Conflict Checker 

planned_zones = {"Z1", "Z2", "Z3", "Z5", "Z7"}
restricted_zones = {"Z3", "Z5", "Z6", "Z8"}
cleared_zones = {"Z1", "Z2", "Z3", "Z4", "Z5", "Z6", "Z7", "Z8"}

#restricted planned zones
print("Restricted Planned Zones:")
print(planned_zones.intersection(restricted_zones))
#safe zones
print("\nSafe Zones:")
print(planned_zones.difference(restricted_zones))
#symmetric difference
print("\nEither planned or restricted but not both:")
print(planned_zones.symmetric_difference(restricted_zones))

#subset check
if planned_zones.issubset(cleared_zones):
    print("\nAll planned zones are cleared.")
else:
    print("\nSome planned zones are not cleared.")

#modifying planned zones
planned_zones.add("Z9")
planned_zones.remove("Z7")
print("\nUpdated Planned Zones:")
print(planned_zones)

#total unqiue zones
all_zones = planned_zones.union(restricted_zones)
print("\nTotal Unique Zones:",len(all_zones))