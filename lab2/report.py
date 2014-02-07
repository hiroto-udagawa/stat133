import json

infile = open('data/test.json')
student = json.load(infile)
infile.close()

name = student['name']
grades = student['grades']

print "." * 70
print "%s got a %s out of %s on lab1" % (name, grades['lab1']['earned'],grades['lab1']['possible'])
print "%s got a %s out of %s on lab2" % (name, grades['lab2']['earned'],grades['lab2']['possible'])
print "%s got a %s out of %s on lab3" % (name, grades['lab3']['earned'],grades['lab3']['possible'])
print "." * 70