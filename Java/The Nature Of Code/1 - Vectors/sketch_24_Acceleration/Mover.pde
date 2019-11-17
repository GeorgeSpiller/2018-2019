class Mover {
  PVector location;
  PVector verlocity;
  PVector acceleration;

  Mover() {
    location = new PVector(width/2, height/2);
    verlocity = new PVector(0, -1);
    acceleration = new PVector(0.01, 0);
  }

  void update() {
    acceleration = PVector.random2D();
    verlocity.add(acceleration);
    location.add(verlocity);
    println(location.x, location.y);
    verlocity.limit(5);
  }

  void edges() {
    if (location.x > width) location.x = 0;
    if (location.x < 0) location.x = width;
    if (location.y > height) location.y = 0;
    if (location.y < 0) location.y = height;
  }

  void display() {
    fill(100);
    stroke(10);
    ellipse(location.x, location.y, 40, 40);
  }
}
