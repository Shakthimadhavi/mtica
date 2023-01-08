import sys
print("Coming through stdout")
save_stdout = sys.stdout
fh = open(r"d:\pythonpractice55\day17\test.txt","w")
sys.stdout = fh
print("This line goes to test.txt")
print(input())
sys.stdout = save_stdout
fh.close()
