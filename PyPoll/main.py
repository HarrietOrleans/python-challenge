import csv

# set path
file_path = '../python-challenge/PyPoll/Resources/election_data.csv'

votes = []
with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        votes.append(row)

# Total number of votes cast
total_votes = len(votes)

# Vote counts for candidates
vote_counts = {}

for vote in votes:
    candidate = vote['Candidate']
    if candidate in vote_counts:
        vote_counts[candidate] += 1
    else:
        vote_counts[candidate] = 1

# List of candidates with votes
candidates = list(vote_counts.keys())

# Percentage of votes each candidate won
vote_percentages = {candidate: (count / total_votes) * 100 for candidate, count in vote_counts.items()}

# Winner based on popular vote
winner = max(vote_counts, key=vote_counts.get)

# Results print
results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

for candidate in candidates:
    results += (
        f"{candidate}: {vote_percentages[candidate]:.3f}% "
        f"({vote_counts[candidate]})\n"
    )

results += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)


print(results)

# Print to text file
output_file_path = '../python-challenge/PyPoll/Analysis/election_results.txt'
with open(output_file_path, 'w') as file:
    file.write(results)
