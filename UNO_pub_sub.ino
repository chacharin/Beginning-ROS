#include <ros.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Int16.h>

ros::NodeHandle nh; 
std_msgs::Float32 myData;
ros::Publisher pub("/arduino_pub", &myData);


void callback( const std_msgs::Int16 &recived_msg){
  if(recived_msg.data == 0){digitalWrite(13, 0);}   
  else if (recived_msg.data == 1){digitalWrite(13, 1);}  
}
ros::Subscriber<std_msgs::Int16> sub("/arduino_sub", &callback);


void setup() {
   pinMode(13, OUTPUT);
   pinMode(A0,INPUT);
   nh.initNode();
   nh.subscribe(sub);
   nh.advertise(pub);
}
 
void loop() {
    myData.data = analogRead(A0);
    pub.publish(&myData);
    delay(100);
    nh.spinOnce();
}
