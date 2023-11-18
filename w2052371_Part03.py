# # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: 20234004
# Date: 07/11/2023

print(" **** STUDENT PROGRESSION SOFTWARE ****")

# Part 03 -  Text File (extension)
def writeInAFile(Outcome):
    open('dataFile.txt', 'w').close()
    try:
        with open("dataFile.txt"):
            with open("dataFile.txt","a") as dataFile:
                dataFile.write(Outcome+"\n")
    except IOError:
        with open("dataFile.txt",'w') as dataFile:
            dataFile.write(Outcome+"\n")

def progressionOutcome():
    while True:
        try:
            volumeOfCredit = [int(credit) for credit in (input("Enter Pass, Defer, Fail credit in order: ").split())]
            Pass, Defer, Fail = volumeOfCredit[:]

            if not (Pass%20==0 and Defer%20==0 and Fail%20==0): 
                print("Out of range")
                continue
            if (Pass + Defer + Fail) != 120 or len(volumeOfCredit)!=3:
                print("Total incorrect")
                continue
         
        except ValueError as valueError:
            if ("invalid literal for int()" in str(valueError)):
                print("Integer required")
            elif ("not enough values to unpack" in str(valueError)) or ("too many values" in str(valueError)):
                print("You can input only 3 values!")
            continue
    
        if Pass == 120:
            return writeInAFile(f'Progress - {", ".join([str(credit) for credit in volumeOfCredit])}')
        elif (Pass+Defer) < Fail:
            return writeInAFile(f'Exclude - {",".join([str(credit) for credit in volumeOfCredit])}')
        elif Pass == 100 and (Defer==20 or Fail==20):
            return writeInAFile(f'Progress (module trailer) - {",".join([str(credit) for credit in volumeOfCredit])}')
        elif (Pass in [0,20,40,60,80]) and (Defer in [0,20,40,60,80,100,120]) and (Fail in [0,20,40,60]):
            return writeInAFile(f'Progress (module trailer) - {",".join([str(credit) for credit in volumeOfCredit])}')
            
while True:
    progressionOutcome()
    userChoice = str(input("\nWould you like to enter another set of data ?\nEnter 'y' for Yes or 'q' to Quit and view results: ")).title()
    if userChoice != "Y":
        break

with open("dataFile.txt","r") as dataFile:
    data = dataFile.readlines()
    for line in data:
        print(line)