filepath = input().split("\\")

file_details = filepath[-1].split('.')
file_name = file_details[0]
file_extension = file_details[1]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")