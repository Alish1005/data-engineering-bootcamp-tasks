import datetime
class Post:
    all=[];
    def __init__(self,title:str,author:str,image:str,section:str,keywords:[],category:str,type:str,description:str,summary:str,content:str,location:str,source:str):

        assert title!=None,"You must enter a title"
        assert author != None, "You must enter a title"
        assert section != None, "You must enter a title"
        assert category != None, "You must enter a title"
        assert type != None, "You must enter a title"
        assert description != None, "You must enter a title"

        Post.all.append(self)

        self.__Id=0 if len(Post.all)==None else len(Post.all)
        self.__title=title
        self.__author=author
        self.__image=image
        self.__section=section
        self.__keywords=keywords
        self.__category=category
        self.__type=type
        self.__description=description
        self.__Wordcount=len(self.__description.strip(' '))
        self.__summary=summary
        self.__content=content
        self.__location=location
        self.__source=source
        self.__date_published=datetime.datetime.now()


        print("The Post has been uploaded")
    def __repr__(self):
        print_in_location=f" in {self.__location} " if self.__location!=None else ""
        return (f"\n"
                f"______________________________________________________________\n"
                f"{self.__author} upload a {self.__class__.__name__}{print_in_location} at {self.__date_published}\n"
                f"{self.__title}\n"
                f"{self.__description}\n"
                f"{self.__image}\n"
                f"Keywords:{self.__keywords}")

        @property
        def Id(self):
            return self.__Id

        @property
        def title(self):
            return self.__title
        @title.setter
        def title(self, value):
            self.__title = value

        @property
        def author(self):
            return self.__author

        @property
        def image(self):
            return self.__image
        @image.setter
        def image(self, value):
            self.__image = image

        @property
        def section(self):
            return self.__section
        @section.setter
        def section(self, value):
            self.__section = value

        @property
        def keywords(self):
            return self.__keywords
        @keywords.setter
        def keywords(self, value):
            self.__keywords = value

        @property
        def type(self):
            return self.__type
        @type.setter
        def type(self, value):
            self.__type = value

        @property
        def category(self):
            return self.__category
        @category.setter
        def category(self, value):
            self.__category = value

        @property
        def description(self):
            return self.__description
        @description.setter
        def description(self, value):
            self.__description = value
            self.__Wordcount=len(value.strip(' '))

        @property
        def Wordcount(self):
            return self.__Wordcount

        @property
        def summary(self):
            return self.__summary
        @summary.setter
        def summary(self, value):
            self.__summary = value

        @property
        def content(self):
            return self.__content
        @content.setter
        def content(self, value):
            self.__content = value

        @property
        def location(self):
            return self.__location
        @location.setter
        def location(self, value):
            self.__location = value

        @property
        def date_published(self):
            return self.__date_published


post1=Post("Hello","Ali",None,"trip",['trip','vacation','like'],"all",'post',"this is my first post",None,None,"lobanon",None)
post2 = Post(title="10 Best Tourist Attractions in Paris",author="Emma Thompson",image="paris-tower.jpg",section="Travel",keywords=["Travel", "Tourism", "Paris"],category="Destinations",type="Listicle",description="Explore the top tourist attractions in the beautiful city of Paris.",summary="Discover the must-visit places that showcase the charm and culture of Paris.",content="Paris, often referred to as the 'City of Love'...",location="Paris, France",source="https://www.example.com/article/paris-attractions")
post3=Post(title="Healthy Breakfast Ideas",author="Alice Johnson",image="breakfast.jpg",section="Food",keywords=["Food", "Health", "Recipes"],category="Cooking",type="Article",description="Start your day with these nutritious breakfast options.",summary="Explore a variety of healthy and delicious breakfast recipes.",content="A nutritious breakfast is essential for...",location=None,source="https://www.example.com/article/healthy-breakfast")
post4=Post(title="The Benefits of Yoga",author="Michael Smith",image="yoga.jpg",section="Health",keywords=["Health", "Fitness", "Yoga"],category="Wellness",type="Guide",description="Discover the physical and mental benefits of practicing yoga.",summary="Learn how yoga can improve flexibility, strength, and relaxation.",content="Yoga is an ancient practice that...",location=None,source="https://www.example.com/article/benefits-of-yoga")
print(Post.all.__repr__())