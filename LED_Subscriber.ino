#include <ros.h>
#include <std_msgs/Int16.h>
 
ros::NodeHandle  nh;
 
void LED13( const std_msgs::Int16 & cmd_msg)
{
  int cmd = cmd_msg.data; 
  digitalWrite(13, cmd);  
}

ros::Subscriber<std_msgs::Int16> sub("LED_Control_Topic", LED13);
 
void setup()
{
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);

}
 
void loop()
{
  nh.spinOnce();
  delay(1);
}
