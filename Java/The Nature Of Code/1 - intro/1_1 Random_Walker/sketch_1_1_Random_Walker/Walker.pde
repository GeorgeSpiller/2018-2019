class Walker {

  int x;
  int y;
  float choice;
  Walker() {
    x = width /2;
    y = height / 2;
  }

  void walk() {
    choice = int(random(4));
    if (choice == 0) {
      x++;
    } else if (choice == 1) {
      x--;
    } else if (choice == 2) {
      y++;
    } else {
      y--;
    }
    
    x = constrain(x,0,width-1);
    y = constrain(y,0,height-1);
  }//end step

  void display() {
    stroke(0);
    point(x, y);
  }
}//end class
