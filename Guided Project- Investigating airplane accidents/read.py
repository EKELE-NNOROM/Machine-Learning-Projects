from collections import defaultdict
import operator

aviation_data = [x for x in open("AviationData.txt", "r")]
aviation_list = [x.split(" | ") for x in aviation_data]
lax_code = [row for row in aviation_list if "LAX94LA336" in row]
print(lax_code)

# Above process takes exponential time (each col in each row)

lax_lines = [x for x in open("AviationData.txt", "r") if "LAX94LA336" in x]
print(lax_lines)

# 3: Hash Tables
headers = aviation_data[0].split(" | ")
aviation_dict_list = [dict(zip(headers, row.split(" | "))) for row in aviation_data[1:]]
lax_dict = [row for row in aviation_dict_list if "LAX94LA336" in row.values()]
print(lax_dict)

# Above is easier.

# 4: Accidents by US State

state_accidents = defaultdict(int)
for row in aviation_dict_list:
    if row['Country'] == 'United States' and ", " in row['Location']:
        state = row['Location'].split(", ")[1]
        state_accidents[state] += 1
state_accidents = dict(state_accidents)
most_accident_state = max(state_accidents.items(), 
                          key=operator.itemgetter(1))[0]
print(state_accidents)
print(most_accident_state)

# Fatalities and Injuries by Month
monthly_injuries = defaultdict(lambda: [0,0])
for row in aviation_dict_list:
    month = row['Event Date'].split("/")[0]
    for ix, field in enumerate(['Total Fatal Injuries', 'Total Serious Injuries']):
        if row[field] != '':
            monthly_injuries[month][ix] += int(row[field])
        else:
            monthly_injuries[month][ix] += 0

print(monthly_injuries)

'''
6: Next Steps
That's it for the guided steps! We recommend exploring the data more on your own.

Here are some potential next steps:

Map out accidents using the basemap library for matplotlib.
Count up the number of accidents by air carrier.
Count up the number of accidents by airplane make and model.
Figure out what percentage of accidents occur in adverse weather conditions.
We recommend creating a Github repository and placing this project there. It will help other people, including employers, see your work. As you start to put multiple projects on Github, you'll have the beginnings of a strong portfolio.

You're welcome to keep working on the project here, but we recommend downloading it to your computer using the download icon above and working on it there.

We hope this guided project has been a good experience, and please email us at hello@dataquest.io if you want to share your work!
'''