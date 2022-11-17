def main ():

    a = input("a: ")

    try:
        b = int(a)
        print(b)
    except:
        print("Not a number!")

    print("All done!")

if __name__ == "__main__":
    main()

