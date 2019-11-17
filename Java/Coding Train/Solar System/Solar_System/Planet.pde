class Planet {
  float radius;
  float angle;
  float distance;
  float orbitSpeed;
  PVector v;
  Planet[] planets;
  
  PShape globe; //used for textures

  Planet(float r, float d, float o, PImage img) {
    v = PVector.random3D();
    radius = r;
    distance = d;
    v.mult(distance);
    angle = random(TWO_PI);
    orbitSpeed = o;
    
    noStroke();
    noFill();
    globe = createShape(SPHERE,radius);
    globe.setTexture(img);
  }

  void orbit() {
    angle = angle + orbitSpeed;
    if (planets != null) {
      for (int i = 0; i < planets.length; i++) {
        planets[i].orbit();
      }
    }
  }

  void spawnMoons(int total, int level) {
    planets = new Planet[total];
    for (int i = 0; i < planets.length; i++) {
      float r = radius/(level*2);
      float d = random(radius + r, (radius + r)*4);
      float o = random(-5, 5) / d;
      if (abs(o) < 1){
      o = random(2, 5) / d;
      }
      int index = int(random(0, textures.length));
      planets[i] = new Planet(r, d, o, textures[index]);
      if (level < 3) {
        int num = int(random(0, 4 / level));
        planets[i].spawnMoons(num, level+1);
      }
    }
  }


  void show() {
    pushMatrix();
    noStroke();
    fill(255);

    PVector v2 = new PVector(1, 0, 1);
    PVector p = v.cross(v2);
    rotate(angle, p.x, p.y, p.z);

    translate(v.x, v.y, v.z);
    //ellipse(0, 0, radius*2, radius*2);
    shape(globe);
    //sphere(radius);
    if (planets != null) {
      for (int i = 0; i < planets.length; i++) {
        planets[i].show();
      }
    }
    popMatrix();
  }
}
