#include "myfoods.h"

String getFruit(String c, String sz)
{
  int num = random(0, 10);

  if (c == "red" && sz == "medium") {
    if (num < 5) return "apple";
    else return "mango";
  }

  if (c == "green" && sz == "small") {
    if (num < 5) return "grape";
    else return "baby plantain";
  }

  if (c == "yellow" && sz == "large") {
    if (num < 3) return "banana";
    else if (num == 4 || num == 5) return "durian";
    else return "honeydew melon";
  }

  return "mystery fruit";
}

String getVeg(String c, String sz)
{
  int num = random(0, 10);

  if (c == "red" && sz == "medium") {
    if (num < 5) return "red bell pepper";
    else return "red cabbage";
  }

  if (c == "green" && sz == "small") {
    if (num < 5) return "baby broccoli";
    else return "pea";
  }

  if (c == "purple" && sz == "medium") {
    if (num < 3) return "eggplant";
    else if (num == 4 || num == 5) return "asian eggplant";
    else return "pac choy";
  }

  return "mystery vegetable";
}

String getStarch(String c, String sz)
{
  int num = random(0, 10);

  if (c == "red" && sz == "medium") {
    if (num < 5) return "yam";
    else return "kidney beans";
  }

  if (c == "brown" && sz == "small") {
    if (num < 5) return "potato";
    else return "lentils";
  }

  if (c == "yellow" && sz == "medium") {
    if (num < 3) return "yukon gold potato";
    else if (num == 4 || num == 5) return "polenta";
    else return "french bread";
  }

  return "mystery starch";
}