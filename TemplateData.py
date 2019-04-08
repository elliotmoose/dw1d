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

def student(name, id, student_class, can_number, contact, email,  modules):
    return {
        'name' : name,
        'id': id,
        'class': student_class,
        'can_number': can_number,
        'contact': contact,
        'email': email,
        'modules' : modules,
        'credits': 500
    }

def module(name, id):
    return {
        'name' : name,
        'id' : id
    }

slot1 = slot('0800', '24/08/19')
slot2 = slot('1000', '24/08/19')

meixuan = prof('Mei Xuan', '91111000', 'meixuan@sutd.edu.sg',['10.008', '10.011'])
chunkiat = prof('Chun Kiat', '91111999', 'chunkiat@sutd.edu.sg',['10.007'])
okakurniawan = prof('Oka Kurniawan', '90000999', 'okakurniawan@sutd.edu.sg',['10.009'])

biology = module('Introduction to Biology', '10.012')
physics = module('Engineering in the Physical World', '10.008')
modellingsystems = module('Modelling the Systems World', '10.007')
digitalworld = module('Digital World', '10.009')

dbtemplate = {}
dbtemplate['current'] = []        
dbtemplate['professors'] = [meixuan, chunkiat, okakurniawan]
dbtemplate['students'] = []
dbtemplate['modules'] = [biology, physics, modellingsystems, digitalworld]
dbtemplate['slots'] = [slot1, slot2] 

import copy
loggedindbtemplate = copy.deepcopy(dbtemplate)
loggedindbtemplate['current'] = student('Elliot', '1003501', 'F04', '999999999999', '98880000', 'elliot@mymail.sutd.edu.sg', ['10.007', '10.009'])