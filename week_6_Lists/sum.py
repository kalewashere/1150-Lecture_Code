languages = ['Python', 'Java', 'JavaScript', 'C#', 'Swift']  # list used for example, coding languages which we will
# 'add together' next (add in quotes due to being a string)

for language in languages:  # this will print each value in each index on it's own line
    print(language)

all_languages = ' and '.join(languages)  # .join function brings together assigned list in a single line. whatever is
# indicated in '' will place that value in between each element when it is printed. can be anything,
# should be something that makes sense when printing in sentence or however data will be delivered to user.
print(all_languages)  # this will print whatever is indicated between (), which is the list + the element indicated
# between .join()

languages.sort() # prints list in a sorted order, alphabetical by default
print(languages)

languages.reverse() # prints indicated list in reverse order, in this case, reverse alphabetical
print(languages)