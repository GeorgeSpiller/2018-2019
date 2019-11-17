//Cartisan space is a space where we use (x,y) coordinates to dictate where points are on the screen
// Polar coordinates uses, instead of (x,y), they use (r, theta)
// r is the radius that goes from the origin (in cartisan (0,0) towards the point, and theta (just another
//way of saying angle), is that angle between the x axsis and the r line (r,theta)

//just go to https://www.youtube.com/watch?v=znOBmOrtz_M&list=PLRqwX-V7Uu6bR4BcLjHHTopXItSjRA7yG&index=2&ab_channel=TheCodingTrain
// time stap 7:36


float r = 50;
float theta = 0.0;
float aVel = 0.0;
float aAcc = 0.001;

void setup() {
  size(640, 360);
} 

void draw() {
  background(0);
  translate(width/2, height/2);

  r = mouseX/5;

  float y = r * sin(theta);
  float x = r * cos(theta);
  fill(255);
  stroke(255);
  line(0,0,x,y);
  ellipse(x, y, 50, 50);
  
  theta += aVel;
  aVel += aAcc;
  aVel = constrain(aVel,0,0.3);
}
