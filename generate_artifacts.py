for i in range(10500):
    with open("output/exp_file_no_{}".format(i), "w") as f:
        f.write(str(i))
