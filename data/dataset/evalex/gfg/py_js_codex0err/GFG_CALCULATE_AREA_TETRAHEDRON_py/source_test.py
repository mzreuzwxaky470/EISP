def test():
  "--- test function ---"
  param =[(58,),(56,),(35,),(99,),(13,),(45,),(40,),(92,),(7,),(13,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
#TESTED_PROGRAM"-----------------"
test()
