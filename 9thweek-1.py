import os

# fp = "temp.txt"
# # fp = "temp1.txt"

# # file = open(fp, "w")

# if os.path.exists(fp):
#     f = open(fp, "r")
#     for line in f: 
#         print(line)
#     # print("ok")
# else :
#     f = open(fp, "w")
#     for i in range(100):
#         f.write(str(i) + "\n")
#     # print("error")
    
# f.close()


# fp = "new.txt"

# f = open(fp, "w")
# f.close()

# os.remove(fp)
# print("complete")

# def dir_print(p):
#     files = os.listdir(p)
#     for f in files:
#         print(f)
        
# fp = "new.txt"

# f = open(fp, "w")
# f.close()

# dir_print("./")

# os.remove(fp)
# print("----------------------\n\n")
# dir_print("./")

# fp = "new.txt"

# f = open(fp, "w")
# f.close()

# os.rename(fp, "new1.txt")
# print("complete")

# fp = "new.txt"
# tp = "new1.txt"

# f = open(fp, "w")
# f.close()

# if os.path.exists(tp) :
#     print("exist, same name file")
#     os.remove(tp)
# else :
#     os.rename(fp,"new1.txt")
#     print("complete")


def dir_print(p):
    files = os.listdir(p)
    for f in files :
        print(f)
        
fp = "new.txt"
tp = "new1.txt"

f = open(fp, "w")
f.close()

dir_print("./")
print("\n----------------------------------------\n\n")
if os.path.exists(tp) :
    os.remove(tp)
    dir_print("./")
    print("exist, same name file")
else :
    os.rename(fp, "new1.txt")
    dir_print("./")
    print("complete")
