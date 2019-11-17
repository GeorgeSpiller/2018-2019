float a = 0.0;
float aVerlocity = 0.0;
float aAcceleration = 0.0;

void setup() {
  size(630, 360);
}

void draw() {
  background(255);

  aAcceleration = map(mouseX, 0, width, -0.001, 0.001);


  //how forces work
  a += aVerlocity;
  aVerlocity += aAcceleration;

  rectMode(CENTER);
  stroke(0);
  fill(127);
  //rotation always happeneds around the point
  //of origin (0,0 the top left corner)
  //so if we have
  //rotate(PI/4) (its PI/4 cuz we work in radials instead of degrees, one radial is a length of the circumfrance of a circle that is equal to the circles radius)
  //the rectangle would be rotated off screen
  //so to get around this we translate the origin(the pen) to 
  //the center of the rectangle

  translate(width/2, height/2);
  //rotate(PI/4);
  rotate(a);
  rect(0, 0, 64, 36);
}
