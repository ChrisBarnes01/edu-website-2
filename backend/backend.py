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


@app.route('/getallprojects')
def getallprojects():
	client = pymongo.MongoClient("mongodb://Teach:teachCS@edu-content-database-shard-00-00-wxgai.mongodb.net:27017,edu-content-database-shard-00-01-wxgai.mongodb.net:27017,edu-content-database-shard-00-02-wxgai.mongodb.net:27017/test?ssl=true&replicaSet=edu-content-database-shard-0&authSource=admin&retryWrites=true&w=majority")
	edu_database = client['edu-content']
	projectList = edu_database.projects.find()
	#name
	#image
	#description
	#cs_topic
	json_response = []
	for project in projectList:
		project_json = {
			"project_name": project['project_name'],
			"image": project['image'],
			"description": project['description']
		}
		json_response.append(project_json)

	return jsonify(projects=json_response)



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


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)



if __name__ == '__main__':
    app.run()