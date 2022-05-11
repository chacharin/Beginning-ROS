# ROS-Setup

1. ติดตั้ง VMWare https://mailkmuttacth-my.sharepoint.com/:u:/g/personal/chacharin_lert_mail_kmutt_ac_th/EcJriInTdyVFhVROKO1TxxQBV7-VeZu-QNP1XYH_nTq60g?e=ZMe1Qd

2. ติดตั้ง Ubuntu https://releases.ubuntu.com/20.04.4/ubuntu-20.04.4-desktop-amd64.iso

3. ติดตั้ง ROS
  เปิด Terminal แล้วพิมพ์ทีละบรรทัด http://wiki.ros.org/noetic/Installation/Ubuntu
    (หาก EROR <bash: /opt/ros/noetic/setup.bash: No such file or directory> 
      ให้ใช้คำสั่ง gedit $HOME/.bashrc แล้วลบ /opt/ros/noetic/setup.bash ท้ายไฟล์)
 
4. ติดตั้ง Enviroment
  1. $ mkdir catkin_ws
  2. $ cd catkin_ws/
  3. $ mkdir src
  4. $ catkin_make
  5. $ source ~/catkin_ws/devel/setup.bash
  6. $ gedit ~/.bashrc
  7.เติม sourceใหม่  ใน  bashrc แล้ว save
  
5. สร้างไฟล์ python ใน ROS

   
