import random
text = ""
stringthing = ""
common = ["a","e","i","o","u"]
options = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
p = random.choice(options.copy())
q = random.choice(common.copy())
space = 26
rarity = 60
for foob in range(random.randint(4,8)):
  p = random.choice(options.copy())
  q = random.choice(common.copy())
  stringthing = stringthing+str(random.choice([p,q]))
print("## the", stringthing, "poem")
print("")
for totalfoob in range(random.randint(4, 6)):
    for foob in range(random.choice([4,4,4,5])):
        while len(text) < random.randint(16, 24):
          p = random.choice(options.copy())
          q = random.choice(common.copy())
          if len(text) < 1 or text[len(text)-1] == " ":
            letter = str(random.choice([p,q]))
          else:
            randint = random.randint(1,100)
            if randint <= space:
              letter = " "
            else:
              letter = str(random.choice([p,q]))
          text = (text+letter)
        print(text)
        text = ""
    print(" ")