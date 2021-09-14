import requests

BASE = "http://127.0.0.1:5000/"

# response1 = requests.get(BASE + "helloworld/Ruturaj/21")
# print(response1.json())
#
# response2 = requests.post(BASE + "helloworld/Paper/55")
# print(response2.json())

# data = [{"likes" : 10 , "name" : "Tony Stark" , "views" : 10},
#         {"likes" : 100 , "name" : "Ruturaj Sutar" , "views" : 100},
#         {"likes" : 1000 , "name" : "Paper Potts" , "views" : 1000},
#         {"likes" : 100000 , "name" : "James Rhodes" , "views" : 10000}]
#
# for i in range(len(data)):
#     response3 = requests.put(BASE + "video", data[i])
#     print(response3.json())
#
# input()


# response5 = requests.delete(BASE + "video/0")
# print(response5)
#
#
# input()

# response4 = requests.get(BASE + "video/100")
# print(response4.json())

# response6 = requests.patch(BASE + "video/2" , {"views" : 99 , "likes" : 89 , "name" : "Ruturaj Sutar Tony"})
# print(response6.json())

#response7 = requests.delete(BASE + "video/2")

if __name__ == "__main__":
    while True:
        print("Select Choice : ")
        print("1 for get")
        print("2 for put")
        print("3 for patch")
        print("4 for delete")
        print("5 for Quit")
        choice = input("Enter your choice : ")
        if choice == "1":
            video_id = input("Enter video ID : ")
            response = requests.get(BASE + "video/"+video_id)
            print(response.json())
        if choice == "2":
            video_name = input("Enter video name :")
            video_views = input("Enter video views :")
            video_likes = input("Enter video likes :")
            my_dict = {"name" : video_name , "views" : video_views , "likes" : video_likes}
            response = requests.put(BASE + "video" , my_dict)
            print(response.json())
            print("Data added successfully")
        if choice == "3":
            video_name = None
            video_likes = None
            video_views = None
            video_id = input("Enter video ID : ")
            c1 = input("Do you want to update the video name (y/n) :")
            if c1 == "y":
                video_name = input("Enter video name : ")
            c2 = input("Do you want to update the video views (y/n) :")
            if c2 == "y":
                video_views = input("Enter video views : ")
            c3 = input("Do you want to update the video likes (y/n) :")
            if c3 == "y":
                video_likes = input("Enter video likes : ")
            my_dict = {"name" : video_name , "views" : video_views , "likes" : video_likes}
            response = requests.patch(BASE + "video/"+video_id , my_dict)
            print(response.json())
            print("Data updated successfully")

        if choice == "4":
            video_id = input("Enter video ID : ")
            response = requests.delete(BASE + "video/"+video_id)
            print("Data deleted successfully")
        if choice == "5":
            print("Thank You!!")
            break
