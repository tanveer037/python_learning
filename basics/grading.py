#Here we are calculating a grade based on finals and class performance. If finals + class performance is bellow 40, which is a F, teacher will increase some mark in class performance to make the studen pass
finals = float( input("Enter the finals mark: ") )
class_performance = float( input("Enter the class performance mark: ") )
total = finals + class_performance
if total < 40 :
    class_performance = 30
    print( "Class performance lightly evaluated" )
total = finals + class_performance
print(f"total = {total} ")