# union and intersection

set1 = {1,2,3,4}
set2 = {2,3,4,5}
res = set1.union(set2) # output 1,2,3,4,5  (sbb element ko print krega lekin ek barr chahe kitna nhi same element ho dono me se kisi ek ka hi print krega wo bhi ek sabb element )
print(res)

res2 = set1.intersection(set2)  # output 2,3,4 (jo jo common hai dono me wo)
print(res2)