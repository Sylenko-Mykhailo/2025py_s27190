# PURPOSE:
# This program generates a random DNA sequence in FASTA format based on user input.
# It asks for a sequence length, ID, description, and your name.
# It then inserts the name randomly into the DNA sequence (excluded from statistics),
# saves the sequence in a .fasta file, and displays nucleotide composition statistics.

# CONTEXT OF USE:
# This script is useful in bioinformatics education, testing software tools that process FASTA files,
# or simulating DNA data for learning or prototyping purposes.

import random

#MODIFIED(Creating main function. It improves modularity):

def main():

    # Define the possible nucleotides
    NUCLEOTIDES = ['A', 'C', 'G', 'T']

    # Prompt user for input values
    # ORIGINAL:
    #sequence_length = int(input("Enter the sequence length: "))
    # MODIFIED (Added input validation to prevent crashes on invalid or negative input):
    while True:
        try:
            sequence_length = int(input("Enter the sequence length: "))
            if sequence_length <= 0:
                print("Sequence length must be a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    sequence_id = input("Enter the sequence ID: ")
    description = input("Provide a description of the sequence: ")
    user_name = input("Enter your name: ")

    # Generate the random DNA sequence
    dna_sequence = ''.join(random.choices(NUCLEOTIDES, k=sequence_length))

    # Insert user's name at a random position in the DNA sequence (not counted in stats)
    insert_pos = random.randint(0, sequence_length)
    sequence_with_name = dna_sequence[:insert_pos] + user_name + dna_sequence[insert_pos:]

    # Save the sequence in FASTA format
    fasta_filename = f"{sequence_id}.fasta"
    with open(fasta_filename, 'w') as fasta_file:
        fasta_file.write(f">{sequence_id} {description}\n")
        fasta_file.write(sequence_with_name + "\n")
    #ORIGINAL:
    # Calculate nucleotide statistics
    #a_count = dna_sequence.count('A')
    #c_count = dna_sequence.count('C')
    #g_count = dna_sequence.count('G')
    #t_count = dna_sequence.count('T')

    # Total without the inserted name
    #total = sequence_length
    #a_percent = (a_count / total) * 100
    #c_percent = (c_count / total) * 100
    #g_percent = (g_count / total) * 100
    #t_percent = (t_count / total) * 100

    # CG/AT ratio
    #cg_ratio = ((c_count + g_count) / (a_count + t_count)) * 100 if (a_count + t_count) > 0 else 0

    # Display the output
    #print(f"\nThe sequence was saved to the file {fasta_filename}")
    #print("Sequence statistics:")
    #print(f"A: {a_percent:.1f}%")
    #print(f"C: {c_percent:.1f}%")
    #print(f"G: {g_percent:.1f}%")
    #print(f"T: {t_percent:.1f}%")
    #print(f"%CG: {cg_ratio:.1f}")
    #MODIFIED(created function for easier management):
    def calculate_nucleotide_stats(sequence: str) -> dict:

        total = len(sequence)
        a_count = sequence.count('A')
        c_count = sequence.count('C')
        g_count = sequence.count('G')
        t_count = sequence.count('T')

        a_percent = (a_count / total) * 100
        c_percent = (c_count / total) * 100
        g_percent = (g_count / total) * 100
        t_percent = (t_count / total) * 100

        cg_ratio = ((c_count + g_count) / (a_count + t_count)) * 100 if (a_count + t_count) > 0 else 0

        return {
            'A': a_percent,
            'C': c_percent,
            'G': g_percent,
            'T': t_percent,
            'CG_ratio': cg_ratio
        }

    stats = calculate_nucleotide_stats(dna_sequence)


    print("Sequence statistics:")
    print(f"A: {stats['A']:.1f}%")
    print(f"C: {stats['C']:.1f}%")
    print(f"G: {stats['G']:.1f}%")
    print(f"T: {stats['T']:.1f}%")
    print(f"%CG: {stats['CG_ratio']:.1f}")

if __name__ == "__main__":
    main()
