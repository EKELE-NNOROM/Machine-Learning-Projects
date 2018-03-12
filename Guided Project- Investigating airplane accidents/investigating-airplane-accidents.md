# 1: Airline Accidents

Accidents are an unfortunate fact of air travel. Although flying is statistically safer than driving, there are minor and major accidents daily. In this project, you'll work with a dataset on airplane accidents to analyze patterns and figure out if we can find any common threads in the accidents.

In this project, you'll be working with a dataset that contains `77282` aviation accidents that occurred in the US and their associated metadata. The data comes from the [NTSB], and is stored in a file called `AviationData.txt`. You can download the file [here]. Here's the beginning of the file:

```python
Event Id | Investigation Type | Accident Number | Event Date | Location | Country | Latitude | Longitude | Airport Code | Airport Name | Injury Severity | Aircraft Damage | Aircraft Category | Registration Number | Make | Model | Amateur Built | Number of Engines | Engine Type | FAR Description | Schedule | Purpose of Flight | Air Carrier | Total Fatal Injuries | Total Serious Injuries | Total Minor Injuries | Total Uninjured | Weather Condition | Broad Phase of Flight | Report Status | Publication Date |
20150908X74637 | Accident | CEN15LA402 | 09/08/2015 | Freeport, IL | United States | 42.246111 | -89.581945 | KFEP | albertus Airport | Non-Fatal | Substantial | Unknown | N24TL | CLARKE REGINALD W | DRAGONFLY MK |  |  |  | Part 91: General Aviation |  | Personal |  |  | 1 |  |  | VMC | TAKEOFF | Preliminary | 09/09/2015 |
20150906X32704 | Accident | ERA15LA339 | 09/05/2015 | Laconia, NH | United States | 43.606389 | -71.452778 | LCI | Laconia Municipal Airport | Fatal(1) | Substantial | Weight-Shift | N2264X | EVOLUTION AIRCRAFT INC | REVO | No | 1 | Reciprocating | Part 91: General Aviation |  | Personal |  | 1 |  |  |  | VMC | MANEUVERING | Preliminary | 09/10/2015 |
20150908X00229 | Accident | GAA15CA251 | 09/04/2015 | Hayes, SD | United States |  |  |  |  |  |  |  | N321DA | AIR TRACTOR INC | AT 402A |  |  |  |  |  |  |  |  |  |  |  |  |  | Preliminary |  |
```

As you can see, each row represents a single aviation accident, and contains descriptive data about the accident. Here are descriptions of some of the columns:

- Event Id -- the unique id of the incident.
- Investigation Type -- what kind of investigation the NTSB conducted.
- Event Date -- the date of the accident.
- Location -- where the accident occurred.
- Country -- the country where the accident occurred.
- Latitude -- the latitude of the accident.
- Longitude -- the longitude of the accident.
- Injury Severity -- How severe the injuries were, if any.
- Aircraft Damage -- the extent of the damage to the aircraft.
- Aircraft Category -- the type of aircraft.
- Make -- the make of the aircraft.
- Model -- the model of the aircraft.
- Number of Engines -- the number of engines on the plane.
- Air Carrier -- the carrier operating the aircraft.
- Total Fatal Injuries -- the number of fatal injuries.
- Total Serious Injuries -- the number of serious injuries.
- Total Minor Injuries -- the number of minor injuries.
- Total Uninjured -- the number of people who weren't injured.
- Broad Phase of Flight -- the phase of flight in which the accident occurred.

As you can see, the file isn't in CSV format -- instead the fields are separated with a pipe character (`|`). You'll need to do some custom parsing to read in `AviationData.txt`.

# Instructions

- Use the head and tail commands to explore AviationData.txt on the command line.
- Open the empty Python script read.py.
- In read.py, open AviationData.txt, and read each line into a list.
- At the end, you should have a list of strings, where each string is one line from AviationData.txt.
- Assign the result to aviation_data.
- Loop through each item in aviation_data, and split it on the | character.
- At the end, you should have a list of lists, where each inner list is a single row.
- Assign the result to aviation_list.
- Create a list lax_code.
- Search through aviation_list for LAX94LA336 -- this value could be in any column in any row.
- Whenever you find the value, append the entire row to lax_code.
- Were there any downsides to the approach you just took to search through AviationData.txt? Write a text file explaining.

# 2: Linear And Constant Time

In the last screen, the algorithm you wrote took exponential time, because it has to loop through each row, then each column inside that row.

There are ways to make the algorithm take linear and constant time while we still scan across the whole dataset, though.

## Instructions

Write a linear time algorithm that searches each row in aviation_data for the string LAX94LA336.

Write a constant time algorithm that searches AviationData.txt for the string LAX94LA336\. Are there any tradeoffs to using a constant or linear time solution versus an exponential time solution? Write a text file explaining.

# 3: Hash Tables

So far, you've stored the data as a list of strings, and a list of lists. You can also store the data as a list of dictionaries.

## Instructions

- Create an empty list called aviation_dict_list.
- Loop through each item in aviation_data, and split it on the | character.
- Convert the split row to a dictionary. The dictionary should have the columns names as keys, and the associated values as values. Here's an example of a single item: {"Event Id": "20150908X74637", "Investigation Type": "Accident", ...}.
- Append the result to aviation_dict_list.
- Create an empty list called lax_dict.
- Search through aviation_dict_list for LAX94LA336 -- this value could be in any key in any dictionary.
- Whenever you find the value, append the entire dictionary to lax_dict.
- Was it harder or easier to search through a list of dictionaries than a list of lists? Write your thoughts in a text file.

# 4: Accidents By US State

You now have two representations of the data, aviation_dict_list, and aviation_list. In the analysis in the next few screens, feel free pick the representation that makes the analysis the easiest.

In this screen, you'll count up how many accidents occurred in each US state, and then figure out which state had the most accidents overall.

## Instructions

- Count up how many times accidents occured in each US state, and assign the result to state_accidents.
- You can parse the state by splitting the Location field and extracting the state.
- Sort state_accidents, and extract the name of the state with the most aviation accidents.

# 5: Fatalities And Injuries By Month

You can also count up how many fatalities and serious injuries occurred in each month in the dataset.

## Instructions

- Count up how many fatalities and serious injuries occured in each unique month and year, and assign the result to `monthly_injuries`.

  - You can parse the date by splitting the `Event Date` column and extracting the month number.
  - You can add up fatalities and serious injuries by adding the numbers in the `Total Fatal Injuries` and `Total Serious Injuries` columns.
  - When there were no fatalities or serious injuries, the columns are blank, so you'll have to replace those items with `0`.

- Turn `monthly_injuries` into two lists – one with the month names, and one with the counts.

- Implement a clever way of displaying these lists so you can understand the number of fatalities and serious injuries per month.

# 6: Next Steps

That's it for the guided steps! We recommend exploring the data more on your own.

Here are some potential next steps:

- Map out accidents using the [basemap] library for [matplotlib].
- Count up the number of accidents by air carrier.
- Count up the number of accidents by airplane make and model.
- Figure out what percentage of accidents occur in adverse weather conditions.

We recommend creating a [Github] repository and placing this project there. It will help other people, including employers, see your work. As you start to put multiple projects on Github, you'll have the beginnings of a strong portfolio.

You're welcome to keep working on the project here, but we recommend downloading it to your computer using the download icon above and working on it there.

We hope this guided project has been a good experience, and please email us at hello@dataquest.io if you want to share your work!

[basemap]: http://matplotlib.org/basemap/
[github]: https://github.com
[here]: http://catalog.data.gov/dataset/aviation-data-and-documentation-from-the-ntsb-accident-database-system-05748/resource/4b1e95fe-91a7-4112-85fa-424d2672a906
[matplotlib]: http://matplotlib.org/
[ntsb]: http://www.ntsb.gov/Pages/default.aspx
