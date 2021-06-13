from flask import jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import dumps, ObjectId
import db_config as database

class Badges(Resource):
    """ Get all badges """
    def get(self):
        response = list(database.db.Badges.find())

        for doc in response:
            doc['_id'] = str(doc['_id'])

        return jsonify(response)

    def post(self):
        _ids = list(database.db.Badges.insert_many([
            
               {
                'header_img_url': request.json[0]['header_img_url'],
                'profile_picture_url': request.json[0]['profile_picture_url'],
                'name': request.json[0]['name'],
                'age': request.json[0]['age'],
                'city': request.json[0]['city'],
                'followers': request.json[0]['followers'],
                'likes': request.json[0]['likes'],
                'post': request.json[0]['post']
                },
               {
                'header_img_url': request.json[1]['header_img_url'],
                'profile_picture_url': request.json[1]['profile_picture_url'],
                'name': request.json[1]['name'],
                'age': request.json[1]['age'],
                'city': request.json[1]['city'],
                'followers': request.json[1]['followers'],
                'likes': request.json[1]['likes'],
                'post': request.json[1]['post']
                },
               {
                'header_img_url': request.json[2]['header_img_url'],
                'profile_picture_url': request.json[2]['profile_picture_url'],
                'name': request.json[2]['name'],
                'age': request.json[2]['age'],
                'city': request.json[2]['city'],
                'followers': request.json[2]['followers'],
                'likes': request.json[2]['likes'],
                'post': request.json[2]['post']
                },
               {
                'header_img_url': request.json[3]['header_img_url'],
                'profile_picture_url': request.json[3]['profile_picture_url'],
                'name': request.json[3]['name'],
                'age': request.json[3]['age'],
                'city': request.json[3]['city'],
                'followers': request.json[3]['followers'],
                'likes': request.json[3]['likes'],
                'post': request.json[3]['post']
                }
            #   {
            #     'header_img_url': request.json[4]['header_img_url'],
            #     'profile_picture_url': request.json[4]['profile_picture_url'],
            #     'name': request.json[4]['name'],
            #     'age': request.json[4]['age'],
            #     'city': request.json[4]['city'],
            #     'followers': request.json[4]['followers'],
            #     'likes': request.json[4]['likes'],
            #     'post': request.json[4]['post']
            #     },
            #    {
            #     'header_img_url': request.json[5]['header_img_url'],
            #     'profile_picture_url': request.json[5]['profile_picture_url'],
            #     'name': request.json[5]['name'],
            #     'age': request.json[5]['age'],
            #     'city': request.json[5]['city'],
            #     'followers': request.json[5]['followers'],
            #     'likes': request.json[5]['likes'],
            #     'post': request.json[5]['post']
            #     }
            
        ]).inserted_ids)

        results = []

        for _id in _ids:
            results.append(str(_id))

        return jsonify({'inserted_ids': results})

    def delete(self):
        return database.db.Badges.delete_many({}).deleted_count