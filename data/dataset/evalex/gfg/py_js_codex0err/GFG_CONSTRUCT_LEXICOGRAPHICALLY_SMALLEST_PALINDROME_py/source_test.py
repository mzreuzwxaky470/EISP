def test():
  "--- test function ---"
  param =[(['A', 'B', 'C', 'G', 'I', 'L', 'L', 'O', 'O', 'P', 'Q', 'S', 'W', 'Y', 'c', 'd', 'e', 'f', 'f', 'i', 'm', 'm', 'o', 'q', 'v', 'w', 'x', 'x', 'y', 'z'], 27,),(['3', '2', '3', '6', '8', '9', '0', '5', '0', '5', '8', '7', '9', '0', '3', '6', '9', '6', '2', '4', '2', '3', '1', '2', '7', '9', '1', '8', '8', '7', '1', '1', '6', '1'], 30,),(['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], 27,),(['z', 'v', 'B', 'Y', 'n', 'K', 'h', 'C', 'T', 'L', 'g'], 7,),(['1', '2', '5', '6', '7'], 4,),(['0', '0', '1', '0'], 3,),(['D', 'n', 'r'], 1,),(['0', '9', '9', '1', '2', '1', '5', '3', '7', '5', '9', '2', '4', '4', '8', '9', '6', '4', '2', '8', '8', '5', '5', '7', '1', '7', '6', '2', '2', '2', '3', '3', '7', '9'], 24,),(['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], 21,),(['E', 's', 'I', 'S', 'h', 'H', 'i', 'm', 'v', 'B'], 6,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
#TESTED_PROGRAM"-----------------"
test()
