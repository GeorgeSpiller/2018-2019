import peasy.*;

Planet sun;
PeasyCam cam;

PImage sunTex;
PImage background;
PImage[] textures = new PImage[12];
float xoff = 0.0;


void setup() {
  size(600, 600, P3D);
  sunTex = loadImage("Sun1.jpeg");
  textures[0] = loadImage("Earth.jpeg");
  textures[1] = loadImage("Earth2.jpeg");
  textures[2] = loadImage("Planet.jpeg");
  textures[3] = loadImage("Planet1.jpeg");
  textures[4] = loadImage("Planet2.jpeg");
  textures[5] = loadImage("Planet3.jpeg");
  textures[6] = loadImage("Planet4.jpeg");
  textures[7] = loadImage("Planet5.jpeg");
  textures[8] = loadImage("Planet6.jpeg");
  textures[9] = loadImage("Planet7.jpeg");
  textures[10] = loadImage("Moon1.jpeg");
  textures[11] = loadImage("Moon2.jpeg");
  background = loadImage("Space.jpg");


  sun = new Planet(50, 0, 0, sunTex);
  sun.spawnMoons(5, 1);
  cam = new PeasyCam(this, 500);
}

void draw() {
  //lights(); //generic light function that makes filled 3d stuff look more 3d

  xoff = xoff + 0.005;
  float hue = noise(xoff)*310;
  if (hue > 255) {
    hue = 255;
  } else if (hue < 150) {
    hue = 150;
  }
  println(hue);


  float dir = 50 * 4;
  int angle = 0;
  spotLight(hue, hue, hue, dir, 0, 0, -1, 0, 0, angle, 0);
  spotLight(hue, hue, hue, -dir, 0, 0, 1, 0, 0, angle, 0);
  spotLight(hue, hue, hue, 0, dir, 0, -1, 0, 0, angle, 0);
  spotLight(hue, hue, hue, 0, -dir, 0, 0, 1, 0, angle, 0);
  spotLight(hue, hue, hue, 0, 0, dir, 0, -1, 0, angle, 0);
  spotLight(hue, hue, hue, 0, 0, -dir, 0, 0, 1, angle, 0);
  pointLight(hue, hue, hue, 0, 0, 0); //light out from the sun

  background(background);
  sun.show();
  sun.orbit();
}
