# ROS-Setup

1. ติดตั้ง VMWare https://mailkmuttacth-my.sharepoint.com/:u:/g/personal/chacharin_lert_mail_kmutt_ac_th/EcJriInTdyVFhVROKO1TxxQBV7-VeZu-QNP1XYH_nTq60g?e=ZMe1Qd

2. ติดตั้ง Ubuntu https://releases.ubuntu.com/20.04.4/ubuntu-20.04.4-desktop-amd64.iso

3. ติดตั้ง ROS
  เปิด Terminal แล้วพิมพ์ทีละบรรทัด http://wiki.ros.org/noetic/Installation/Ubuntu
    (หาก EROR <bash: /opt/ros/noetic/setup.bash: No such file or directory> 
      ให้ใช้คำสั่ง gedit $HOME/.bashrc แล้วลบ /opt/ros/noetic/setup.bash ท้ายไฟล์)
 
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
    $ catkin_create_pkg my_project rospy turtlesim
    $ sudo snap install code --classic
    $ catkin_make
    
7. สร้าง Node ด้วย python ใน ROS
    $ cd catkin_ws/src/my_project
    $ mkdir scripts
    $ cd scripts
    $ touch one.py
    $ chmod +x one.py
    $ cd --
    $ cd catkin_ws/src
    $ code .
    จากนั้นเขียนโค้ดใน VS code
    
8. ทดสอบเรียกใช้ไฟล์ Node ที่สร้างขึ้น ให้เปิด 3 terinal 
    terminal 1. สั่ง $ rosrun ด้วย new terminal 
    terminal2.  สั่ง $ rosrun my_project one.py
    terminal3.  สั่ง $ rosnode list (  และทดสอบ $ rosnode kill /node_one)
    #ใช้ $ rqt_graph ดู Model Node Link
    
    

   
