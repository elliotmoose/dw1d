slot_1 = {
    'time' : '0800',
    'date' : '24/08/19'    
}

slot_2 = {
    'time' : '1000',
    'date' : '24/08/19'    
}

prof_1 = {
    'name' : 'Mei Xuan',
    'contact': '91110000',
    'email': 'meixuan@sutd.edu.sg',
    'slots' : [
        slot_1,
        slot_2
    ]
}

prof_2 = {
    'name' : 'Chun Kiat',
    'contact': '91119999',
    'email': 'chunkiat@sutd.edu.sg',
    'slots' : [
        slot_1
    ]
}

subject_1 = {
    'name' : "10.008 Engineering in the Physical World",
    'professors' : [prof_1,prof_2]
}

subject_2 = {
    'name' : "10.007 Modelling the Systems World",
    'professors' : [prof_2]
}

data = {
    'modules' : [subject_1, subject_2],
    'student' : {
        'name' : 'Elliot',
        'class' : 'F04',
        'student_id': '1003501',
        'credits' : 500
    }
}  