#arbitary parameters(kwargs)
def student_info(**kwargs):
    for key,value in kwargs.items():
        print(key+":"+value)
student_info(name="harshita",age="20",clg="bitm")