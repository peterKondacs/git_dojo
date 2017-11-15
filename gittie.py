def say_hello ():
    print("Hi, my name is Gittie!")

def joke_telling():
    answer = input("would you like a joke?")
    if answer == "Yes":
        print("Egy fickó a taxisofőrhöz: '\n'- Mennyiért visz el Kecskemétig? '\n'- Nem a távolságtól, hanem az időtől függ - feleli a sofőr.'\n' - Mondjuk akkor, ha esik?")
    else:
        print("Then have a boring day.")

joke_telling()

def add(a, b):
    print(int(a) + int(b))
