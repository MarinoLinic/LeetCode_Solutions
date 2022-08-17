#0. FizzBuzz | Easy | O(1)
for i in range(100):
    out = ""

    if i % 3 == 0:
        out += "Fizz"

    if i % 5 == 0:
        out += "Buzz"

    if i % 7 == 0:
        out += "Bazz"

    # Printing
    if out == "": # JS: console.log(out || i)
        print(i)
    else:
        print(out)


# 1. Partitioning a number
def partition(n):
  if n == 1:
    return [[1]]

  result = [[n]]

  for i in range(1, n):
    a = n-i

    b = partition(i)

    for j in b:
      if j[0] <= a:   
        result.append([a] + j)

  return result

print(partition(5))