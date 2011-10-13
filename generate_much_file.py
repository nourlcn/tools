
def main():
    for i in range(1000000):
        f = file('./testfile/'+str(i),'w')
        f.write("test content")
        f.close()

if __name__ == "__main__":
    main()
