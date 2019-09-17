using System;
using System.Collections.Generic;

public class Powerball
{
  // generates 5 unique random numbers between 1 and 69
  static void Main(string[] args)
  {
    Dictionary<int, int> nums = new Dictionary<int, int>();

    while (nums.Count < 6)
    {
      int randomNum = new Random().Next(1, 69);

      nums[randomNum] = randomNum;
    }

    foreach (var item in nums)
    {
      System.Console.WriteLine($"{item.Key}, {item.Value}");
    }
  }
}
