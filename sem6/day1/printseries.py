#!/usr/bin/env python3

def ascending(start, end, step):
    for i in range(start, end + 1, step):
        print(i)

def descending(start, end, step):
    for i in range(start, end - 1, -step):
        print(i)

def main():
    print("Enter start, end, step:")
    try:
        start, end, step = map(int, input().split())
        if step <= 0:
            print("Step must be a positive integer")
            return
            
        if start > end:
            descending(start, end, step)
        else:
            ascending(start, end, step)
    except ValueError:
        print("Please enter valid integers")

if __name__ == "__main__":
    main()
