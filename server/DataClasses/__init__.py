class Student:
    def __init__(
        self,
        Name = "user",
        RollNo = "rollno",
        Gender = "gender",
        BGroup = "bgroup",
        Mob = "mob",
        Pwd = "pwd"
    ):
        self.Name = Name
        self.RollNo = RollNo
        self.Gender = Gender
        self.BGroup = BGroup
        self.Mob = Mob
        self.Pwd = Pwd
        self.Appointments = []
        self.MedRecod = []

    def _dict(self):
        return {
            "Name" : self.Name,
            "RollNo" : self.RollNo,
            "Gender" : self.Gender,
            "BGroup" : self.BGroup,
            "Mob" : self.Mob,
        }

    def _signupdict(self):
        return {
            "Name" : self.Name,
            "RollNo" : self.RollNo,
            "Gender" : self.Gender,
            "BGroup" : self.BGroup,
            "Mob" : self.Mob,
            "Pwd" : self.Pwd,
            "Appointments" : self.Appointments,
            "MedRecord" : self.MedRecod
        }
