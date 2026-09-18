s1 = input("Enter string 1 :-")
s2 = input("Enter string 2 :-")
if s1 == s2:
  print("Both the strings are same")
elif s2 in s1:
  print(s2,"is a substring of",s1)
else:
  print("They are not same")
