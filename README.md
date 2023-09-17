# digital_class
Digital class project. Mastering Django

# The project is called ‘Digital class’
> The main goal is digitalisation of the learning process. It is a reflection of the processes in real world. Using this system teachers and students can see the whole picture.
It provides students with an access to the lessons and class materials: presentations, video-recordings, links to additional materials and links to respective tasks. Also students can comment each lesson and ask questions to teachers and communicate.
The teachers can upload the respective materials and do assessments and communicate with the students and place tasks and materials for self-studying.

Projected DataBase: 

Data tables needed:
- Persons (Users)
	- id
	- first name
	- last name
	- dob
	- group_id
	- role (enum) ? # actually IDK how to implement it

- Teachers
	- id
	- person_id
	- group_id (many groups)
	- thema_id (many themas)

- Students
  - id
	- person_id
	- group_id (many groups)

- Groups
	- id
	- group_name
	- group_type

- Module
	- id
	- topic

- Lessons
	- id
	- group_id
	- lesson_type
	- module_id
	- topic
	- date
	- start_time
	- end_time
	- teacher_id

- Materials
	- id
	- type_of_materials
	- titlle
	- description
	- lesson_id

- Comments
	- person_id
	- lesson_id
	- body

## Development steps:
- setting up Django project (basically done)
- define DB models in models.py (started, but not finished)
	- add to user model the "role of user"("teacher", "student" etc) [done but can not move the field up in admin]
- create student app [x]
- create teacher app [x]
- registering created apps in settings [x]

- refactor 'Resource' model creating tables:
	- Module
	- Lessons
	- Materials
	- Comments

- define relations between user-teacher-student 

- create templates:
	- teachers part
		- lessons list
		- lesson for teacher (with possibility to upload materials)
		- uploading materials
		- answering students questions
		- looking up students list 
		- access to student profile (+ answers made by student) + teachers notes
	- students part (also accessible by teachers) any authorised user can see it
		- list of lessons
		- lesson for student
		- student's profile (including answered questions + answers from teachers)

- build logic in 'views' for above mentioned templates
