
void setup() {
  size(500, 300);
  // We look at:
  //add(sub)
  //mult(div) 'scale'
  //magnitude mag()
  //normalize()
}

void draw() {
  background(255);
  strokeWeight(2);
  stroke(0);
  noFill();

  translate(width/2, height/2);
  ellipse(0, 0, 4, 4);

  PVector mouse = new PVector(mouseX, mouseY);
  PVector centre = new PVector(width / 2, height/2);
  PVector mouseopp = new PVector(mouseX, mouseY);

  //SUB
  mouse.sub(centre);
  //we need to sub here as all the vectors are drawm from the origin (0,0)
  //comment out the sub to see
  //Examples:
  line(0, 0, mouse.x, mouse.y);
  //the (0, 0) is not the top left due to the translate
  ellipse(mouse.x, mouse.y, 5, 5);

  //MULT:
  mouse.mult(2); // this scales the vector * 2
  //so in effect its twice as long
  //mouse.mult(0.5) //will make it half as long
  stroke(255, 0, 0);
  line(0, 0, mouse.x, mouse.y);

  //MAG basically 'length'
  //gets the length of the vector through pithagros (spell?)
  // a2 + b2 = c2
  //where a and b are x and y, and c is the vector
  //do really need to know all that but there you go ^^

  float m = mouse.mag();
  //rectangle changs based on the magnitude of the vector(or length of the vector)
  rect(0, 0, m, 20);

  //normalize
  //normalizing a vector is taking its length (mag) and setting
  //it to a fixed value (default 1)
  //although 1 is small so we mult() so we can see it
  mouseopp.sub(centre);
  stroke(0, 0, 255);
  
  mouseopp.normalize();// this normalize and mult is 
  mouseopp.mult(50);//used alot so there is a function
  //called setmag(), which does this:
  
  mouseopp.setMag(50); // does the same
  
  line(0, 0, mouseopp.x, mouseopp.y);
}
