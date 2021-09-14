from flask import Flask , request
from flask_restful import Api , Resource , reqparse , abort , fields , marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Ruturaj8003#@localhost/MyAPI"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
mydb = SQLAlchemy(app)

class MyVideoModel(mydb.Model):
    id = mydb.Column(mydb.Integer , primary_key=True)
    name = mydb.Column(mydb.String(100) , nullable=False)
    likes = mydb.Column(mydb.Integer , nullable=False)
    views = mydb.Column(mydb.Integer , nullable=False)

    def __repr__(self):
        return f"Video(name = {self.name} , views = {self.views} , likes = {self.likes})"


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name" , type=str , help="Name of the video is required" , required=True)
video_put_args.add_argument("views" , type=int , help="Views of the video are required" , required=True)
video_put_args.add_argument("likes" , type=int , help="Likes on the video are required" , required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name" , type=str , help="Name of the video is required")
video_update_args.add_argument("views" , type=int , help="Views of the video are required")
video_update_args.add_argument("likes" , type=int , help="Likes on the video are required")



resource_fields = {
    "id" : fields.Integer,
    "name" : fields.String,
    "views" : fields.Integer,
    "likes" : fields.Integer
}

resource_fields_2 = {
    "name" : fields.String,
    "views" : fields.Integer,
    "likes" : fields.Integer
}




# names = {"Ruturaj" : {"age" : 21 , "gender" : "male"},
#          "Paper" : {"age" : 45 , "gender" : "female"}}
# class HelloWorld(Resource):
#     def get(self , name , age):
#         return names[name]
#
#     def post(self , name , age):
#         return names[name]



# videos = {}
#
# def abort_if_video_id_doesnt_exist(video_id):
#     if video_id not in videos:
#         abort(404 , message = "Video id is not valid")
#
#
# def abort_if_video_exist(video_id):
#     if video_id in videos:
#         abort(409 , message = "Video already exist with that ID.")


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self , video_id):
        result = MyVideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404 , message = "Could not find video with that ID")
        return result , 200
        # abort_if_video_id_doesnt_exist(video_id)
        # return videos[video_id]

    @marshal_with(resource_fields)
    def patch(self , video_id):
        args = video_update_args.parse_args()
        result = MyVideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404 , message = "Video Doesn't Exist. Connot Update.")
        if args["name"] :
            result.name = args["name"]

        if args["likes"]:
            result.likes = args["likes"]

        if args["views"]:
            result.views = args["views"]

        mydb.session.commit()

        return result , 200



    def delete(self , video_id):
        MyVideoModel.query.filter_by(id = video_id).delete()
        mydb.session.commit()
        return "Record Deleted" , 204
        # abort_if_video_id_doesnt_exist(video_id)
        # del videos[video_id]
        # return "" , 204

class Video2(Resource):
    @marshal_with(resource_fields_2)
    def put(self):
        args = video_put_args.parse_args()
        video = MyVideoModel(name=args["name"], views=args["views"], likes=args["likes"])
        mydb.session.add(video)
        mydb.session.commit()
        return video , 200



api.add_resource(Video , "/video/<int:video_id>")

api.add_resource(Video2 , "/video")


if __name__ == "__main__":
    app.run(debug=True)