quetions = [
  "who is invented computer",
]

answers = [
  "(A)John Logie Baird     (B)Vint Cerf\n(C)Johann Zahn         (D)Charles Babbage\n"
]

cnt = []
rightAnswer = ["D"]

for i in quetions:
  print((i))
  for an in answers:
    print((an))
    x = input("Enter your choose   ")
    a = x.upper()
  for ra in rightAnswer:
    if (a == (ra)):
      cnt.append("1")
      print("sahi jabab")
      break
    else:
      print("yha aapka galat jabab hai manyavar")
      cnt.pop()
      break

prize = cnt.count("1")
if (prize == 1):
  print("Congratulations, You won 10 Rupees.")
if (prize == 2):
  print("Congratulations, You won 20 Rupees.")
if (prize == 2):
  print("Congratulations, You won 40 Rupees.")
