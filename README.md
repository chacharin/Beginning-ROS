# ROS-Setup

1. ติดตั้ง VMWare https://mailkmuttacth-my.sharepoint.com/:u:/g/personal/chacharin_lert_mail_kmutt_ac_th/EcJriInTdyVFhVROKO1TxxQBV7-VeZu-QNP1XYH_nTq60g?e=ZMe1Qd

2. ติดตั้ง Ubuntu https://releases.ubuntu.com/20.04.4/ubuntu-20.04.4-desktop-amd64.iso

3. ติดตั้ง ROS
  เปิด Terminal แล้วพิมพ์ทีละบรรทัด http://wiki.ros.org/noetic/Installation/Ubuntu
    (หาก EROR <bash: /opt/ros/noetic/setup.bash: No such file or directory> 
      ให้ใช้คำสั่ง gedit $HOME/.bashrc แล้วลบ /opt/ros/noetic/setup.bash ท้ายไฟล์)
      เพิ่มเติม
     $ sudo apt install ros-noetic-rosserial-arduino
     $ pyhton3 --version
     $ sudo apt install python3-pip
 
4. ติดตั้ง Enviroment
    $ mkdir catkin_ws
    $ cd catkin_ws/
    $ mkdir src
    $ catkin_make
    $ source ~/catkin_ws/devel/setup.bash
    $ gedit ~/.bashrc
    เติม sourceใหม่  ใน  bashrc แล้ว save
  
5. สร้าง Packgage เก็บ Code ของตัวเอง
    $ cd catkin_ws/src
    $ catkin_create_pkg my_project rospy turtlesim rosserial_arduino
    $ sudo snap install code --classic
    $ catkin_make (การ make  ต้องทำใน path catkin_ws หลัก )
    
6. สร้าง Node ด้วย python ใน ROS
    $ cd catkin_ws/src/my_project
    $ mkdir scripts
    $ cd scripts
    $ touch one.py
    $ chmod +x one.py
    $ cd --
    $ cd catkin_ws/src
    $ code .
    จากนั้นเขียนโค้ดใน VS code
    
7. ทดสอบเรียกใช้ไฟล์ Node ที่สร้างขึ้น ให้เปิด 3 terminal 
    terminal 1. สั่ง $ roscore
    terminal 2. สั่ง $ rosrun my_project one.py
    terminal 3. สั่ง $ rosnode list (  และทดสอบ $ rosnode kill /node_one)
    #ใช้ $ rqt_graph ดู Model Node Link

8. ทดลองใช้ turtlesim เพื่อเรียนรู้การรับส่งข้อมูลระหว่าง Node ให้เปิด 4 terminal
    terminal 1. สั่ง $ roscore 
    terminal 2. สั่ง $ rosrun turtlesim turtlesim_node
    terminal 3. สั่ง $ rosrun turtlesim draw_square
    terminal 4. สั่ง $ rqt_graph
    ตรวจสอบ topic ด้วยคำสั่งต่างๆ ดังต่อไปนี้ 
                   $ rostopic list
                   $ rostopic info /turtle1/pose
                   $ rosmsg show turtle1/pose (จะพบชุดตัวแปรข้อมูล)
                   $ rostopic echo /turtle1/pose
    
9. ทดลองสร้างโค้ด Pubish คำสั่ง ไปที่ turtlesim ให้เปิด 4 terminal
    terminal 1. สั่ง $ roscore 
    terminal 2. สั่ง $ rosrun turtlesim turtlesim_node 
    terminal 3. สั่ง $ rostopic list
                   $ rostopic info /cmd_vel
                   $ rosmsg show geometry_msgs/Twist (จะพบชุดตัวแปรข้อมูล)
    terminal 4. สั่ง $ cd catkin_ws/src/my_project/scripts
                   $ touch draw_circle.py
                   $ chmod +x draw_circle.py
                   $ cd ../..
                   $ code . แล้วเขียนโค้ด
                   (ต้องเปิดไฟล์ packgage.xml แล้วเติม geometry_msgs ใน depend tag 3 อัน)
                   $ rosrun my_project draw_circle.py
  
 10. ทดลองสร้างโค้ด Subcribe ข้อมูลจาก turtlesim ให้เปิด 5 terminal
    terminal 1. สั่ง $ roscore 
    terminal 2. สั่ง $ rosrun turtlesim turtlesim_node 
    terminal 3. สั่ง $ rostopic list
                   $ rostopic info /turtle1/pose
                   $ rostopic echo /turtle1/pose
    terminal 4. สั่ง $ cd catkin_ws/src/my_project/scripts
                   $ touch pose_subscriber.py
                   $ chmod +x pose_subscriber.py
                   $ cd ../..
                   $ code . แล้วเขียนโค้ด
                   $ rosrun my_project pose_subscriber.py
 
 11. ทดลองสร้างโค้ดผสม Pubish และ Subcribe เพื่อควบคุม turtlesim 
    terminal 1. สั่ง $ roscore 
    terminal 2. สั่ง $ rosrun turtlesim turtlesim_node 
    terminal 3. สั่ง $ cd catkin_ws/src/my_project/scripts
                   $ touch turtle_controller.py
                   $ chmod +x turtle_controller.py
                   $ cd ../..
                   $ code . แล้วเขียนโค้ด
                   $ rosrun my_project turtle_controller.py 

12. ทดลองใช้ ROS service เพื่อควบคุม turtlesim 
    terminal 1. สั่ง $ roscore 
    terminal 2. สั่ง $ rosrun turtlesim turtlesim_node 
    terminal 3. สั่ง $ rosservice list
                   $ rosservice info /turtle1/set_pen
                   $ rossrv show turtlesim/SetPen
                   $ rosservice call /turtle1/set_pen "{'r': 200, 'g': 0, 'b': 0, 'width': 4, 'off': 0}"
                   
    terminal 4. สั่ง $ rosrun turtlesim turtle_teleop_key

13. ทดลองสร้างโค้ดผสม Pubish Subcribe และ Service เพื่อควบคุม turtlesim 
    terminal 1. สั่ง $ roscore 
    terminal 2. สั่ง $ rosrun turtlesim turtlesim_node 
    terminal 3. สั่ง $ cd catkin_ws/src/my_project/scripts
                   $ touch mix_pub_sub_service.py
                   $ chmod +x mix_pub_sub_service.py
                   $ cd ../..
                   $ code . แล้วเขียนโค้ด
                   $ rosrun my_project mix_pub_sub_service.py               
