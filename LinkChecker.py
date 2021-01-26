#This script was written to check all possible link IDs if casing in unknown
#Made by Willox25565

import requests, webbrowser, time
from itertools import product

def start():
    option = input(("\n\n\nChoose a domain for bruteforce: \n1) bit.ly\n2) imgur.com\n3) Keyboard input(might not work)\n\nNumber: "))
    if option == "1":
        address = "https://bit.ly/"
    if option == "2":
        address = "https://imgur.com/"
    if option == "3":
        address = input("Input you address here as an example: \n\n https://bit.ly/ \n https://imgur.com/ \n\nAddress: ")
    sub = input("\n\nInput your id for bruteforce: ")
    return address, sub

def generate_and_bruteforce(sub, address, trouble, found):
    ids = list(set(list(map(''.join, product(*zip(sub.lower(), sub.upper()))))))
    for id in ids:
        url = address + id
        try: 
            result = requests.post(url)
            print(url, result) #debug
        except Exception:
            print(url, "some trouble with this one") #debug
            trouble.append(url)
        if str(result) == "<Response [200]>":
            found.append(url)

def results_printer(found, trouble):
    print("\n\n\n=====RESULTS=====")
    if len(found) == 0:
        print("\n\nNo working urls found")
    else:
        print('\n\nURLs found:')
        for i in found:
            print(i)

    if len(trouble) > 0:
        print("\n\nThere were some troubles with this links")
        for i in trouble:
            print(i)

def output_save(found, trouble):
    if len(found) > 0 or len(trouble) > 0:
        answer = str(input("\n\nWould you like to save output to file?(yes/no): "))
        if answer.lower() == "yes":
            filename = "LinkChecker_" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
            f = open(filename, 'w')
            if len(found) == 0:
                f.write("No working urls found\n")
            else:
                f.write("URLs found:\n")
                for i in found:
                    f.write(i+"\n")
            if len(trouble) > 0:
                f.write("\n\nThere were some troubles with this links:\n")
                for i in trouble:
                    f.write(i+"\n")
            f.close()
            print("Results were saved to file.")
        else:
            print("Results were not saved.")

def browse(found):
    if len(found) > 0:
        answer = str(input("\n\nDo you want to open found links in browser?(yes/no): "))
        if answer.lower() == "yes":
            for i in found:
                webbrowser.open(i, new=2)

def main():
        address, sub = start()
        found = []
        trouble = []
        generate_and_bruteforce(sub, address, trouble, found)
        results_printer(found, trouble)
        output_save(found, trouble)
        browse(found)

if __name__ == "__main__":
    while True:
        main()
        if input("Do you want ro repeat? (yes/no): ").lower() == "no":
            break