
float[] vals;
float[] norms;

void setup() {
  size(400, 300);
  vals = new float[width];
  norms = new float[width];
}

void draw() {
  background(100);

  //Pick a random number
  float n = montecarlo();

  int index = int(n*width);
  vals[index]++;
  stroke(255);

  boolean normalization = false;
  float maxy = 0.0;

  //Draww Graph based on values in norms array

  for (int x = 0; x < vals.length; x++) {
    line(x, height, x, height-norms[x]);
    if (vals[x] > height) normalization = true;
    if (vals[x] > maxy) maxy = vals[x];
  }
  //if normalization is true then normalize to height
  //otherwize just copy theinfo
  for (int x = 0; x < vals.length; x++) {
    if (normalization) norms[x] = (vals[x] / maxy * (height));
    else norms[x] = vals[x];
  }
}
// Probability deturmined by formular y = x
float montecarlo() {
  //have we found one yet
  boolean foundone = false;
  int hack = 0; // counter
  while (!foundone && hack < 10000) {
    //pick two random numbers
    float r1 = (float) random(1);
    float r2 = (float) random(1);
    float y = r1*r1;//y=x*x (the equation that will be drawn)
    //if r2 is valid, use it
    if (r2 < y) {
      foundone = true;
      return r1;
    }
    hack ++;
  }
  //hack in case we run into a problem
  return 0;
}
