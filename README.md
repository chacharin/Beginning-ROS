# ROS-Setup

1. ติดตั้ง VMWare https://mailkmuttacth-my.sharepoint.com/:u:/g/personal/chacharin_lert_mail_kmutt_ac_th/EcJriInTdyVFhVROKO1TxxQBV7-VeZu-QNP1XYH_nTq60g?e=ZMe1Qd

2. ติดตั้ง Ubuntu https://ubuntu.com/download/desktop/thank-you?version=22.04&architecture=amd64

3. ติดตั้ง ROS Melodic
  เปิด Terminal แล้วพิมพ์ทัละบรรทัด http://wiki.ros.org/noetic/Installation/Ubuntu
    (หาก EROR """bash: /opt/ros/noetic/setup.bash: No such file or directory"""  
      ให้ใช้คำสั่ง gedit $HOME/.bashrc แล้วลบ """/opt/ros/noetic/setup.bash""" ท้ายไฟล์)
 
4. ติดตั้ง Enviroment
  เปิด Terminal แล้วพิมพ์ทัละบรรทัด http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment
   (sudo apt-get install python-rosinstall ก่อน)

คำสั่งใช้ประจำ
  1. source devel/setup.bash
  2. chmod +x <file.py>
  3. rosrun <folder> <file.py> เช่น rosrun beginner_tutorials talker.py หรือ rosrun beginner_tutorials talker.py
  4. 

   
