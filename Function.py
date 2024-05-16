def student(name1,class1,batch):
    result = {"name": name1,
              "class": class1,
               "batch": batch }
    
    return result

output = student("john","data_analytics","DA")

print(output)


def program(function,location,timing):
    result  = {"name": function,
               "place": location,
               "time": timing }
    
    return result

output = program("marriage","pune","07:00 PM")

print(output)

