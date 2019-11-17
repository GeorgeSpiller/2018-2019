class Attractor {
  PVector location;

  float mass;
  float G;

  Attractor(float size) {
    size = constrain(size, 1, 8);
    location = new PVector(mouseX, mouseY);
    mass = size; //mass = random(0.5, 4);
    G = 1;
  }

  PVector attract (Mover m) {
    //Direction of the force
    PVector force = PVector.sub(location, m.location);
    float d = force.mag();
    force.normalize();

    d = constrain(d, 5, 25);

    //Magnitude (strength) of the force
    float strength = (G * mass * m.mass) / (d * d);

    //putting mag and dir together
    force.mult(strength);

    return force;
  }

  void display() {
    fill(127, 100);
    stroke(10);
    ellipse(location.x, location.y, mass*20, mass*20);
  }
}
