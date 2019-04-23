import uuid

def slot(time, date, prof_id):
    return {
        'time' : time,
        'date' : date,
        'prof_id': prof_id,
        'student_id': 'null',
        'id': newuuid()
    }

def prof(name,id, contact, email, modules):
    return {
        'name' : name,
        'id': id,
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

def newuuid():
    return str(uuid.uuid4())
slot1 = slot('0800', '24/08/19', 0)
slot2 = slot('1000', '25/08/19', 0)
slot3 = slot('1200', '26/08/19', 1)
slot4 = slot('1400', '27/08/19', 1)

meixuan = prof('Mei Xuan', 0, '91111000', 'meixuan@sutd.edu.sg',['10.008', '10.011'])
chunkiat = prof('Chun Kiat',1, '91111999', 'chunkiat@sutd.edu.sg',['10.007'])
okakurniawan = prof('Oka Kurniawan',2, '90000999', 'okakurniawan@sutd.edu.sg',['10.009'])

elliot = student('Elliot Koh', '1003501', 'F04', '974498831285', '91000092', 'elliot@sutd.edu.sg',['10.007', '10.009', '10.008', '10.011'])
sid = student('Sidharth', '1002345', 'F04', '372390003533', '91123123', 'sidharth@sutd.edu.sg',['10.007', '10.008', '10.011'])
#     elliot = student('Elliot Koh', '1003501', 'F04', '\xe2\xe4\xa8\x1b', '91000092', 'elliot@sutd.edu.sg',['10.007', '10.009', '10.008', '10.011'])
# sid = student('Sidharth', '1002345', 'F04', '\xc7\xa1h&', '91123123', 'sidharth@sutd.edu.sg',['10.007', '10.008', '10.011'])

biology = module('Introduction to Biology', '10.012')
physics = module('Engineering in the Physical World', '10.008')
modellingsystems = module('Modelling the Systems World', '10.007')
digitalworld = module('Digital World', '10.009')

dbtemplate = {}
dbtemplate['current'] = []        
dbtemplate['professors'] = [meixuan, chunkiat, okakurniawan]
dbtemplate['students'] = {
    elliot['id']: elliot, 
    sid['id'] : sid
}
dbtemplate['modules'] = [biology, physics, modellingsystems, digitalworld]
# dbtemplate['slots'] = [slot1, slot2, slot3, slot4] 
dbtemplate['slots'] = {
    slot1['id'] : slot1, 
    slot2['id'] : slot2, 
    slot3['id'] : slot3, 
    slot4['id'] : slot4, 
}

import copy
loggedindbtemplate = copy.deepcopy(dbtemplate)
loggedindbtemplate['current'] = student('Elliot', '1003501', 'F04', '999999999999', '98880000', 'elliot@mymail.sutd.edu.sg', ['10.007', '10.009', '10.008', '10.011'])