file_path = 'sentiment.train.1'
write_path = 'sentiment.train.2'

with open(file_path, 'r') as f:
    with open(write_path, 'w') as w:
        for line in f:
            tokens = line.split(" ")
            clean_line = ""
            for token in tokens:
                if token.startswith("http://") or token.startswith("https://") or token.startswith("@"):
                    pass
                else:
                    clean_line += " " + token
            w.write(clean_line[1:])
        