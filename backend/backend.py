from flask import Flask, request, jsonify
from flask_cors import CORS

import json
import pymongo

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return "Hello Worldy!"

@app.route('/goodbye')
def goodbye():
	return "goodbye!"

@app.route('/upload_to_mongo')
def uploadMongoCode():
	#print(request.args())
	#print("WHOOOOOOHOOOOOO!!")
	project_name = request.args.get('name')
	description = request.args.get('description')
	social_topic = request.args.getlist('social_topic')
	cs_topic = request.args.getlist('cs_topic')
	category = request.args.get('category')
	image = request.args.get('image')
	difficulty = request.args.get('difficulty')
	completion_time = request.args.get('completion_time')
	student_links = request.args.get('student_links')
	starter_code = request.args.get('starter_code')
	teacher_ppt = request.args.get('teacher_ppt')
	teacher_handout = request.args.get('teacher_handout')


	client = pymongo.MongoClient("mongodb://Teach:teachCS@edu-content-database-shard-00-00-wxgai.mongodb.net:27017,edu-content-database-shard-00-01-wxgai.mongodb.net:27017,edu-content-database-shard-00-02-wxgai.mongodb.net:27017/test?ssl=true&replicaSet=edu-content-database-shard-0&authSource=admin&retryWrites=true&w=majority")
	edu_database = client['edu-content']
	projectsList = edu_database.projects
	project = {"project_name": project_name,
		"description": description,
		"social_topic": social_topic,
		"cs_topic": cs_topic,
		"category": category,
		"image": image,
		"difficulty": difficulty,
		"completion_time": completion_time,
		"student_links": student_links,
		"starter_code": starter_code,
		"teacher_ppt": teacher_ppt,
		"teacher_handout": teacher_handout}
	projectsList.insert_one(project).inserted_id
	print(description)

	return "Uploading project now!"

#Right Now, this is a demo version of sign in!
@app.route('/signin', methods=['POST'])
def signin():
	content = request.get_json()
	try:
		username = content['username']
	except: 
		username = None
	try:
		password = content['password']
	except:
		password = None
	if (username == None or password == None):
		return jsonify({'response': 'bad request, please try again and specify a \'phoneNumber\' parameter in the JSON request body'})
	else:
		return jsonify({'user_id': "1"})



@app.route('/getallprojects')
def getallprojects():
	client = pymongo.MongoClient("mongodb://Teach:teachCS@edu-content-database-shard-00-00-wxgai.mongodb.net:27017,edu-content-database-shard-00-01-wxgai.mongodb.net:27017,edu-content-database-shard-00-02-wxgai.mongodb.net:27017/test?ssl=true&replicaSet=edu-content-database-shard-0&authSource=admin&retryWrites=true&w=majority")
	edu_database = client['edu-content']
	projectList = edu_database.projects.find()
	json_response = []
	for project in projectList:
		project_json = {
			"project_name": project['project_name'],
			"image": project['image'],
			"description": project['description']
		}
		json_response.append(project_json)

	return jsonify(projects=json_response)

@app.route('/generateCurriculum')
def generateCurriculum():
	return "Curriculum is here"



@app.route('/uploadteacher')
def uploadteacher():
	name = event['name']
	email = event['email']
	password = event['password']
	client = pymongo.MongoClient("mongodb://Teach:teachCS@edu-content-database-shard-00-00-wxgai.mongodb.net:27017,edu-content-database-shard-00-01-wxgai.mongodb.net:27017,edu-content-database-shard-00-02-wxgai.mongodb.net:27017/test?ssl=true&replicaSet=edu-content-database-shard-0&authSource=admin&retryWrites=true&w=majority")
	edu_database = client['edu-content']
	teacherList = edu_database.teachers
	
	teacher = {"name": name,
            "email": email,
            "password": password}
	
	teacherList.insert_one(teacher).inserted_id
	return "Uploaded"



@app.route('/createcurriculum')
def createcurriculum():
	curriculum_name = event['curriculum_name']
	teacher_id = event['teacher_id']
	project_list = event['project_list']

	client = pymongo.MongoClient("mongodb://Teach:teachCS@edu-content-database-shard-00-00-wxgai.mongodb.net:27017,edu-content-database-shard-00-01-wxgai.mongodb.net:27017,edu-content-database-shard-00-02-wxgai.mongodb.net:27017/test?ssl=true&replicaSet=edu-content-database-shard-0&authSource=admin&retryWrites=true&w=majority")
	edu_database = client['edu-content']
	curriculum_list = edu_database.curriculums

	curriculum = {
		"curriculum_name": curriculum_name,
		"teacher_id": teacher_id,
		"project_list": project_list,
	}

	curriculum_list.insert_one(curriculum).inserted_id
	return "Curriculum created and uploaded"


@app.route('/getcontent')
def getcontent():
	project_id = event['project_id']
	for_students = event['for_students']

	client = pymongo.MongoClient("mongodb://Teach:teachCS@edu-content-database-shard-00-00-wxgai.mongodb.net:27017,edu-content-database-shard-00-01-wxgai.mongodb.net:27017,edu-content-database-shard-00-02-wxgai.mongodb.net:27017/test?ssl=true&replicaSet=edu-content-database-shard-0&authSource=admin&retryWrites=true&w=majority")
	edu_database = client['edu-content']
	project_list = edu_database.projects

	myquery = { "_id": project_id }
	project = project_list.find_one(myquery)

	content = {}
	if for_students:
		content = {
			"starter_code": project.get("starter_code", ""),
			"student_links": project.get("student_links", "")
		}
	else:
		content = {
			"teacher_ppt": project.get("teacher_ppt", ""),
			"teacher_handout": project.get("teacher_handout", "")
		}

	return content



if __name__ == '__main__':
    app.run()