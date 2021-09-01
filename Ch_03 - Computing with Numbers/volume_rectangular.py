# volume_cube
#   This program finds the volume of a cube.

def main():
    print("This program is used to find the volume of a 3-dimensional, "
          "rectangular prism.")
    print()

    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))

    unit = input("What kind of units are you using? ")

    volume = length * width * height
    print()
    print("The volume of your rectangular prism is: "
          , volume, "cubic", unit)
    print()
    print("*" * 50)
    print()


for i in range(100):
    main()
