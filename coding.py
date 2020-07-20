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

def reverse(string):
  str = [ord(c) for c in string]
  reversed_string = list()
  newString = []
  counter = -1
  for _ in str:
    reversed_string.append(str[counter])
    counter -= 1

  for i in reversed_string:
    newString.append(chr(i))

  return "".join(newString)

print(reverse("school"))