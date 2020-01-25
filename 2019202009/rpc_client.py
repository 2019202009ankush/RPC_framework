import codegen,os
print("Welcome to rpc framework\nEnter the function you want to run\n")
d=input()
lis=d.split()
fun=lis[0]
def speak():
    print('hi\n')
try:
    c=eval(fun+'()')
except:
    codegen.gen_code(lis) #call stub generator
    import temp
    a=temp.fun(lis[1],lis[2])
    print(a)
    os.remove("temp.py")
