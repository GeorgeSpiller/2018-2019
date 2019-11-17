Mover[] movers;
ArrayList<Attractor> attractors;
boolean toggle;
float itemSize;

void setup() {
  size(600, 500);
  attractors = new ArrayList();
  movers = new Mover[5];
  for (int i = 0; i < movers.length; i++) {
    movers[i] = new Mover();
  }
}

void draw() {
  background(255);
  for (Mover m : movers) {
    ////// ADD GRAVITY ////////
    //PVector gravity = new PVector(0, 0.3);
    //gravity.mult(m.mass);
    //m.applyForce(gravity);
    ////if (mousePressed) {
    //PVector wind = new PVector(0.2, 0);
    //m.applyForce(wind);
    ////}

    //Drag
    PVector drag = m.verlocity.get();
    drag.normalize();
    float DragConstant = -0.001;
    float speed = m.verlocity.mag();
    drag.mult(DragConstant * speed * speed);
    m.applyForce(drag);  
    //}


    for (Attractor a : attractors) {
      PVector force = a.attract(m);
      m.applyForce(force);
      m.update();
      a.display();
    }

    m.update();
    m.edges();
    m.display();



    //////// ADD FORCE ///////
    //if (mousePressed) {
    ////Friction
    //PVector friction = m.verlocity.get();
    //friction.normalize();
    //float c = -0.1;
    //friction.mult(c);
    //m.applyForce(friction);
  }//end of movers loop

  if (mousePressed) {
    itemSize += 0.1;
  }
}//end of draw

void mouseReleased() {
  println(itemSize);
  attractors.add(new Attractor(itemSize));
  itemSize = 0;
}
