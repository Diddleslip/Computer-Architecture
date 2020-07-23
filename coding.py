# Write an algo that will take in an object, the obj will only have str and int as values.
# Grab the sum of all the ints in the values and objs.

# def function(object):
#     sum = 0
#     for i in object.values():
#         if isinstance(i, int):
#             sum += i

#     return sum


# print(function({  
#   "cat": "bob",
#   "dog": 23,
#   19: 18,
#   90: "fish"
# }))

# def reverse(string):
#   str = [ord(c) for c in string]
#   reversed_string = list()
#   newString = []
#   counter = -1
#   for _ in str:
#     reversed_string.append(str[counter])
#     counter -= 1

#   for i in reversed_string:
#     newString.append(chr(i))

#   return "".join(newString)

# print(reverse("school"))

keyTimes = [[0, 3], [20, 5], [2, 6], [15, 7], [9, 8], [19, 9], [24, 10], [4, 12], [3, 13]]
    
def getLongestTime(keyTimes):
  array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  highscore = list()
  saved = list()
  for i, v in enumerate(keyTimes):
    if i == 0:
      saved = [v[0], v[1]]
    if len(v) > 1:
      if i != 0:
        if len(highscore) == 0:
          highscore = [v[0], v[1], (v[1] - keyTimes[i - 1][1])]
        elif (v[1] - keyTimes[i-1][1]) > highscore[2]:
          highscore = [v[0], v[1], (v[1] - keyTimes[i - 1][1])]
  
  # Edge case
  if saved[1] > highscore[2]:
    highscore = [saved[0], saved[1]]

  return array[highscore[0]]

print(getLongestTime(keyTimes))