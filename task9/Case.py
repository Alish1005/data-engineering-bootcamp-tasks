
class Case:
    all = [];
    def __init__(self,id:int,Pregnancies:int,Glucose:int,BloodPressure:int,SkinThickness:int,Insulin:int,BMI:int,DiabetesPedigreeFunction:int,Age:int,Outcome:int): #the values that are on the parameter are the deafult value for each attribute
        # throwing Exception if any of this are false
        #gives limit to each attr.
        assert id>=0,f"id can't be below zero"
        assert Pregnancies>=0,f"Pregnancies can't be below zero"
        assert Glucose>=0,f"Glucose can't be below zero"
        assert BloodPressure>=0,f"Blood Pressure can't be below zero"
        assert SkinThickness>=0,f"Skin Thickness can't be below zero"
        assert Insulin>=0,f"Insulin can't be below zero"
        assert BMI>=0,f"BMI can't be below zero"
        assert DiabetesPedigreeFunction>=0,f"Diabetes Pedigree Function can't be below zero"
        assert Age>=0,f"Age can't be below zero"
        assert Outcome>=0,f"Outcome can't be below zero"
        #initalize attr. : _attr is a private attr.
        self.__id=id
        self.__Pregnancies =Pregnancies
        self.__Glucose =Glucose
        self.__BloodPressure =BloodPressure
        self.__SkinThickness =SkinThickness
        self.__Insulin =Insulin
        self.__BMI =BMI
        self.__DiabetesPedigreeFunction =DiabetesPedigreeFunction
        self.__Age =Age
        self.__Outcome =Outcome
        #Actions to execute
        Case.all.append(self)
    def nbOfCases(self):
        return  len(Case.all)
