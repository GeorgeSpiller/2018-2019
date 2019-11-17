class Mover {
  PVector location;
  PVector verlocity;
  PVector acceleration;

  float mass;

  Mover() {
    location = new PVector(random(width), height/2);
    verlocity = new PVector(0, 0);
    acceleration = new PVector(0, 0);
    mass = random(0.5, 4);
  }

  //Newons 2md Law with mass
  void applyForce(PVector force) {
    PVector f = PVector.div(force, mass);
    acceleration.add(f);
  }

  void update() {   
    verlocity.add(acceleration);
    location.add(verlocity);
    //verlocity.limit(5);
    acceleration.mult(0);//as each fram is a newmoent in time
  }

  void applyFriction(float fricForce) {
    //fricForce = -0.1;
    PVector friction = verlocity.get();
    friction.normalize();
    friction.mult(-1);// if fricforce is possitive
    friction.mult(fricForce);
    applyForce(friction);
  }

  void edges() {
    float edgeFriction = 1.5;
    int t = 0;
    if (location.x > width) {
      location.x = width -10;
      verlocity.x *= -1;
      t = 100;
    }
    if (location.y > height) {
      location.y = height -10;
      t = 100;
      verlocity.y *= -1;
    }
    if (location.x < 0) {
      location.x = 10;
      t = 100;
      verlocity.x *= -1;
    }
    if (location.y < 0) {
      location.y = 10;
      t = 100;
      verlocity.y *= -1;
    }

  

  }

  void display() {
    fill(127, 100);
    stroke(10);
    ellipse(location.x, location.y, mass*20, mass*20);
  }
}
