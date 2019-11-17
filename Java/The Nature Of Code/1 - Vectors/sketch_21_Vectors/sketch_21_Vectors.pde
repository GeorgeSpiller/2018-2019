//What is a vector?
//Vector has, 
//1-magnitude
// 2-direction

//magnitude is the length, the size of the vecor
//the direction is obvs where it points
//direction could be represented by an angle reletive to a point

//vector could be eg, an arrow!
//a vector can be seperated into its components, x and y
//eg two points iether side of hypotanuse in a right angles triangle, 

//a vectors main use = to store a point with an x and a y value

ball[] ball = new ball[10];

void setup() {
  size(600, 500);
  for (int i = 0; i < ball.length; i++) {
    ball[i] = new ball();
  }
}

void draw() {
  background(255);
  
  for (int i = 0; i < ball.length; i++) {
    ball[i].move();
    ball[i].display();
  }
}
