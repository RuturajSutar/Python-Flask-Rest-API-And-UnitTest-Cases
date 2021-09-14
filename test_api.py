import requests
import unittest
BASE = "http://127.0.0.1:5000/video"

class Test_API(unittest.TestCase):
    def test_get(self):
        video_id = input("Enter video ID to get video : ")
        response = requests.get(BASE + "/" + video_id)
        print("Result is : ")
        print(response.json())
        self.assertEqual(response.status_code , 200)
        print("Test case 1 passed")
    def test_put(self):
        video_name = input("Enter video name :")
        video_views = input("Enter video views :")
        video_likes = input("Enter video likes :")
        my_dict = {"name": video_name, "views": video_views, "likes": video_likes}
        response = requests.put(BASE , my_dict)
        print("Data entered is : ")
        print(response.json())
        self.assertEqual(response.status_code , 200)
        print("Test case 2 passed")
    def test_patch(self):
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
        my_dict = {"name": video_name, "views": video_views, "likes": video_likes}
        response = requests.patch(BASE + "/" + video_id, my_dict)
        print("Data updated is : ")
        print(response.json())
        self.assertEqual(response.status_code , 200)
        print("Test case 3 passed")
    def test_delete(self):
        video_id = input("Enter video ID : ")
        response = requests.delete(BASE + "/" + video_id)
        print("Data deleted Successfully")
        self.assertEqual(response.status_code , 204)
        print("Test case 4 passed")

if __name__ == "__main__":
    test_api = Test_API()
    # test_api.test_get()
    # test_api.test_put()
    # test_api.test_patch()
    test_api.test_delete()