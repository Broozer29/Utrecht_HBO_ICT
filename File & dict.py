def leesFile(welke):
    file = open('Ticker.txt', 'r').readlines()
    dictionary = {}
    for line in file:
        currentline = line.split(":")
        currentline[1] = currentline[-1].strip()
        if welke == "Company":
            dictionary[currentline[0]] = currentline[1]
        elif welke == "Ticker":
            dictionary[currentline[1]] = currentline[0]
    return dictionary


def main():
    companyFirst = leesFile("Company")
    tickerFirst = leesFile("Ticker")
    company = str(input("Enter Company Name: "))
    print(companyFirst[company])
    ticker = str(input("Enter Ticker Symbol: "))
    print(tickerFirst[ticker])

main()