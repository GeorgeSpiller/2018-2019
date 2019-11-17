float tx = 0;
float ty = 50;
void setup() {
  size(600, 400);
}

void draw() {
  background(0);
  fill(255);
  
  tx = tx + 0.01;
  ty = ty + 0.01;
  
  float x = noise(tx);
  float y = noise(ty);
  
  x = map(x, 0, 1, 0 , width);
  y = map(y, 0, 1, 0 , height);
  ellipse(x, y, 40, 40);
}
