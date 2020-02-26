# So Meta
After downloading the image, run the [imagemagick](imagemagick.org) command `identify -verbose pico_img.png` on it. This gives 
all the metadata: 
```
Image: pico_img.png
  Format: PNG (Portable Network Graphics)
  Mime type: image/png
  Class: DirectClass
  Geometry: 600x600+0+0
  Units: Undefined
  Colorspace: sRGB
  Type: TrueColor
  Base type: Undefined
  Endianess: Undefined
  Depth: 8-bit
  Channel depth:
    Red: 8-bit
    Green: 8-bit
    Blue: 8-bit
  Channel statistics:
    Pixels: 360000
    Red:
      min: 0  (0)
      max: 255 (1)
      mean: 179.084 (0.70229)
      standard deviation: 98.4394 (0.386037)
      kurtosis: -1.65464
      skewness: -0.557373
      entropy: 0.262552
    Green:
      min: 0  (0)
      max: 255 (1)
      mean: 179.084 (0.702288)
      standard deviation: 98.4398 (0.386038)
      kurtosis: -1.65463
      skewness: -0.557375
      entropy: 0.262631
    Blue:
      min: 0  (0)
      max: 255 (1)
      mean: 179.084 (0.702291)
      standard deviation: 98.4393 (0.386037)
      kurtosis: -1.65464
      skewness: -0.557372
      entropy: 0.262415
  Image statistics:
    Overall:
      min: 0  (0)
      max: 255 (1)
      mean: 179.084 (0.70229)
      standard deviation: 98.4395 (0.386037)
      kurtosis: -1.65463
      skewness: -0.557375
      entropy: 0.262533
  Colors: 843
  Histogram:
        36: (  0,  0,  0) #000000 black
         1: (  1,  0,  1) #010001 srgb(1,0,1)
        [...REMOVED BECAUSE ITS TOO LONG...]
       121: (255,254,255) #FFFEFF srgb(255,254,255)
         4: (255,255,254) #FFFFFE srgb(255,255,254)
    217948: (255,255,255) #FFFFFF white
  Rendering intent: Perceptual
  Gamma: 0.454545
  Chromaticity:
    red primary: (0.64,0.33)
    green primary: (0.3,0.6)
    blue primary: (0.15,0.06)
    white point: (0.3127,0.329)
  Matte color: grey74
  Background color: white
  Border color: srgb(223,223,223)
  Transparent color: none
  Interlace: None
  Intensity: Undefined
  Compose: Over
  Page geometry: 600x600+0+0
  Dispose: Undefined
  Iterations: 0
  Compression: Zip
  Orientation: Undefined
  Properties:
    Artist: picoCTF{s0_m3ta_368a0341}
    date:create: 2019-10-22T23:49:23+00:00
    date:modify: 2019-09-28T21:50:58+00:00
    png:IHDR.bit-depth-orig: 8
    png:IHDR.bit_depth: 8
    png:IHDR.color-type-orig: 2
    png:IHDR.color_type: 2 (Truecolor)
    png:IHDR.interlace_method: 0 (Not interlaced)
    png:IHDR.width,height: 600, 600
    png:sRGB: intent=0 (Perceptual Intent)
    png:text: 2 tEXt/zTXt/iTXt chunks were found
    signature: c58b4e54359656f5ca62919f091dc1df941c504bbda927f61ad05efb88bef7f1
    Software: Adobe ImageReady
  Artifacts:
    verbose: true
  Tainted: False
  Filesize: 108795B
  Number pixels: 360000
  Pixels per second: 18.4689MP
  User time: 0.010u
  Elapsed time: 0:01.019
  Version: ImageMagick 7.0.8-68 Q16 x86_64 2019-10-07 https://imagemagick.org
```
Or you could use `identify pico_img.png  | pbcopy `

flag: `picoCTF{s0_m3ta_368a0341}`