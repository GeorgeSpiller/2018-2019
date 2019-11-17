class ball {
  float x = random(10, width - 10);
  float y = random(10, height - 10);
  float xspeed = random(1, 5);
  float yspeed = random(1, 5);


  void move() {
    if (x > width -10) {
      xspeed--;
    } else if (x < 10) {
      xspeed++;
    } else if (y > height -10) {
      yspeed--;
    } else if (y < 10) {
      yspeed++;
    }
    x = x + xspeed;
    y = y + yspeed;
  }

  void display() {
    fill(100);
    stroke(10);
    ellipse(x, y, 40, 40);
  }
}
