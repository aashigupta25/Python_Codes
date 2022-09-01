'''File input and output'''
# f = open("this.txt", "r", encoding= "utf8")
# text = f.read()
# print(text)
# f.close()

# f = open("this.txt", "w", encoding= "utf8")
# f.write("This is nice")
# f.close()

# Open and Close File automatically
with open("this .txt", "r", encoding= "utf8") as f:
    f.read()

with open("this.txt", "w", encoding= "utf8") as f:
    f.write()
