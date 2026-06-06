from modules import run

def main():
    try:
        run()
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()