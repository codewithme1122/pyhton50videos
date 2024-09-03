a = open('myfile.txt', 'r')
while True:
  i = i + 1
  line = a.readline()
  print(line)
  if not line:
    break
m1 = int(line.split(",")[0])
m2 = int(line.split(",")[1])
m3 = int(line.split(",")[2])
print(f"Marks of student {i} in Maths is: {m1*2}")
print(f"Marks of student {i} in English is: {m2*2}")   
print(f"Marks of student {i} in SST is: {m3*2}")
