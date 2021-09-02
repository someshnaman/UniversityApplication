database_section = "courseInsertion"

query_insert_course = "INSERT INTO course1 (courseID , courseCode , courseName , courseDesc , courseImageUrl , " \
                      "courseDuration " \
                      ") VALUES (?,?,?,?,?,?) "
uery_insert_user = "INSERT INTO user(id, email , password , username ) VALUES (?,?,?,?) "
query_update_course = "UPDATE course1 SET courseCode=? , courseName=? , courseDesc=? , courseImageUrl=? , " \
                      "courseDuration=? " \
                      "where courseID=? "
query_for_list_of_email_or_username = "select ? from user"
query_find_course_by_id = "select * from course1 where courseID=?"
query_delete_course_by_id = "DELETE from course1 where courseID=?"
query_find_user_by_email = "select * from user where email=? ALLOW Filtering"

