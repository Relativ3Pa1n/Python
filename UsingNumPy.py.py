import numpy as np

def zer_fun():
    print("NOTE: np.zeros function to create an array with 0 as the values\n")
    zer = np.zeros((3, 4), dtype=int)
    print("[+]This is the \'np.zeros((3, 4), dtype=int\' function\n\n", zer, "\n")
def ones_fun():
    print("NOTE: np.ones function to create an array with 1 as the values\n")
    one = np.ones((3, 4))
    print("[+]This is the \'np.ones((3, 4))\' function\n\n", one, "\n")
def ful_fun():
    print("NOTE: np.full function creates an arry with the value you inputed as a constant\n")
    ful = np.full((4, 3), 5)
    print("[+]This is the \'np.full((4, 3), 5)\' function\n\n", ful, "\n")
def eye_fun():
    print("NOTE: np.eye function creates and identity matrix from linear algebra\n")
    print("NOTE: this puts a number along the diagonal of the array\n")
    eye = np.eye((5))
    print("[+]This is the \'np.eye((5))\' function\n\n", eye, "\n")
def dia_fun():
    print("NOTE: np.diag function will create an aaray with values on the diagonal\n")
    dia = np.diag([10, 20, 30, 50])
    print("[+]This is the \'np.diag([10, 20, 30, 50])\' function\n\n", dia, "\n")
def ara_fun():
    print("NOTE: np.arange function that creates a one dimensional array with a Start, Stop and Step\n")
    ara = np.arange(10)
    ara2 = np.arange(4, 10)
    ara3 = np.arange(1, 14, 3)
    print("[+]This is the \'np.arange(10)\' function\n\n", ara, "\n")
    print("[+]This is the \'np.arange(4, 10)\' function\n\n", ara2, "\n")
    print("[+]This is the \'np.arange(1, 14, 3)\' function\n\n", ara3, "\n")
def lin_fun():
    print("NOTE: np.linspace function is like arange but requires Start, Stop and n. np.\ninspace uses floating point values and n = the evenly spaced numbers\nwe can exlude the endpoint with endpoint=False\n")
    lin = np.linspace(0, 25)
    lin2 = np.linspace(0, 25, 5)
    lin3 = np.linspace(0, 25, 10, endpoint=False)
    print("[+]This is the \'np.linspace(0,25)\' function(defaults to n=50)\n\n", lin, "\n")
    print("[+]This is the \'np.linspace(0, 25, 5)\' function (using n=5)\n\n", lin2, "\n")
    print("[+]This is the \'np.linspace(0, 25, 10, endpoint=False)\' function\n\n", lin3, "\n")
def res_fun():
    print("NOTE: np.reshape function will reshape a 1D array to a 2D array as long as the x,y is equal\nso an array of 20 elements would divide equally into a 2x10 or a 4x5 2D array\n")
    res_array = np.arange(20)
    res = np.reshape(res_array, (10, 2))
    res2 = np.reshape(res_array, (5, 4))
    print("[+]This is the \'np.reshape(res_array, (10, 2))\' function\nExample array is np.arange(20)\n", res, "\n")
    print("[+]This is the \'np.reshape(res_array, (5, 4))\' function\nExample array is np.arange(20)\n", res2, "\n")
def met_fun():
    print("NOTE: np.reshape is also a method that can be used with linspace() and arange()\n")
    met = np.arange(20).reshape((10, 2))
    met2 = np.linspace(0, 50, 10, endpoint=False).reshape(5, 2)
    print("[+]This is the \'np.arange(20).reshape((10, 2))\' method one liner\n", met, "\n")
    print("[+]This is the \'np.linspace(0, 50, 10, endpoint=False).reshape(5, 2)\' method one liner\n", met2, "\n")
def ran_fun():
    print("NOTE: np.random.random() creates an array of a given shape with random floats\n")
    ran = np.random.random((3, 3))
    print("[+]This is the \'np.random.random((3, 3))\' function\n", ran, "\n")
def rand_fun():
    print("np.random.randint() creates a random set of integers with a specifc Start and End, with endbeing exluded.\nnp.random.normal() Satisfies a certain statistical property, when you want numbers to be close to the average of 0.\nGiven shape with random numbers picked from a normal distribution with a given mean and standard deviation.\nWe are creating a 1000x1000 array of random floats drawn from a normal distribution with the mean of 0 and a standard deviation of 0.1\n\n")

    print("Standard Deviation: measure of the amount of variation(0.1)\nMean: A calculated central value, the average of the numbers\nNormal Distribution: continuous probability distribution that is symmetrical around its mean, example: a Bell Curve, so their would be more points closer to the mean.(1)\n")
    rand = np.random.randint(4, 15, (3, 2))
    rand2 = np.random.normal(0, 0.1, size=(1000, 1000))
    print("[+]This is the \'np.random.randit(4, 15, (3, 2))\' function\n", rand, "\n")
    print("[+]This is the \'np.random.normal(0, 0.1, size=(1000, 1000))\' function\n", rand2, "\n")
def ope_fun():
    print("NOTE: np.OPERATOR is a way to use operators as a method with numpy we can use a few to get more data out of our 1000x1000 array in \"operators\"\n")
    operators = np.random.normal(0, 0.1, size=(1000, 1000))
    print("mean, operators.mean(): ", operators.mean())
    print("std, oprerators.std(): ", operators.std())
    print("max, operators.max(): ", operators.max())
    print("min, operators.min(): ", operators.min())
    print("# of positive, (operators > 0).sum()): ", (operators > 0).sum())
    print("# of negative, (operators < 0).sum()): ", (operators < 0).sum())

while True:
    try:
        print("[!] List of Functions and Methods:\n- np.zeros\n- np.ones\n- np.full\n- np.eye\n- np.diag\n- np.arange\n- np.linspace\n- np.reshape\n- .np.reshape (method)\n- np.random.random\n- np.random.other\n- np.operators\n\n or \'exit\'")
        query = input("[?] Which Function above would you like to see?\n")
        if query == "np.zeros":
            print("____________")
            zer_fun()
            print("____________")
        if query == "np.ones":
            print("____________")
            ones_fun()
            print("____________")
        if query == "np.full":
            print("____________")
            ful_fun()
            print("____________")
        if query == "np.eye":
            print("____________")
            eye_fun()
            print("____________")
        if query == "np.diag":
            print("____________")
            dia_fun()
            print("____________")
        if query == "np.arange":
            print("____________")
            ara_fun()
            print("____________")
        if query == "np.linspace":
            print("____________")
            lin_fun()
            print("____________")
        if query == "np.reshape":
            print("____________")
            res_fun()
            print("____________")
        if query == ".np.reshape":
            print("____________")
            met_fun()
            print("____________")
        if query == "np.random.random":
            print("____________")
            ran_fun()
            print("____________")
        if query == "np.random.other":
            print("____________")
            rand_fun()
            print("____________")
        if query == "np.operators":
            print("____________")
            ope_fun()
            print("____________")
        if query == "exit":
            break

    except KeyboardInterrupt:
        print("\nExiting")
        break

