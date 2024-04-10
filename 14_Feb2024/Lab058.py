def make_pizza(*topings):
            #for toping in topings:
     print(topings)
     for item in topings:
         print(item)
sherine = make_pizza("Paneer","Sweet corn"," Onion")
royce = make_pizza("Tomato","paneer","capsicum","butter")
Riyan = make_pizza("Cheese","butter")


def make_pizza_base(* topings, base):  # * multiple arguments   , if base = "Wheat" in the function , then default will be wheat
    print(*topings,base)
    for item in topings,base:
        print(item)

make_pizza_base("Paneer","Sweet corn"," Onion", base = "thin")
make_pizza_base("Tomato","paneer","capsicum","butter", base = "hard")


# def make_pizza_base(* topings, * base): # Mutliple parameters not allowed

def make_pizza_return(*topings, base ="wheat"):
    print("******************")
    print(topings,base)
    for item in topings,base:
        print(item)
    return topings,base    # can return multiple by comma seperated

sherine_t,sherine_b = make_pizza_return("Paneer","tomato","Onion", base="thin")
Kids = make_pizza_return("Paneer","tomato","sweet corn")
print("Sherine's topings:",sherine_t)
print("sherine's base:",sherine_b)

