import csv
import os

# Some constants we may reuse through-out the program.
LINE_DIVIDER = "-------------------------"

# Path to the input file.
input_file = os.path.join("Resources", "election_data.csv")

# Open the CSV file.
with open(input_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Given CSV file has a header row.
    # Skipping the header row.
    #
    # Headers are:
    # ['Ballot ID', 'County', 'Candidate']
    header = next(csv_reader)

    total_votes = 0
    # Dictionary to store candidate names and the count of votes.
    # Name of the candidate is the key and the count of votes for that candidate is the value.
    votes_dictionary = {}
    # No winner now.
    winner = ""
    highest_votes_count = 0

    # Iterate through all the rows to perform analysis.
    for row in csv_reader:
        candidate = row[2]
        # Use "get" method of dictionary to get the value stored for the given key if it exists.
        # The "get" method returns the default we provide, which is zero in this case, if the key doesn't exist.
        votes_for_candidate = votes_dictionary.get(candidate, 0) + 1
        votes_dictionary[candidate] = votes_for_candidate
        if votes_for_candidate > highest_votes_count:
            highest_votes_count = votes_for_candidate
            winner = candidate
        total_votes = total_votes + 1

    output = [
        "Election Results",
        LINE_DIVIDER,
        f'Total Votes: {total_votes}',
        LINE_DIVIDER
    ]
    for candidate in votes_dictionary:
        votes_for_candidate = votes_dictionary[candidate]
        output.append(f'{candidate}: {(votes_for_candidate / total_votes):.3%} ({votes_for_candidate})')
    output.append(LINE_DIVIDER)
    output.append(f'Winner: {winner}')
    output.append(LINE_DIVIDER)

    output_file = os.path.join("analysis", "output.txt")

    with open(output_file, 'w') as file:
        for output_line in output:
            print(output_line)
            file.write(output_line + os.linesep)
