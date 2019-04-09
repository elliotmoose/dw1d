/**
 * Here are the templates for the data to be passed into the UI
 */

/**
 * Student
 */
let studentTemplate = {
    name: 'Student Name',
    id: 1003999,
    class: 'F04'
}

/**
 * Professor
 */
let profTemplate = {
    name: 'Prof Name',    
    contact : '99999999',
    email : 'prof@email.com',
    slots : [

    ]
}

/**
 * Subject
 */
let subjectTemplate = {
    name: 'Subject Name',
    id: '10.000',
    professors: [

    ]
}

/**
 * Final Payload Template, containing all above templates as children
 */
let payloadTemplate = {
    current : studentTemplate,
    subjects : [
        subjectTemplate
    ],
}