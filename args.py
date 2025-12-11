def yigindi(*son):

    jami = 0
    for son in son:
        jami += son
    return jami

print(yigindi(1, 2, 3, 10, 100, 1000))