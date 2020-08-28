from getch import _Getch

def get():
    inkey = _Getch()
    while(1):
            k=inkey()
            if k!='':break
    print('you pressed' + str(k))

def main():
    for i in range(0,25):
        get()

if __name__=='__main__':
    main()