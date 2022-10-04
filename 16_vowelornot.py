#   This code print if a letter is a vowel or not

def v_yn(l):
         if (l == "a") or (l == "e") or (l == "i") or (l == "o") or (l == "u"):
            return print("\nthe character inserted is a vowel")
         else:
            return print("\nthe character inserted is NOT a vowel")

k = str(input("\nInsert a letter:  "))

v_yn(k)