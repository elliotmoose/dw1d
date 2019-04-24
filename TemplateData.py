"""

    THIS SCRIPT IS TO HELP AUTOMATE TESTING AND POPULATING OF DATABASE. IT PROVIDES HELPER FUNCTIONS TO CREATE DICTIONARIES THAT CONFORM TO THE DESIRED DATABASE STRUCTURE

"""

import uuid

def slot(time, date, prof_id):
    return {
        'time' : time,
        'date' : date,
        'prof_id': prof_id,
        'student_id': 'null',
        'id': newuuid()
    }

def prof(name,id, contact, email, modules, username, password):
    return {
        'name' : name,
        'id': id,
        'contact': contact,
        'email': email,
        'modules' : modules,
        'username': username,
        'password': password
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
slot1 = slot('0800', '24/04/19', 2)
slot12 = slot('1000', '24/04/19', 3)
slot13 = slot('1100', '24/04/19', 3)
slot14 = slot('1130', '24/04/19', 3)
slot2 = slot('0800', '25/04/19', 3)
slot21 = slot('1000', '25/04/19', 2)
slot3 = slot('1200', '25/04/19', 2)
slot4 = slot('1400', '25/04/19', 3)

meixuan = prof('Mei Xuan', 0, '91111000', 'meixuan@sutd.edu.sg',['10.008', '10.011'], 'meixuan','12345')
chunkiat = prof('Chun Kiat',1, '91111999', 'chunkiat@sutd.edu.sg',['10.007'], 'chunkiat','12345')
okakurniawan = prof('Oka Kurniawan',2, '90000999', 'okakurniawan@sutd.edu.sg',['10.009'], 'okakurniawan','12345')
natalieagus = prof('Natalie Agus',3, '90000999', 'natalie_agus@@sutd.edu.sg',['10.009'], 'natalieagus','12345')

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
dbtemplate['professors'] = [meixuan, chunkiat, okakurniawan, natalieagus]
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
    slot12['id'] : slot12, 
    slot13['id'] : slot13, 
    slot14['id'] : slot14, 
    slot21['id'] : slot21,     
}

import copy
loggedindbtemplate = copy.deepcopy(dbtemplate)
loggedindbtemplate['current'] = student('Elliot', '1003501', 'F04', '999999999999', '98880000', 'elliot@mymail.sutd.edu.sg', ['10.007', '10.009', '10.008', '10.011'])