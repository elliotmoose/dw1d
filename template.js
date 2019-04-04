/**
 * Here are the templates for the data to be passed into the UI
 */

/**
 * Student
 */
let studentTemplate = {
    name: 'Student Name',
    student_id: 1003999,
    class: 'F04'
}

/**
 * Subject
 */
let subjectTemplate = {
    name: 'Subject Name'
}

/**
 * Final Payload Template, containing all above templates as children
 */
let payloadTemplate = {
    user : studentTemplate,
    subjects : [

    ]
}