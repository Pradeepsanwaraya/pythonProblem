try:
    f = open("students.txt", "r")
    result = open("result.txt", "w")
    error = open("error_log.txt", "w")

    for line in f:
        record = line.strip()
        data = record.split(",")

        try:
            
            if len(data) < 4:
                raise ValueError("Marks are missing")

            
            sid, name, subject, marks = data

           
            if not sid or not name or not subject or not marks:
                raise ValueError("Required data is missing")

            marks = int(marks)

      
            if marks < 0 or marks > 100:
                raise ValueError("Marks must be between 0 and 100")
            
            if marks >= 90:
                grade = "Excellent"
            elif marks >= 75:
                grade = "Very Good"
            elif marks >= 60:
                grade = "Good"
            elif marks >= 40:
                grade = "Pass"
            else:
                grade = "Fail"
            result.write(f"{sid} - {name} - {subject} - {marks} - {grade}\n")

        except ValueError as e:
   
            if len(data) == 4 and data[3] and not data[3].isdigit():
                reason = "Marks must be numeric"
            elif len(data) < 4:
                reason = "Marks are missing"
            else:
                reason = str(e)

            error.write(f"Error: {record} -> {reason}\n")

  
    f.close()
    result.close()
    error.close()

    print("Student result processing completed successfully.")
    print("Valid records have been written to result.txt")
    print("Invalid records have been written to error_log.txt")

except FileNotFoundError:
    print("Error: students.txt file not found.")