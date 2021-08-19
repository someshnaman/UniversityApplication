database_section = "courseInsertion"

query_insert_course = "INSERT INTO course1 (courseID , courseCode , courseName , courseDesc , courseImageUrl , " \
                      "courseDuration " \
                      ") VALUES (?,?,?,?,?,?) "
query_update_course = "UPDATE course1 SET courseCode=? , courseName=? , courseDesc=? , courseImageUrl=? , " \
                      "courseDuration=? " \
                      "where courseID=? "
query_find_course_by_id = "select * from course1 where courseID=?"
query_delete_course_by_id = "DELETE from course1 where courseID=?"

