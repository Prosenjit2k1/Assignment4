'''file_name='sample.txt'
try:
    with open('sample.txt', 'r') as file:
    print("Reading file content")
    reading_file=file.readlines()
    for line in reading_file:
        print(line.strip())
except file_not_found_error:
    print(f"The file {file_name} was not found")     
 '''
data=input("Enter text to write to the file: ")
with open('output.txt','w') as new_file:
    new_file.write(data)
    print("Data  successfully written to the ",'output.txt')
with open('output.txt','a') as file:
    append_data=input("Enter additional text to append : ")
    file.write(append_data)
    print("Data successfully appended")
with open('output.txt','r') as file1:
    reading_file=file1.read()
    print("Final content of","output.txt")
    print(reading_file)


