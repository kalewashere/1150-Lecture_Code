""" Solving this took a lot of trial and error """


def main():
    megabytes = float(input('Please enter the number of megabytes: '))
    bytes = float(bytes_to_megabytes(megabytes))
    print(f'{megabytes} megabytes is equal to {bytes} bytes. ')


def bytes_to_megabytes(megabytes):
    mb = megabytes * 1000000
    return mb


main()  # calls function
# .... i got this code to work but i don't think...it's...correct? it gives me the correct answer, but i feel like
# some things may be backwards or...not correct in some way ahh, upon continuing the lecture video, i see i switched
# the placement for bytes and megabytes (should be megabytes_to_bytes instead) functions can be put in any order (
# program can be before main, and other way around, as long as function is called at end
