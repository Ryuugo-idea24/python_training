
def main():
    num1 = 30
    print("decimal %d, hexadecimal %x." % (num1, num1))

    name = "Suzuki"
    age = 18
    print("Name is %-8s. Age is %03d." % (name, age))

    flt = 0.0752
    print("exponent %e. float=%f." % (flt, flt))
    
if __name__ == "__main__":
    main()