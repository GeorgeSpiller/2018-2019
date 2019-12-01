class boid {
  PVector loc;
  PVector direction;
  PVector steer;
  float viewDistance;
  color fillval;

  PVector NrbyBoid_NetDirection;
  PVector NrbyBoid_NetPos;
  PVector NrbyBoid_SumPos;
  float NrbyBoid_Total;

  float Dir_SteerForce;
  float Cen_SteerForce;
  float Avd_SteerForce;


  boid() {
    loc = new PVector(random(width), random(height));
    direction = new PVector(random(width) - random(width), random(height) - random(height));
    steer = new PVector();
    viewDistance = 50; 
    fillval = color(random(20, 60), random(140, 180), random(210, 250)); //40, 160, 230

    NrbyBoid_NetDirection = new PVector(0, 0); //Net direction of nearby boids
    NrbyBoid_NetPos = new PVector(0, 0);       //Net possition of nearby boids (final: SumPos / total)
    NrbyBoid_SumPos = new PVector(0, 0);       //All nearby posstions added together
    NrbyBoid_Total = 0;

    Dir_SteerForce = 0.1; 
    Cen_SteerForce = 0.4; 
    Avd_SteerForce = 0.08;
  }

  void SetSF_dir(float val) {
    Dir_SteerForce = val;
  }
  void SetSF_cen(float val) {
    Cen_SteerForce = val;
  }
  void SetSF_avd(float val) {
    Avd_SteerForce = val;
  }
  void SetViewDis(float val) {
    viewDistance = val;
  }

  void Get_NrbyBoidCentre(boid boid2) {
    // get the common distance of nearby boids
    if (dist(loc.x, loc.y, 0, boid2.loc.x, boid2.loc.y, 0) < viewDistance) {
      NrbyBoid_SumPos.add(boid2.loc);
      NrbyBoid_Total++;
      //to remove
      NrbyBoid_SumPos.set(boid2.loc);
    }
  }

  void Steer_NrbyBoidCentre() {
    //if (dist(loc.x, loc.y, 0, boid2.loc.x, boid2.loc.y, 0) < viewDistance) {
    //ellipse(NrbyBoid_SumPos.x, NrbyBoid_SumPos.y, 8, 8);
    //NrbyBoid_SumPos.setMag(10);
    if (NrbyBoid_Total > 0) {
      //NrbyBoid_SumPos.add(loc);
      //NrbyBoid_SumPos.div(NrbyBoid_Total);
      steer.set(PVector.sub(NrbyBoid_SumPos, loc));
      //ellipse(steer.x, steer.y, 8, 8);
      //println(steer);
    } else {
      NrbyBoid_SumPos = new PVector(0, 0);
    }
    
    // magnitued of the steer vector is the turn speed of the boid
    direction.add(steer.setMag(Cen_SteerForce));
    NrbyBoid_Total = 0;
    //}
  }

  //##########################################################################

  void Get_NrbyBoidDirection(boid boid2) { 
    if (dist(loc.x, loc.y, 0, boid2.loc.x, boid2.loc.y, 0) < viewDistance) {
      // get average location
      NrbyBoid_NetDirection.set(PVector.add(NrbyBoid_NetDirection, boid2.direction));
    }
  }

  void Steer_NrbyBoidDirection() {
    // for all boids within view distance
    // try to move torwars their direction
    //NrbyBoid_NetDirection.setMag(0.5);
    steer.set(PVector.sub(NrbyBoid_NetDirection, direction));
    //print(steer);
    //println(loc);
    // magnitued of the steer vector is the turn speed of the boid
    direction.add(steer.setMag(Dir_SteerForce));
  }

  void avoidBoids(boid boid2) { 
    // if within viewDistance of another boid
    if (dist(loc.x, loc.y, 0, boid2.loc.x, boid2.loc.y, 0) < viewDistance) {
      // steering force = desired location - current verlocity
      PVector desiredLoc = new PVector();
      desiredLoc.set(PVector.sub(loc, boid2.loc));
      steer.set(PVector.sub(desiredLoc, direction));
      // magnitued of the steer vector is the turn speed of the boid
      direction.add(steer.setMag(Avd_SteerForce));
    }
  }

  void move(int speed) {
    loc.add(direction.setMag(speed));
  }

  void edges() {
    if (loc.x > width) loc.x = 3;
    if (loc.x < 0) loc.x = width - 3;
    if (loc.y > height) loc.y = 3;
    if (loc.y < 0) loc.y = height - 3;
  }

  void show() {
    stroke(40, 130, 160);
    fill(fillval);
    pushMatrix();
    translate(loc.x, loc.y);
    rotate(direction.heading());
    triangle(0, 0, -15, 5, -15, -5);
    popMatrix();

    noFill();
    
    //ellipse(loc.x, loc.y, viewDistance, viewDistance); // View Distance
  }
}
