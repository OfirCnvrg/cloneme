import os

def a():
  print("hello2")
  filename = "output/myawesomeoutput.txt"
  os.makedirs(os.path.dirname(filename), exist_ok=True)
  with open(filename, "w") as file:
    file.write("This is a nice artifact")
    
a()
