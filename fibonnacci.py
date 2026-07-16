import tools, time  # noqa: E401


def main():
    print("***************************************************")
    print("1. Find number in place n in the Fibonacci sequence")
    print("2. Find the n Fibonacci number")
    print("3. Quit")


def fibonacci_place(n):
    if n <= 0:
        return f"{tools.ROUGE}the number must be greater than 0{tools.RESET}"
    fib1, fib2, count = 1, 1, 2
    if n == 1:
        return f"the number is at the {tools.VERT}1st or 2nd place{tools.RESET}"
    while fib2 < n:
        fib1, fib2, count = fib2, fib1 + fib2, count + 1
    if fib2 == n:
        return f"the number is at the {tools.VERT}{count}th place{tools.RESET}"
    else:
        return f"{tools.ROUGE}the number isnt in the Fibonacci sequence{tools.RESET}"


def fibonnacci_index_num(n):
    if n <= 0:
        return None
    fib1, fib2 = 1, 1
    if n == 1 or n == 2:
        return 1
    for _ in range(3, n + 1):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


if __name__ == "__main__":
    while True:
        main()
        choice = input(
            f"{tools.ROUGE}Enter your choice: {tools.RESET}\n{tools.GRAS}>>>{tools.RESET}\t"
        )
        if choice == "1":
            try:
                n = int(input("Enter a index of the Fibonacci sequence :\nPlace: "))
                result = fibonnacci_index_num(n)
                if result is None:
                    print(f"{tools.ROUGE}the index must be greater than 0{tools.RESET}")
                else:
                    print(
                        f"To the place {n} of the Fibonacci sequence there is the "
                        f"{tools.VERT}{tools.format_number(result)}{tools.RESET}"
                    )
            except ValueError:
                print(f"{tools.ROUGE}please enter a valid integer{tools.RESET}")
            input("")
            tools.clear()
        elif choice == "2":
            try:
                n = int(
                    input(
                        "Enter a number to check if he's in the sequence and at wich place:\nNumber to check:  "
                    )
                )
                print(fibonacci_place(n))
            except ValueError:
                print(f"{tools.ROUGE}please enter a valid integer{tools.RESET}")
            input("")
            tools.clear()
        elif choice == "3":
            break
        else:
            print("Invalid choice")
            tools.shutdown()

print("Thanks for your nice utilisation")
time.sleep(0.5)
tools.clear()
