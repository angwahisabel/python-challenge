import os

# Function to read data from CSV file
def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header row
        for line in file:
            ballot_id, county, candidate = line.strip().split(',')
            data.append({'Ballot ID': int(ballot_id), 'County': county, 'Candidate': candidate})
    return data

# Function to calculate the election results
def calculate_results(data):
    total_votes = len(data)
    candidates = set(row['Candidate'] for row in data)
    votes_per_candidate = {candidate: sum(1 for row in data if row['Candidate'] == candidate) for candidate in candidates}
    winner = max(votes_per_candidate, key=votes_per_candidate.get)
    return total_votes, votes_per_candidate, winner

# Function to print the analysis to the terminal
def print_analysis(total_votes, votes_per_candidate, winner):
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in votes_per_candidate.items():
        print(f"{candidate}: {(votes / total_votes) * 100:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# Function to export the results to a text file
def export_results(total_votes, votes_per_candidate, winner):
    output_folder = os.path.join(os.path.dirname(__file__), "analysis")
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, "election_results.txt")

    with open(output_file, "w") as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("-------------------------\n")
        for candidate, votes in votes_per_candidate.items():
            file.write(f"{candidate}: {(votes / total_votes) * 100:.3f}% ({votes})\n")
        file.write("-------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write("-------------------------\n")

# Main function
def main():
    # Get the path to the CSV file
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, "resources", "election_data.csv")

    data = read_csv(filepath)
    total_votes, votes_per_candidate, winner = calculate_results(data)

    # Print analysis to terminal
    print_analysis(total_votes, votes_per_candidate, winner)

    # Export results to a text file
    export_results(total_votes, votes_per_candidate, winner)
    print("Results exported to 'analysis/election_results.txt'")

if __name__ == "__main__":
    main()
