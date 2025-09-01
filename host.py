with open("kjk.txt", "w", encoding="utf-8") as file:
    for i in range(1, 1000):
        file.write(f"{i}\n")

    # file.close()


with open("kjk.txt", "r", encoding="utf-8") as file:

    content = file.read()
    print(content)

# with open("kjk.txt", "a", encoding="utf-8") as file:
#     file.write("r")

#     file.write("=" * 50 + "\n\n")