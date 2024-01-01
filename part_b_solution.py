# the function undoom dice will arrange i.e will fill the doomed spots on the faces of dice

def undoom_dice(DiceA, DiceB):
    
    # this function is used to return all possible combination sum values for both dies 
    def combination_sums(DiceA, DiceB):
      
        sums_val=[]
        A = DiceA
        B = DiceB
        for i in A:
          for j in B:
            sums_val.append(i+j)
        sums_val = sorted(sums_val)
        return sums_val
        
    #this function will return all possible combinations of face values to the dies to maitain the sum probability and also
    #returns the all possible pairs i.e face value pairs for both dies

    def poss_combinations():

        all_combi = [[1, x, y, z, i, j] for x in range(2, 9) for y in range(x, 9) for z in range(y, 9) for i in range(z, 9) for j in range(i, 9)]
        all_pairs=[]
        for i in all_combi:
          for j in all_combi:
            if(i<=j):
              all_pairs.append((i,j))
        return all_pairs
        
    #this part of code returns the pair that maintains the same probability like the original pairs
    original_pairs = DiceA, DiceB
    original_sums = combination_sums(DiceA, DiceB)
    new_pair=[]
    possible_pairs=poss_combinations()
    for (A,B) in possible_pairs:
      if (combination_sums(A,B) == original_sums) and (A,B) != original_pairs:
        new_pair.append((A,B))
    return new_pair
    
    
# code execution starts from here  
DiceA = [1,2,3,4,5,6]
DiceB = [1,2,3,4,5,6]
New_config=undoom_dice(DiceA, DiceB)
New_DiceA=New_config[0][0]
New_DiceB=New_config[0][1]
print("new configurations for dice A is - ", New_DiceA)
print("new configurations for dice B is - ", New_DiceB)