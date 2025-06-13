# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of builtin data types)

# yeah 9 and 9.0 dono ka matlab same hai 9 but 9.3 and 9 ka matlab alag hai isliye python isse same value samajhta hai
# to isse set me normally store nahi krr payenge kyuki set unique value ko store krta hai

num1 = int(9)
num2 = float(9.0)

# inn dono ke help se set me store krr skte hai
my_set = (num1,num2)
print(my_set)