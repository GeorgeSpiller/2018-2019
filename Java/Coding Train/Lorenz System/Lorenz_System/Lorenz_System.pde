import peasy.*;
PeasyCam camera;

float x = 0.01;
float y = 0;
float z = 0;

 float a = 10;
 float b = 28;
 float c = 8.0 / 3.0;

/* 
 Other known constants for more cool shapes:
 float a = 10;
 float b = 28;
 float c = 8.0 / 3.0;
 
 float a = 10;
 float b = 28;
 float c = 10;
 
 float a = 28;
 float b = 46.92;
 float c = 4;
 */


//Dynamic array that stores vector values
ArrayList<PVector> points = new ArrayList<PVector>();


//dx = change in x, dt = change in time
// (dx / dt) = a(y - x)
// (dy / dt) = x(b - z) - y
// (dz / dt) = x * y - c * z

void setup() {
  size(800, 600, P3D);
  colorMode(HSB);
  camera = new PeasyCam(this, 0, 0, 0, 800);
}

void draw() {
  background(0);
  //Each loop over draw increases time, but inorder
  //to draww a smooth line we cant use the time in
  //the diferential function (or the line will be too
  //jagged) - so we difine a new dt (change in time)
  float dt = 0.01;
  // To incorporate our draw time in the equations, 
  //we multiply it to the formulars at the end:

  //first differential equation to set how x changes
  float dx = (a * (y - x)) * dt;
  //Second differential equation to set how y changes
  float dy = (x * (b - z) - y) * dt;
  //Third differential equation to set how z changes
  float dz = (x * y - c * z) * dt;
  x = x + dx; //update x
  y = y + dy; //update y
  z = z + dz; //update z

  //add vector values to the dynamic array
  points.add(new PVector(x, y, z));

  //translate(width/2,height/2);
  scale(4);
  stroke(255);
  noFill();

  float hue = 0;
  beginShape();
  //for every vector in points
  for (PVector v : points) {
    stroke(hue, 255, 255);
    vertex(v.x, v.y, v.z);
    hue += 0.1;
    if (hue > 255) {
      hue = 0;
    }
  }
  endShape();

  println(x, y, z);
}
