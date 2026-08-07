/* 
  Part 4: Implementing an Algorithm
  Brennon York
  01/29/2026
  byork8@my.gcu.edu or yorkbrennon7@gmail.com
*/

void setup() 
{
  // start serial port
  Serial.begin(115200);
  while(!Serial);
  Serial.println("===Program Start===");
  // generate array n = 50 , 0 > x > 500
  int myArray[50];
  randomSeed(analogRead(A0));
  for(int i = 0; i < 50; i++)
  {
    myArray[i] = random(1,501);
  }
  Serial.println("Unordered set: ");
  for(int i = 0; i < 50; i++)
  {
    Serial.print(myArray[i]);
    Serial.print(", ");
  }

  // setup variables
  int numChanges = 0;
  int pos = 0;
  bool arrayOrdered = 0;

  while(arrayOrdered == 0)
  {
    for(pos = 0; pos < 49; pos++)
    {
      // compare pos and pos + 1
      if(myArray[pos] > myArray[pos+1])
      {
        // swap values and numChanges++ if needed
        int tempVal = myArray[pos+1];
        myArray[pos+1] = myArray[pos];
        myArray[pos] = tempVal;
        numChanges++;
      }
    }
      // determine numChanges = 0 
    if(numChanges == 0) {arrayOrdered =1;} 
    else{numChanges = 0;}
  }
  // print results
  Serial.println("");
  Serial.println("Ordered Set: ");
  for(int i = 0; i < 50; i++)
  {
    Serial.print(myArray[i]);
    Serial.print(", ");
  }
}

void loop() 
{
  // not needed
}
