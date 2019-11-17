Mover m;

void setup() {
  size(400, 300);
  m = new Mover();
}

void draw() {
  background(255);
  m.update();
  m.edges();
  m.display();
}
