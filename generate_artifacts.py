for i in range(10500):
    with open("/output/file_no_{}".format(i), "w") as f:
        f.write(str(i))
