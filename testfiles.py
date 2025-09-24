import glob

bad_labels = []

for f in glob.glob("**/labels/**/*.txt", recursive=True):
    with open(f) as file:
        for line in file:
            cls = int(line.split()[0])
            if cls < 0 or cls >= 1:  # since nc=1, only class "0" is valid
                bad_labels.append((f, line.strip()))

if bad_labels:
    print("⚠️ Found invalid labels:")
    for f, line in bad_labels:
        print(f"{f}: {line}")
else:
    print("✅ All labels are valid!")
