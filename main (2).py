def fac(no):
  if no == 0 or no == 1:
    return 1
  else:
    return no * fac(no - 1)


s = int(input("Enter a number:"))
print(s, "factorial is", fac(s))
