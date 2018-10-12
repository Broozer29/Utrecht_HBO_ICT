dictionary ={
  "Alfred": 4,
  "Beatrice": 6,
  "Cleo": 1,
  "Daan": 6,
  "Erzel": 9,
  "Flugel": 10,
  "Grant": 10,
  "Hannes": 10
}

for x in dictionary:
    if dictionary[x] > 9:
        print(x, "heeft een score van: ", dictionary[x])