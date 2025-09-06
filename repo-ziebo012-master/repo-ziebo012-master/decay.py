init = float(input("Initial Amount: "))
halflife = float(input("Half-Life: "))
time = float(input("Elapsed Time: "))
residual = init*0.5**(time/halflife)
print("Residual amount remaining =",residual)

print("hello world!")
