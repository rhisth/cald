from sys import exit
from cald import getday

def main():
    while True:
        try:
            answer = input("Айди дня: ")
            year = int(input("Год: "))
            day = getday(answer, year)
            print(day[0], day[1], sep="\n")
        except KeyboardInterrupt: exit()
        except Exception as ex: print(ex)

if __name__ == "__main__":
    main()