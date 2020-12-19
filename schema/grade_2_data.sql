DELETE FROM course_grade;
DELETE FROM course;
DELETE FROM student;

INSERT INTO student (sn, no, name)  VALUES
    (101, 'S001',  '张三'),
    (102, 'S002',  '李四'), 
    (103, 'S003',  '王五'),
    (104, 'S004',  '马六');

INSERT INTO course (sn, no, name, place, week, section )  VALUES 
    (101, 'C01',  '决策方法与应用', '一公教C309', '周一', '第二节'), 
    (102, 'C02',  'JAVA程序设计', '一公教B309', '周三', '第二节'),
    (103, 'C03',  '信息资源管理', '一公教A111', '周三', '第三节'),
    (104, 'C04',  '系统工程', '一公教B305', '周五', '第二节'),
    (105, 'C05',  '信息系统开发', '机房', '周五', '第三，四节');




INSERT INTO student_course (stu_sn, cou_sn, cou_name)  VALUES 
    (101, 101, '决策方法与应用'), 
    (102, 102, 'JAVA程序设计'),
    (103, 103, '信息资源管理'),
    (104, 104, '系统工程'),
    (102, 105, '信息系统开发');
  


INSERT INTO course_grade (stu_sn, cou_sn, grade)  VALUES 
    (101, 101,  91), 
    (102, 101,  89),
    (103, 101,  90),
    (101, 102,  89);


    