tuples_list = [(1, 7), (1, 3), (3, 4, 0), (2, 2)]

def sort_last(tuples_list):
  return sorted(tuples_list, key=lambda tuples_list:tuples_list[-1])

#Run the program as sort_last(tuples)
