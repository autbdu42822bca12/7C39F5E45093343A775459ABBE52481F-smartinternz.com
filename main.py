#implement a recursive function to calculate the factorial  of a given number.


def fac(no):
  if no == 0:
    return 1
  else:
    return no * fac(no - 1)


number = int(input("enter the number:"))
res = fac(number)

print("the factorial of {} is {}".format(number, res))
