import datetime
file = open("Hardlopers.txt","a+")


def strftime():
    vandaag = datetime.datetime.today()
    return vandaag.strftime("%a %d %b %Y")

def schrijfFile():
    tijd = "04:20:00"
    hardlopers = ["Miranda", "Piet", "Sascha", "Karel", "Kemal"]
    for i in hardlopers:
        file.write("%s  %s  %s\n" % (strftime(),tijd , i))
schrijfFile()
