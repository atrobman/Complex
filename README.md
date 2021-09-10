# Complex

I was very bored one day and curious about how imaginary numbers work in computers, so I decided to write a little implementation myself. I also added two small tests to show that my implementation was working in the form of the Mandelbrot Set.

### Mandelbrot.py

This file generates an image of the Mandelbrot Set. Be warned, this takes quite a bit of time to run at the included settings, but it generates a very nice image

### Pi.py

There is a funny little quirk about the Mandelbrot Set that I learned recently (from when I coded this program, anyways). You can learn more about the specifics of why this works from [this video](https://www.youtube.com/watch?v=d0vY0CKYhPY), but the gist of it is that you can calculate Pi (INCREDIBLY INEFFICIENTLY) from the Mandelbrot set by approaching the point -0.75 + 0i and looking at the number of iterations that it takes for the point to explode out past the bounding circle of radius 2 around the Mandelbrot set. I stopped at 6 iterations of this calculation since every step gets exponentially longer, but you can uncomment out c7 if you dare.
