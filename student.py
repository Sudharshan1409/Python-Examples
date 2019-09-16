class student:

    def __init__(self,name = None,usn = None,marks = None,gender = None):

        self.name = name
        self.usn = usn
        self.marks = marks
        self.gender = gender

    def __repr__(self):
        
        return f"Name : {self.name}\nUSN : {self.usn}\nMarks : {self.marks}\nGender : {self.gender}\n"

if __name__ == "__main__":
    s = student(name = 'Sudharshan',gender = 'Male',usn = '4MN16CS040',marks = [80,90,70,85,95])
    k = []
    k.append(s)
    print(k)
    