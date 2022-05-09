# # print("\33[101m ERROR \33[0m:")
# format = ';'.join([str(7), str(31), str(47)])
# message_type = "ERROR"

# print(f"\x1b[{format}m {message_type} \x1b[0m: This is an {message_type}, are you sure you ok?")
# print()

# format = ';'.join([str(7), str(33), str(40)])
# message_type = "WARNING"
# print(f"\x1b[{format}m {message_type} \x1b[0m: This is a {message_type}, hope you are warned, and warm!")
# print()

# format = ';'.join([str(7), str(32), str(40)])
# message_type = "INFO"
# print(f"\x1b[{format}m {message_type} \x1b[0m: This is an {message_type} message, are you informed, and know it all now?")
# print()

# format = ';'.join([str(7), str(34), str(47)])
# message_type = "GENERAL"
# print(f"\x1b[{format}m {message_type} \x1b[0m: This is a {message_type} message, for you my General!")


from printer import Printer

json_object = {"name":"John", "age":30, "car":"null"}
type(json_object)

print = Printer()
print.log_message("ERROR", "Got and error: ")
print.log_message("INFO", "Got and error: \n", data=json_object)
# print.log_message("INFO", "Hi There")
# print.log_message("ERROR", "Hi There")
# print.log_message("GENERAL", "Hi There")
# print.log_message("GEN", "Hi There")