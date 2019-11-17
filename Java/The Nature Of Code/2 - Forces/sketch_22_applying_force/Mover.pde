class Mover {
  PVector location;
  PVector verlocity;
  PVector acceleration;


  Mover() {
    location = new PVector(width/2, height/2);
    verlocity = new PVector(0, 0);
    acceleration = new PVector(0, 0);
  }

  //Newons 2md Law (the beginning)
  void applyForce(PVector force) {
    acceleration.add(force);
  }

  void update() {   
    verlocity.add(acceleration);
    location.add(verlocity);
    //verlocity.limit(5);
  }

  void edges() {
    if (location.x > width) {
      location.x = width;
      verlocity.x *= -1;
    }
    if (location.y > height) {
      location.y = height;
      verlocity.y *= -1;
    }
    if (location.x < 0) {
      location.x = 0;
      verlocity.x *= -1;
    }
    if (location.y < 0) {
      location.y = 0;
      verlocity.y *= -1;
    }
  }

  void display() {
    fill(100);
    stroke(10);
    ellipse(location.x, location.y, 40, 40);
  }
}
