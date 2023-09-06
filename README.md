# digital_class
Digital class project. Mastering Django

# The project is called ‘Digital class’
> The main goal is digitalisation of the learning process. It is a reflection of the processes in real world. Using this system teachers and students can see the whole picture.
It provides students with an access to the lessons and class materials: presentations, video-recordings, links to additional materials and links to respective tasks. Also students can comment each lesson and ask questions to teachers and communicate.
The teachers can upload the respective materials and do assessments and communicate with the students and place tasks and materials for self-studying.

Projected DataBase: 

Data tables needed:
- Persons
	- id
	- first name
	- last name
	- dob
	- group_id

- Teachers
	- id
	- person_id
	- group_id (many groups)
	- thema_id (many themas)
- Students
  - id
	- person_id
	- group_id (many groups)

- Tutors
	- id
	- person_id
	- group_id (many groups)
	- thema_id (many themas)

- Groups
	- id
	- group_name
	- group_type

- Themas
	- id
	- thema_name
	- thema_description

- Topics
	- id
	- thema_id

- Lessons
	- id
	- group_id
	- lesson_type
	- thema_id
	- topic_id
	- date
	- start_time
	- end_time

- Materials
	- id
	- type_of_materials
	- titlle
	- description
	- lesson_id
	- thema_id
	- topic_id

- Comments
	- person_id
	- 
	- lesson_id
	- body

