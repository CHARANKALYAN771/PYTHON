##################### file handling in txt files: ##############################

# # READ:
# f=open('intro.txt','r')
# ck=f.read()
# c=ck.split()
# c.insert(0,"myself")
# ck=' '.join(c)
# print(ck)
# f.close()

# # WRITE:
# f=open('intro.txt','w')
# ck=f.write("the king")
# print(ck)
# f.close()

# # APPEND:
# f=open('intro.txt','a')
# ck=f.write("*"*10 +'charan kalyan')
# print(ck)
# f.close()

# # READ&WRITE:
# f=open("intro.txt",'r+')
# ck=f.read()
# print(ck+"1")
# ck=f.write("   new funct  ")
# print(ck)
# ck=f.read()
# print(ck)
# f.close()

# # READLINE&READLINES:
# f=open("intro.txt",'r')
# ck=f.readline()
# ck=f.readlines()
# print(ck)
# f.close()

# # WRITELINE&WRITELINES:
# f=open("intro.txt",'a')
# ck=f.writelines("bsudygBYUgeHEVDwevftyuVJCUkv,chbSJHDvbuiyGS.HBCHUshVDUSIRGFuSHBvuhuiHS")
# f.close()

# # TELL()&SEEK():
# f=open("intro.txt",'r')
# f.read(23)
# print(f.tell())
# f.seek(20)
# print(f.tell())
# f.close()


############################## IN PDF FILES #######################################

# f=open("pics\\test.pdf",'r+')
# ck=f.read()
# print(ck)
# f.write(" something: ")
# ck=f.read()
# print(ck)
# f.close()

############################## IN XLS FILES #######################

# f=open("test1.xls",'r+')
# ck=f.read(100)
# print(ck)
# f.write(" charan kalyan ")
# print(ck)
# f.close()








