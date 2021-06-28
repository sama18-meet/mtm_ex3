#### PART 1 ####
# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output
NUM_DIGITS_IN_ID = 8
MIN_HW_AVG = 51
MAX_HW_AVG = 100
HUNDRED = 100
TWO = 2

def final_grade(input_path: str, output_path: str) -> int:
    output_lines = {}
    saved_avg_grades = {}
    input_file = open(input_path, 'r')
    output_file = open(output_path, 'w')
    course_avg_sum = 0
    for line in input_file:
        student_id, final_grade, output_line = getOutputLine(line[:-1])
        if output_line:
            output_lines[student_id] = output_line
            if student_id in saved_avg_grades:
                course_avg_sum -= saved_avg_grades[student_id]
            course_avg_sum += int(final_grade)
            saved_avg_grades[student_id] = final_grade
    for key in sorted(output_lines):
        output_file.write(output_lines[key])
    input_file.close()
    output_file.close()
    return course_avg_sum//len(output_lines) if len(output_lines) != 0 else 0

def isValidId(student_id: str) -> bool:
    return (len(student_id) == NUM_DIGITS_IN_ID and student_id[0] != '0')

def isValidName(student_name: str) -> bool:
    return student_name.isalpha() and student_name != ''

def isValidSemester(semester_num: str) -> bool:
    return semester_num != '' and int(semester_num) > 0

def isValidHwAvg(hw_avg: str) -> bool:
    return hw_avg != '' and MIN_HW_AVG <= int(hw_avg) and int(hw_avg) <= MAX_HW_AVG

def isValidLine(line: str) -> [str,str,bool]:
    line_content = line.replace(" ", "").split(',')
    if isValidId(line_content[0]) and isValidName(line_content[1]) \
        and isValidSemester(line_content[2]) and isValidHwAvg(line_content[3]):
        return line_content[0], line_content[3], True
    return None, None, False

def calcFinalGrade(student_id: int, hw_avg: int) -> int:
    return (student_id%HUNDRED + hw_avg)//2
    
def getOutputLine(input_line: str) -> [str,str,str]:
    student_id, hw_avg, line_valid = isValidLine(input_line)
    if (not line_valid):
        return None, None, None
    final_grade = calcFinalGrade(int(student_id), int(hw_avg))
    output_line = ", ".join((student_id, hw_avg, str(final_grade)+"\n"))
    return student_id, final_grade, output_line



########################################################################


#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def check_strings(s1: str, s2: str) -> bool:
    # TODO: implement here
    raise NotImplementedError
