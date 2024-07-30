class profile:
    def __init__(self, username, profile_image=None, cover_image=None, education=None, birth_day=None, gender=None, posts=None):
        self.username = username
        self.profile_image = profile_image
        self.cover_image = cover_image
        self.education = education
        self.birth_day = birth_day
        self.gender = gender
        self.posts = posts
        self.id = 0

    def changeUsername(self, newUser):
        self.username = newUser

    def changeProfileImage(self, newImage):
        self.profile_image = newImage

    def changeCoverImage(self, newImage):
        self.cover_image = newImage

    def changeBirthday(self, newBirthDay):
        self.birth_day = newBirthDay

    def changeEdu(self, newEducation):
        self.education = newEducation

    def changeGender(self, newGender):
        self.gender = newGender

    def addPost(self, newPost):
        self.posts.append("")
