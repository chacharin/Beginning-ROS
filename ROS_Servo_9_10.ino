#include <Servo.h> 
#include <ros.h>
#include <std_msgs/Int16.h>
 
ros::NodeHandle  nh;
 
Servo servo_9;
Servo servo_10;

 
void s_9( const std_msgs::Int16& cmd_msg)
{
  servo_1.write(cmd_msg.data); 
}
 
void s_10( const std_msgs::Int16& cmd_msg)
}
  servo_2.write(cmd_msg.data); 
}
 
ros::Subscriber<std_msgs::Int16> sub_1("Topic_servo_9", s_9);
ros::Subscriber<std_msgs::Int16> sub_2("Topic_servo_10", s_10);

 
void setup()
{
  servo_9.attach(9); 
  servo_10.attach(10); 
 
  nh.initNode();
  nh.subscribe(sub_1);
  nh.subscribe(sub_2);
}
 
void loop()
{
  nh.spinOnce();
  delay(1);
}
