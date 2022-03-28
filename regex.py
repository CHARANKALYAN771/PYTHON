import re
x="hgsdhfg namemy nareserree is shaw1n566 shaw566  shae shak shawn sahm qwer6tyuioplkj78hgfdsamnbvcxz"
y=re.search(" ",x)
if y:
    print("yes")
else:
    print("no")

y=re.findall("[a-d]",x)
print(y)

y=re.findall("\d+",x)
print(y)

y=re.findall("sh...",x)
print(y)

y=re.findall("^my",x)
print(y)
if y == []:
    print("False")
else:
    print("True")

y=re.findall("sh.*66",x)
print(y)

y= re.findall("sh..?66",x)
print(y)

y=re.findall("n.{2}e",x)
print(y)

y=re.findall("name|my",x)
print(y)

z="charan kalyan alias katam kalyan"
y=re.findall(r"\Bran",z)
print(y)

y=re.findall("[^a-n]",z)
print(y)











