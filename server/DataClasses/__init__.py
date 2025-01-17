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
        self.Address = ""
        self.Appointments = []
        self.MedRecod = []

    def _profiledict(self):
        return {
            "Name" : self.Name,
            "RollNo" : self.RollNo,
            "Gender" : self.Gender,
            "BGroup" : self.BGroup,
            "Mob" : self.Mob,
            "Address" : self.Address
        }

    def _signupdict(self):
        return {
            "Name" : self.Name,
            "RollNo" : self.RollNo,
            "Gender" : self.Gender,
            "BGroup" : self.BGroup,
            "Address" : self.Address,
            "Mob" : self.Mob,
            "Pwd" : self.Pwd,
            "Appointments" : self.Appointments,
            "MedRecord" : self.MedRecod
        }
