def slot(time, date):
    return {
        'time' : time,
        'date' : date,
        'prof_id': 'null',
        'student_id': 'null'
    }

def prof(name, contact, email, modules):
    return {
        'name' : name,
        'contact': contact,
        'email': email,
        'modules' : modules
    }

def student(name, id, can_number, contact, email, student_class):
    pass

def module(name, id):
    return {
        'name' : name,
        'id' : id
    }

slot_1 = {
    'time' : '0800',
    'date' : '24/08/19'    
}

slot_2 = {
    'time' : '1000',
    'date' : '24/08/19'    
}

meixuan = {
    'name' : 'Mei Xuan',
    'contact': '91110000',
    'email': 'meixuan@sutd.edu.sg',
    'modules' : ['10.008', '10.011']
}

chunkiat = {
    'name' : 'Chun Kiat',
    'contact': '91119999',
    'email': 'chunkiat@sutd.edu.sg',
    'modules': ['10.007']
}

okakurniawan = prof('Oka Kurniawan')

# subject_1 = {
#     'name' : "10.008 Engineering in the Physical World",
#     'professors' : [prof_1,prof_2]
# }

# subject_2 = {
#     'name' : "10.007 Modelling the Systems World",
#     'professors' : [prof_2]
# }

# data = {
#     'subjects' : [subject_1, subject_2],
#     'student' : {
#         'name' : 'Elliot',
#         'class' : 'F04',
#         'student_id': '1003501',
#         'credits' : 500
#     }
# }  


dbtemplate = {}

dbtemplate['current'] = []
        
dbtemplate['professors'] = [prof_1, prof_2]

dbtemplate['students'] = []
dbtemplate ['slots'] = [slot_1, slot_2] 