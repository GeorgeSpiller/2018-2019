class Ball {

  PVector location;
  PVector verlocity;

  Ball() {
    location = new PVector(random(10, width - 10), random(10, height - 10));
    verlocity = new PVector(random(1, 5), random(1, 5));
    
  }
  
  void move() {
    if ((location.x > width -10) || (location.x < 10)) {
      verlocity.x *= -1; //flip sign of value
    } else if ((location.y > height -10) || (location.y < 10)){
      verlocity.y *= -1; //flip sign of value
    }

    location.add(verlocity);
  }

  void display() {
    fill(100);
    stroke(10);
    ellipse(location.x, location.y, 40, 40);
  }
}
