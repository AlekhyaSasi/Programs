import java.util.*;
import java.lang.*;
import java.io.*;
/* Name of the class has to be "Main" only if the class is public. */
 class LehmerRng
{
 final int a = 16807;
  final int m = 2147483647;
  final int q = 127773;
  final int r = 2836;
  private int seed;
  public LehmerRng(int seed)
  {
    if (seed <= 0 || seed == 2147483647)
      System.out.println("Bad Seed");
    this.seed = seed;
  }
  public double Next()
  {
    int hi = seed / q;
    int lo = seed % q;
    seed = (a * lo) - (r * hi);
    if (seed <= 0)
      seed = seed + m;
    return (seed * 1.0) / m;
