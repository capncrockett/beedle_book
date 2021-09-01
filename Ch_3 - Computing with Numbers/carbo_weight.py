# carbo_weight
#   This program computes the molecular weight of a carbohydrate.

def main():
    print("This program computes the molecular weight of a "
          "carbohydrate given the number of atoms in the molecule.")
    print()
    h_count = float(input("Enter the number of hydrogen atoms: "))
    c_count = float(input("Enter the number of carbon atoms: "))
    o_count = float(input("Enter the number of oxygen atoms: "))
    weight = h_count * 1.00794 + c_count * 12.0107 + o_count * 15.9994
    print()
    print("Molecular weight, in grams per mole, is equal to ", weight)


main()
