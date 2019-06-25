for line in file:
    if 'Naschekin' in line:
        rez = line.replace('Naschekin', '<UIB>')
        file1.write(rez)
    else:
        file1.write(line)


