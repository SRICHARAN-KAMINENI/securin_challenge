#part-A

diceA=[1,2,3,4,5,6]
diceB=[1,2,3,4,5,6]

# question 1
# total no of combinations = len(diceA)  * len(diceB) i.e 6x6


combinations=len(diceA)*len(diceB)
print("printting the no of combinations")
print(combinations)

# question 2
# distribution of all possible combinations

poss_combinations={}
for i in range(1,7):
  for j in range(1,7):
    if (i,j) not in poss_combinations:
      poss_combinations[(i,j)]=1
    else:
      poss_combinations[(i,j)]+=1
print("printing the distribution of all possible combinations")

for i in poss_combinations.items():
  print(i)

#question 3
#probability of all possible combination sums

possible_sums={}
for i in poss_combinations:
  if(sum(i)) not in possible_sums:
    possible_sums[sum(i)]=1
  else:
    possible_sums[sum(i)]+=1

    
probability={}
for i in possible_sums:
  probability[i]=possible_sums[i]/combinations
print("printing the Probability of all Possible Sums occurring")  
for i in probability.items():
  print(i)




 