
#ref: https://www.javadrive.jp/python/string/index24.html

def main():
    print("My name is {0}, age is {1}, address is {2}".format("Yamada", 18, "Tokyo"))
    print("My name is {myname}, age is {myold}".format(myname="Ueda", myold=23))
    print("Number1={:d}, Number2={:e}, Number3={:f}".format(10, 0.002, 51.3))


if __name__ == "__main__":
    main()