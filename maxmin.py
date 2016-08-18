# function taking a list as an argument
def find_max_min(numbers):
  # finding the minimum number in the list
  minimum = min(numbers)
  # finding the maximum number in the list
  maximum = max(numbers)
  if minimum == maximum:
    return [len(numbers)]
  else:
    return [minimum, maximum]