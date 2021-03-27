list_tobe_checked = ["a", 0.2]

for i in list_tobe_checked:
    print("The current entry of the list", i)
    
    try:
        print("The reciprocal of",i,"is", 1/i)
    except:
        print("Oops! For", i, "we cannot calculate reciprocal")