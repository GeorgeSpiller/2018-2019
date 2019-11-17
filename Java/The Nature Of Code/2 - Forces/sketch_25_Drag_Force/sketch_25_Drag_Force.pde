Mover[] movers;

void setup() {
  size(600, 500);
  movers = new Mover[5];
  for (int i = 0; i < movers.length; i++) {
    movers[i] = new Mover();
  }
}

void draw() {
  background(255);

  for (Mover m : movers) {

    PVector gravity = new PVector(0, 0.3);
    gravity.mult(m.mass);
    m.applyForce(gravity);
    //if (mousePressed) {
    PVector wind = new PVector(0.2, 0);
    m.applyForce(wind);
    //}

    if (mousePressed) {
      ////Friction
      //PVector friction = m.verlocity.get();
      //friction.normalize();
      //float c = -0.1;
      //friction.mult(c);
      //m.applyForce(friction);
      
      //Drag
      PVector drag = m.verlocity.get();
      drag.normalize();
      float DragConstant = -0.03;
      float speed = m.verlocity.mag();
      drag.mult(DragConstant * speed * speed);
      m.applyForce(drag);  
    }

    m.update();
    m.edges();
    m.display();
  }
}
