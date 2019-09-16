using System;
using System.Linq;

public class Program
{

  public static int NumJewelsInStones(string J, string S)
  {
    // using Linq
    return S.Count(stone => J.Contains(stone));
  }

  static void Main(string[] args)
  {
    string J = "aA";
    string S = "aAAbbbb";

    var res = NumJewelsInStones(J, S);
    System.Console.WriteLine(res);
  }
}
