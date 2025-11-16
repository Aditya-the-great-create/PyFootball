#Dictionary

monthConversions = {
    "JAN": "January",
    "FEB": "February",
    "MAR": "March",
    "APR": "April",
    "MAY": "May",
    "JUN":"June",
    "JUL": "July",
    "AUG":"August",
    "SEP": "September",
    "OCT": "October",
    "NOV": "November",
    "DEC": "December"
}

print(monthConversions["NOV"])
print(monthConversions.get("DEC"))
print(monthConversions.get("Oka", "Not valid key"))

Roundof16 = {
    "Team1": "Real Madrid",
    "Team2": "FC Barcelona",
    "Team3": "Juventus",
    "Team4": "Intermilan",
    "Team5": "Liverpool",
    "Team6": "Manchester City",
    "Team7": "Arsenal",
    "Team8": "Paris Saint-Germain",
    "Team9": "Roma",
    "Team10": "Bayern Munich",
    "Team11": "Dortmund Borussia",
    "Team12": "Ashton Villa",
    "Team13": "Atalanta",
    "Team14": "SSC Napoli",
    "Team15": "AC Monaco",
    "Team16": "Sporting CP"

}

print(Roundof16["Team1"])
print(Roundof16.get("Team16"))
