# Simple ASCII Art generator

A simple Python tool to convert images to ASCII ART.

```
Usage: ascii.py [OPTIONS] FILEPATH [FOLDER]

Options:
  --low INTEGER      Enhance dark areas of the image
  --high INTEGER     Enhance bright areas of the image
  --columns INTEGER  ASCII text width
  --inverse          Inverse colors
  --help             Show this message and exit.
```

## Animated GIFs

If `FILEPATH` points to an animated GIF and a `FOLDER` argument is given,
each frame is converted to ASCII and saved into that folder as
`0001.txt`, `0002.txt`, `0003.txt`, ... The folder is created if needed.

```
ascii.py animation.gif frames/
```

Without the `FOLDER` argument the GIF is treated like any other image
and only its first frame is printed to stdout.

```



                                                                      `
                                                                L¢3RßBZ
                                                           *Ê¶¶¶G±ØQN¶¶±
                                                        ??%¶¶¶¶¶G 0R5r"RÊ
                                                      ±&¶¶¶¶¶¶åRß?²¢$GAÔÊ+
                                                    .ZB¶¶¶¶¶¶ÆQ8& zF²LyL1S;
                                                   ²ÊNØ@¶¶¶¶¶RRß8(  ; r%Ãkk,
                             !c7L+¤;              ¢¶¶¶¶¶¶¶¶ØBÔR80k     ²². L
                        LGB¶¶¶¶¶¶¶¶¶¶¶¶MB&0$XZZmÆ¶¶¶¶¶¶¶@åBNÊÔ05A7
             ^ñåØB&8å0Ø¶¶¶¶¶¶¶¶¶@ØÆ@¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶@ØBßßßß0ñS
          ¢±ñmm0XA3ñ,*¶@@@¶¶¶¶¶¶¶@MåBBÆ@¶¶¶@@¶ååØØ@@Ø¶ØBÆåNåØÆ&5f
        ?ÆGf?c?r+c¤¿ 7BåØÆØåÊßNNNåNßÊÊBÆ@@Ø@@ØBNBNÊÔßNÊBåBNMØ@8Sz
       ?MXÝª^.`:''   *kXQNNQm8Q&mZ$RÊNÊBåBBÊNÊÊßÔRmGm8R88QRÊBÊ&kAÝ
      ªMmSJ¿"**!"',';' *1FG88QQÔB#t1X&&Q#&Q&&Q#RQ&XkÀ8ßÔ8&ÃÃ&XzSS?
      ÀmkÝ713L;LLLCr     "?CFzÝz±±   *¿CÝFñAGZAAAZñfkmÔNÊßÃFL/?¿?
   k&#&2CtLª' ^?C1         "77JyÝL       ^²+ªtttCFyr(ZAAGÔØX* ;¿±*
   CZA%CL;                   ª3Ý7                    '²15$mBØZf¿tSk²
    z3c:                     !¢r^                         ^JZÊå$+  ?±±
                             (¢7¤                             +$G    L;
                             ²?!¿'                            c/     ,7
                             ?c"  ^;                        .%1      "zJ
                              ¤!     cr                    +Ýr       ;L(
                                ^      ;/                             "
                                *²
                                 Ýc


```
