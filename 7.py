def tree(height):
    length=height*2-1
    stars = 1
    for i in range(1,height+1):
        print(("*"*stars).center(length))
        stars = stars + 2
       # print("*".center(length))

tree(8)
