# ROS-Setup

1. ติดตั้ง VMWare https://mailkmuttacth-my.sharepoint.com/:u:/g/personal/chacharin_lert_mail_kmutt_ac_th/EcJriInTdyVFhVROKO1TxxQBV7-VeZu-QNP1XYH_nTq60g?e=ZMe1Qd

2. ติดตั้ง Ubuntu https://releases.ubuntu.com/20.04.4/ubuntu-20.04.4-desktop-amd64.iso

3. ติดตั้ง ROS
  เปิด Terminal แล้วพิมพ์ทัละบรรทัด http://wiki.ros.org/noetic/Installation/Ubuntu
    (หาก EROR """bash: /opt/ros/noetic/setup.bash: No such file or directory"""  
      ให้ใช้คำสั่ง gedit $HOME/.bashrc แล้วลบ """/opt/ros/noetic/setup.bash""" ท้ายไฟล์)
 
4. ติดตั้ง Enviroment
  home:$ mkdir catkin_ws
  home:$ cd catkin_ws/
  home:~/catkin_ws $ mkdir src
  home:~/catkin_ws $ catkin_make
  home:$ source ~/catkin_ws/devel/setup.bash
  home:$ gedit ~/.bashrc
  เติม sourceใหม่  ใน  bashrc แล้ว save
  
5. สร้างไฟล์ python ใน ROS

   
