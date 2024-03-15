def PrintVignereTable():
    table = [[chr((i + j) % 26 + 65) for j in range(26)] for i in range(26)]

    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(
        "####################################################################################################################################"
    )
    print(
        "                                                             VIGNERE TABLE                                                          "
    )
    print(
        "####################################################################################################################################"
    )
    print("   ", end="")
    for i in alphabets:
        print(f"   {i} ", end="")
    print(
        "\n------------------------------------------------------------------------------------------------------------------------"
    )
    for i, row in enumerate(table):
        print(f"{alphabets[i]}  |", end="")
        for j in row:
            print(f"  {j}  ", end="")
        print("\n")
