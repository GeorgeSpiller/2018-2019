
PImage img;
PImage sorted;
int index = 0;
int PivotLeft = 0;
int PivotRight; //defined in setup
boolean SwapMade = true;
String CurrPivot = "PivotLeft";



void setup() {
  size(1000, 500);
  img = loadImage("imageSmall.jpg");
  img.resize(500, 500);
  sorted = createImage(img.width, img.height, RGB);
  sorted = img.get();
  sorted.resize(500, 500);
  sorted.loadPixels();
  PivotRight = sorted.pixels.length - 1;
}

void draw() {
  print(PivotLeft); print(" | "); print(PivotRight); print(" | "); println(CurrPivot);  

  //  Quck Sort - Pivots
  //Get the first value (current value), itterate through the unsorted list and
  //place anything that is smaller than the current value to the left of it. Set
  //this value as a pivot, and then repeat for the next value.

  float PL_Bright = brightness(sorted.pixels[PivotLeft]);
  float PR_Bright = brightness(sorted.pixels[PivotRight]);


  if ((PivotLeft != PivotRight) && (SwapMade = true)) {
    SwapMade = false;

    if (CurrPivot == "PivotLeft") {
      //if the brightness(PivotLeft) > brightness(PivotRight) swap

      if (PL_Bright > PR_Bright) {
        //Swap PivotLeft with RightPivot
        color temp = sorted.pixels[PivotLeft];
        sorted.pixels[PivotLeft] = sorted.pixels[PivotRight];
        sorted.pixels[PivotRight] = temp;

        SwapMade = true;

        CurrPivot = "PivotRight";
      }
      PivotLeft = PivotLeft + 1;
    }//Pivot Chooser


    if (CurrPivot == "PivotRight") {
      //if the brightness(PivorRight) < brightness(PivotLeft) swap
      if (PR_Bright < PL_Bright) {
        //Swap PivotRight with whats behind it
        color temp = sorted.pixels[PivotRight];
        sorted.pixels[PivotRight] = sorted.pixels[PivotLeft];
        sorted.pixels[PivotLeft] = temp;
        SwapMade = true;

        CurrPivot = "PivotLeft";
      }
      PivotRight = PivotRight - 1;
    }//Pivot Chooser
  }
  if ((PivotLeft == PivotRight) && (SwapMade = true)) {
    //restart
    PivotLeft = -1;
    PivotRight = sorted.pixels.length;
  }





//    //Selection sort
//    float record = -1;
//    int selectedPixel = index;
//    for (int j = index; j < sorted.pixels.length; j ++) {
//      color pix = sorted.pixels[j];
//      float b = brightness(pix);
//      if (b >record) {
//        selectedPixel = j;
//        record = b;
//      }
//      //Swap Selected pixel with index
//      color temp = sorted.pixels[index];
//      sorted.pixels[index] = sorted.pixels[selectedPixel];
//      sorted.pixels[selectedPixel] = temp;
//    }

//    if (index < sorted.pixels.length - 1) {
//      index ++;
//    }

  sorted.updatePixels();

  background(0);
  image(img, 0, 0);
  image(sorted, 500, 0);
}
