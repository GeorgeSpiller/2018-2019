Walker w1;
Walker w2;
Walker w3;
void setup() {
  size(800, 600);
  w1 = new Walker();
  w2 = new Walker();
  w3 = new Walker();
  background(255);
}

void draw() {
  w1.walk();
  w1.display();
  w2.walk();
  w2.display();
  w3.walk();
  w3.display();
}
