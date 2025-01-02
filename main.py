def main():
    charcount = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    file_contents = file_contents.lower()
    for c in file_contents:
        if (c not in charcount):
            charcount.update({c:0})
        charcount[c]+=1
    numwords = len(file_contents.split())
    print(f"There are {numwords} total words in the text.")
    for i in charcount:
        print (f"There are {charcount[i]} instances of the letter {i}")
main()