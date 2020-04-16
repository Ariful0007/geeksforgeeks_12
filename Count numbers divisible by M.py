for _ in range(int(input())):
    a= int(input())
    b= int(input())
    m=int(input())
    count=0
    for i in range(a,b+1):
        if i%m==0:
            count=count+1

    print(count)


if __name__ == '__main__':
        pass
