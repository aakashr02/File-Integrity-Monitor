infile = r"File-Integrity-Monitor-master/alert.log"

important = []
keep_phrases = ["test",
              "important",
              "keep me"]

with open(infile) as f:
    f = f.readlines()
print(f)