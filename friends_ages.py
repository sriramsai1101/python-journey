friends={
    "eshwar":20,
    "rakesh":22,
    "yeshwanth":19,
    "harsha":18,
    "shanthi":25
}
for key,value in friends.items():
    print(key,"-->",value)
    #oldest
oldest=max(friends,key=friends.get)
print("oldestfriend =", oldest)
