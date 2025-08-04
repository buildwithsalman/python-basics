def val_list(list,idx=0):
    if (idx == len(list)):
        return 
    print(list[idx])
    val_list(list,idx+1)
cities = ["delhi","mumbai","agra","lucknow","kanpur"]
val_list(cities)