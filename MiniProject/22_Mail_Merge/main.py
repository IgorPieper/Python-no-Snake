PLACEHOLDER = "[name]"

with open("Input/invited_names.txt", "r") as inv_names:
    names = inv_names.readlines()

with open("Input/starting_letter.txt", "r") as file:
    lines = file.readlines()
    mail = lines.copy()
    for n in range(0, len(names)):
        name = names[n].replace("\n", "")
        mail[0] = lines[0].replace(PLACEHOLDER, name)
        f = open(f"Output/mail_for_{name}.py", "w")
        with open(f"Output/mail_for_{name}.py", "a") as final:
            for m in mail:
                final.write(m)
