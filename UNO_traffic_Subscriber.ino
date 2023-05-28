#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle nh;

void callback_R(const std_msgs::Int16 &recive_msg)
{
  if (recive_msg.data == 0) {digitalWrite(13, 0); }
  else if (recive_msg.data == 1) {digitalWrite(13,1);}
}

void callback_Y(const std_msgs::Int16 &recive_msg)
{
  if (recive_msg.data == 0) {digitalWrite(12, 0); }
  else if (recive_msg.data == 1) {digitalWrite(12,1);}
}

void callback_G(const std_msgs::Int16 &recive_msg)
{
  if (recive_msg.data == 0) {digitalWrite(11, 0); }
  else if (recive_msg.data == 1) {digitalWrite(11,1);}
}

ros::Subscriber<std_msgs::Int16> sub_R("/red", &callback_R);
ros::Subscriber<std_msgs::Int16> sub_Y("/yellow", &callback_Y);
ros::Subscriber<std_msgs::Int16> sub_G("/green", &callback_G);

void setup() {
 pinMode(13,OUTPUT);  pinMode(12,OUTPUT);  pinMode(11,OUTPUT);
 nh.initNode();
 nh.subscribe(sub_R);  nh.subscribe(sub_Y);  nh.subscribe(sub_G);
}

void loop() {
  delay(1);
  nh.spinOnce();
}
