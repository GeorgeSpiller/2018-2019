class Walker {
  float x, y;
  float choice;

  Walker() {
    x = width / 2;
    y = height / 2;
  }

  void walk() {
    choice = random(1);
    if (choice < 0.3) {
      x++;
    } else if (choice < 0.6) {
      x--;
    } else if (choice < 0.8) {
      y++;
    } else {
      y--;
    }//end if


    x = constrain(x, 0, width-1);
    y = constrain(y, 0, height-1);
  }//end walk


  void display() {
    stroke(0);
    point(x, y);
  }// end display
}//end class
