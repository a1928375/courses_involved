courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': 
                {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': 
                {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
               'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res


def involved(courses, person):
    M={}
    H=[]
    for j in courses:
        for k in courses_offered(courses, j):
            if person==courses[j][k]["teacher"]:
                if j in M:
                    M[j].append(k)
                else:
                    M[j]=[k]
           
    for j in courses:
        for k in courses_offered(courses, j):
            if "assistant" in courses[j][k]:
                if person==courses[j][k]["assistant"]:
                    if j in M:
                        M[j].append(k)
                    else:
                        M[j]=[k]         
    return M


print involved(courses, 'Dave')

print involved(courses, 'Peter C.')

print involved(courses, 'Dorina')

print involved(courses,'Peter')

print involved(courses,'Robotic')

print involved(courses, '')
