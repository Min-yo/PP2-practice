
def gr_to_ounc():
    gramm = int(input())
    return 28.3495231 * gramm
def f_to_c():
    f = float(input())
    return (5 / 9) * (f - 32)

print("Want to transate mass or degrees? ")
o = input()
if o  == "mass":
    print(gr_to_ounc())
elif o == "degrees":
    print(f_to_c())