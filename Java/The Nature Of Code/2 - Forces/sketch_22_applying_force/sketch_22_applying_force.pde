Mover m;

void setup() {
  size(600, 500);
  m = new Mover();
}

void draw() {
  background(255);
  
  PVector gravity = new PVector(0, -0.3);
  PVector wind = new PVector(0.2, 0);
  m.applyForce(gravity);
  m.applyForce(wind);
  
  
  m.update();
  m.edges();
  m.display();
}
