import json
import requests

player_dict = json.loads(requests.get("https://raw.githubusercontent.com/Charonum/poeltl_player_data/main/data.json").content)
while True:
    print(f"{len(player_dict)} potential players remaining")
    print("Recommended guess: " + list(player_dict.keys())[0])
    print()
    team = input("Team: ")
    team_fe = input("Found/Exclude: ")
    conference = input("Conference: ")
    conference_fe = input("Found/Exclude: ")
    division = input("Division: ")
    division_fe = input("Found/Exclude: ")
    position = input("Position: ")
    position_fe = input("Found/Exclude: ")
    height = input("Height (ex: 6 11): ")
    height_fhl = input("Found/Higher (y)/Lower (y): ")
    age = int(input("Age: "))
    age_fhl = input("Found/Higher (y)/Lower (y): ")
    number = int(input("Number: "))
    number_fhl = input("Found/Higher (y)/Lower (y): ")
    keys_to_delete = []
    feet, inches = map(int, height.split())
    calculated_height = feet * 12 + inches
    for key, value in player_dict.items():
        if (team_fe == 'e' and value[0] == team) or (team_fe == 'f' and value[0] != team):
            keys_to_delete.append(key)
            continue

        if (conference_fe == 'e' and value[1] == conference) or (conference_fe == 'f' and value[1] != conference):
            keys_to_delete.append(key)
            continue

        if (division_fe == 'e' and value[2] == division) or (division_fe == 'f' and value[2] != division):
            keys_to_delete.append(key)
            continue

        if (position_fe == 'e' and value[3] == position) or (position_fe == 'f' and value[3] != position):
            keys_to_delete.append(key)
            continue

        if (height_fhl == 'f' and value[4] != calculated_height) or (
                height_fhl == 'l' and value[4] >= calculated_height) or (
                height_fhl == 'h' and value[4] <= calculated_height) or (
                height_fhl == 'ly' and value[4] < calculated_height - 2) or (
                height_fhl == 'hy' and value[4] > calculated_height + 2):
            keys_to_delete.append(key)
            continue

        if (age_fhl == 'f' and value[5] != age) or (age_fhl == 'l' and value[5] >= age) or (
                age_fhl == 'h' and value[5] <= age) or (age_fhl == 'ly' and value[5] < age - 2) or (
                age_fhl == 'hy' and value[5] > age + 2):
            keys_to_delete.append(key)
            continue

        if (number_fhl == 'f' and int(value[6]) != number) or (number_fhl == 'l' and int(value[6]) >= number) or (
                number_fhl == 'h' and int(value[6]) <= number) or (
                number_fhl == 'ly' and int(value[6]) < number - 2) or (
                number_fhl == 'hy' and int(value[6]) > number + 2):
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del player_dict[key]
