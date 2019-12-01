boid[] boids = new boid[100]; //<>//
HScrollbar SF_dir, SF_cen, SF_avd, ViewDis;

float SliderDIR;
float SliderCEN;
float SliderAVD;
float SliderVWD;

void setup() {
  size(800, 600);
  for (int i = 0; i < boids.length; i++) {
    boids[i] = new boid();
  }
  SF_dir = new HScrollbar(0, height-10, width/2-5, 16, 16);
  SF_cen = new HScrollbar(0, height-30, width/2-5, 16, 16);
  SF_avd = new HScrollbar(width/2+5, height-10, width/2, 16, 16);
  ViewDis = new HScrollbar(width/2+5, height-30, width/2, 16, 16);
}

void draw() {
  background(255);
  final int SPEED = 2;

  //map the slidervals to the vals they are changing
  // change the vals through the (uncoded) functions in boids
  SliderDIR = map(SF_dir.getPos(), 0, width/2-5, 0.01, 0.3);
  SliderCEN = map(SF_cen.getPos(), 0, width/2-5, 0.1, 1);
  SliderAVD = map(SF_avd.getPos(), width/2+5, width, 0.01, 0.5);
  SliderVWD = map(ViewDis.getPos(), ((width/2)+5), width, 5, 100);

  for (int i =0; i < boids.length; i++) {
    for (int j = 0; j < boids.length; j++) {
      if (boids[i] != boids[j]) {
        boids[i].SetSF_dir(SliderDIR);
        boids[i].SetSF_cen(SliderCEN);
        boids[i].SetSF_avd(SliderAVD);
        boids[i].SetViewDis(SliderVWD);

        boids[i].avoidBoids(boids[j]);
        boids[i].Get_NrbyBoidDirection(boids[j]);
        boids[i].Get_NrbyBoidCentre(boids[j]);
      }
    }
    boids[i].Steer_NrbyBoidDirection();
    boids[i].Steer_NrbyBoidCentre();
    boids[i].move(SPEED);


    boids[i].edges();
    boids[i].show();

    SF_dir.update();
    SF_cen.update();
    SF_avd.update();
    ViewDis.update();

    SF_dir.display();
    SF_cen.display();
    SF_avd.display();
    ViewDis.display();

    textSize(14);
    fill(255, 255, 255);
    String str = "SF_dir: " + SliderDIR;
    text(str, 5, height-5); 
    str = "SF_cen: " + SliderCEN;
    text(str, 5, height-25); 
    str = "SF_avd: " + SliderAVD;
    text(str, width/2+10, height-5); 
    str = "ViewDis: " + SliderVWD;
    text(str, width/2+10, height-25);
  }
}
