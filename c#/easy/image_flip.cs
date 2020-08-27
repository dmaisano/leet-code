// https://leetcode.com/problems/flipping-an-image/solution/

using System;

public class Program
{
  public int[][] FlipAndInvertImage(int[][] A)
  {
    if (A == null || A[0] == null)
      return new int[0][];

    for (int i = 0; i < A.GetLength(0); i++)
    {
      // flip the image horizontally
      Array.Reverse(A[i]);

      // invert the image
      for (int j = 0; j < A[i].Length; j++)
      {
        A[i][j] ^= 1;
      }
    }

    return A;
  }

  static void Main(string[] args)
  {
    int[][] myImg = new int[5][] {
      new int[3] { 1, 1, 0 },
      new int[3] { 1, 0, 1 },
      new int[3] { 0, 0, 0 },
      new int[3] { 1, 0, 1 },
      new int[3] { 1, 1, 0 },
    };

    new Program().FlipAndInvertImage(myImg);

    for (int i = 0; i < myImg.GetLength(0); i++)
    {
      int[] row = myImg[i];

      for (int j = 0; j < row.Length; j++)
      {
        if (j != row.Length - 1)
        {
          Console.Write($"{row[j]}, ");
        }
        else
        {
          Console.Write($"{row[j]}\n");
        }
      }
    }
  }
}
