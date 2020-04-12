people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]
#option 1
for person in people:
    print(lambda person:person)
    print(split_title_and_name)
    print(split_title_and_name(person))
    print(split_title_and_name(person) == (lambda person:person))

#option 2
print( list(map(split_title_and_name, people)) == list( map( ( lambda p : p.split()[0] + " " + p.split()[-1] ) , people )) )


