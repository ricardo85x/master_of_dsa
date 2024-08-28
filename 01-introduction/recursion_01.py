def fun(i):
    if i > 3:
        return
    print(i)
    fun(i + 1)
    print("End of call where i = ", i)
    return
fun(1)