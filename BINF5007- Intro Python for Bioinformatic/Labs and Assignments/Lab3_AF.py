"""
Instruct user how to prepare a 3 ml solution of
10 mM NaCl and 0.5 mM MgCl2, given stock solutions
of 1 M NaCl and 0.1 M MgCl2.
"""
"""Business logic"""
try :
    final_vol = int(input("Please enter the final volume (ml): "))
    # NaCl
    nacl_stock = int(input("Please input the stock concentration of NaCl (mM): "))  # use mM concentrations throughout the program
    nacl_final = int(input("Please enter the final concentration of NaCl (mM)"))
    # concatenation, notice how we are calculating something here!
    step1 = "Add " + str(final_vol * (nacl_final / nacl_stock)) + " ml NaCl\n"
    # MgCl2
    mg_stock = int(input("Please input the stock concentration of MgCl2 (mM): "))
    mg_final = int(input("Please enter the final concentration of MgCl2 (mM)"))
    step2 = "Add " + str(final_vol * (mg_final / mg_stock)) + " ml MgCl2\n"
    # Water
    step3 = "Add water to a final volume of " + str(final_vol) + " ml and mix"
    # Protocol, we can then just print things out b/c they have been formatted earlier
    print(step1 + step2 + step3)
except ValueError:
    print("Input does not have a value or is not numeric")     
except ZeroDivisionError:
    print("Stock concentration cannot be 0")