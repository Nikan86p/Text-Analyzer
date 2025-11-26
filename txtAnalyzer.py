import os, time, pyfiglet, colorama


def delete(clk):
    clk = os.system("cls" if os.name == "nt" else "clear")


def banner(srt):
    pyfiglet.print_figlet(srt, font="slant")


def colorize(srt):
    x = colorama.Fore.RED + colorama.Style.BRIGHT + srt + colorama.Style.RESET_ALL
    print(x)


def name():
    global txt
    txt = "sample.txt"
    with open(txt, "r") as file:
        n = file.name
        print(f"Your file name is {n}")


def animation(script):
    for char in script:
        print(char, end="", flush=True)
        time.sleep(0.06)


def line_len():
    line_list = []

    with open(txt, "r") as file:
        for line in file:
            line_list.append(line.strip())

    txt_lenght = len(line_list)
    animation(f"The amount of Lines : {txt_lenght}\n")


def word_len():
    with open(txt, "r") as file:
        global word_list
        word_list = file.read().split()
        word_lenght = len(word_list)
        animation(f"The amount of Word : {word_lenght}\n")


def character_len():
    with open(txt, "r") as file:
        character_list = file.read()
        h = len(character_list)
        animation(f"The amount of Charecters : {h}\n")


def counting(n):
    count_list = []
    for i in set(word_list):
        count_list.append((i, word_list.count(i)))
        count_list.sort(key=lambda x: x[1], reverse=True)
        # print(count_list)
    tops = count_list[:n]
    animation(f"Here are the top {n} words (counts):\n")
    print(f"\nWords\tCounts")
    for word, counter in tops:
        animation(f"{word}\t{counter}\n")
        colorize("-" * 3)


def main():
    # delete()
    banner("... Results ...")
    colorize("=" * 70)
    name()
    animation(f"Theother details about analyzed text are:\n\n")
    line_len()
    word_len()
    character_len()
    colorize("=" * 70)
    counting(5)
    delete(clk=input(""))


if __name__ == "__main__":
    main()
