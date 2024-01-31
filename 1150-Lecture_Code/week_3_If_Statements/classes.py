csharp = input('Have you taken C# in programming class? Type "yes" if so: ')
java = input('Have you taken Java programming in class? Type "yes" if so: ')

if csharp == 'yes' or java == 'yes':  # if commands telling program to verify input, and if so, say this.
    print('You can take iOs Programming!')
else:
    print('You need to take either C# or Java')
