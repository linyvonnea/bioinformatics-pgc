from Bio import SeqIO

# Load fasta file
file_path = "brca1.fasta"
record = SeqIO.read(file_path, "fasta")

# Sequence content
sequence = str(record.seq)
length = len(sequence)
gc_count = sequence.count("G") + sequence.count("C")
gc_content = (gc_count / length) * 100

# Output
print(f"File: {file_path}")
print(f"Sequence ID: {record.id}")
print(f"Total Length: {length} bp")
print(f"GC Content: {gc_content: .2f}%")
print(f"First 100 bases:\n{sequence[:100]}")
